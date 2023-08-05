import logging
import random
import threading
import time
import socket
import uuid
import re
from datetime import datetime
from vsp_model_insight_influxdb.common import Options
from vsp_model_insight_influxdb.common.schedule import Queue, QueueEvent
import influxdb_client
from influxdb_client.client.write_api import SYNCHRONOUS

logger = logging.getLogger(__name__)

class ModelPerformanceLogHandler(logging.Handler):

    def __init__(self, **options):
        super(ModelPerformanceLogHandler, self).__init__()
        self.host = socket.gethostname()
        self.sn = str(uuid.uuid4())
        self.options = Options(**options)
        self.export_interval = self.options.export_interval
        self.max_batch_size = self.options.max_batch_size
        self.app_id = self._normalize_key(self.options.application_id)
        self.level = logging.DEBUG
        self.addFilter(SamplingFilter(self.options.logging_sampling_rate))
        self._queue = Queue(capacity=self.options.queue_capacity)
        self._worker = Worker(self._queue, self)
        service = influxdb_client.InfluxDBClient(url=self.options.url,token=self.options.token,org=self.options.org)
        self._table_client = service.write_api(write_options=SYNCHRONOUS)
        self._worker.start()

    def _export(self, batch, event=None):  # pragma: NO COVER
        try:
            if batch:
                envelopes = [self.log_record_to_envelope(x) for x in batch]
                try:
                    for envelope in envelopes:
                        self._table_client.write(bucket=self.options.bucket,org=self.options.org,record=envelope)
                except Exception as e:
                    logger.exception(
                        "There was an error with model performace trace.")
        finally:
            if event:
                event.set()

    def _export_fallback(self, batch, event=None):  # pragma: NO COVER
        try:
            if batch:
                envelopes = [self.log_record_to_envelope(x) for x in batch]
                try:
                    for envelope in envelopes:
                        self._table_client.write(bucket=self.options.bucket,org=self.options.org,record=envelope)
                except Exception as e:
                    logger.exception(
                        "There was an error with model performace trace.")
        finally:
            if event:
                event.set()

    # Close is automatically called as part of logging shutdown
    def close(self, timeout=None):
        if not timeout:
            timeout = self.options.grace_period
        if self._worker:
            self._worker.stop(timeout)
        super(ModelPerformanceLogHandler, self).close()

    def createLock(self):
        self.lock = None

    def emit(self, record):
        self._queue.put(record, block=False)

    def log_record_to_envelope(self, record):
        envelope = {
            "measurement":self.app_id,
            "tags": {"model": self._normalize_key(record.model_signature),"process":record.process,"serialno": self.sn,"host": self.host},
            "fields":record.model_performance,
            "time": int(record.created * 1000000000)
        }
        # for key, value in record.model_performance.items():
        #     p.field(key,value)

        return envelope

    def flush(self, timeout=None):
        if self._queue.is_empty():
            return

        if not self._worker.is_alive():
            logger.warning("Can't flush %s, worker thread is dead. "
                           "Any pending messages will be lost.", self)
            return

        self._queue.flush(timeout=timeout)

    def _normalize_key(self,key:str)->str:
        return re.sub('[^a-zA-Z0-9 ]','',key)


class SamplingFilter(logging.Filter):

    def __init__(self, probability=1.0):
        super(SamplingFilter, self).__init__()
        self.probability = probability

    def filter(self, record):
        if (hasattr(record, 'model_signature') and hasattr(record, 'model_performance') and isinstance(record.model_performance, dict)):
            return random.random() < self.probability
        else:
            return False


class Worker(threading.Thread):
    daemon = True

    def __init__(self, src, dst):
        self._src = src
        self._dst = dst
        self._stopping = False
        super(Worker, self).__init__(
            name='{} Worker'.format(type(dst).__name__)
        )

    def run(self):
        src = self._src
        dst = self._dst
        while True:
            batch = src.gets(dst.max_batch_size, dst.export_interval)

            if batch and batch[-1] is src.EXIT_EVENT:
                dst._export_fallback(batch[:-1])
                break

            if batch and isinstance(batch[-1], QueueEvent):
                try:
                    dst._export(batch[:-1], event=batch[-1])
                except Exception:
                    logger.exception('Unhandled exception from exporter.')
                if batch[-1] is src.EXIT_EVENT:
                    break
                continue  # pragma: NO COVER
            try:
                dst._export(batch)
            except Exception:
                logger.exception('Unhandled exception from exporter.')

    def stop(self, timeout=None):  # pragma: NO COVER
        start_time = time.time()
        wait_time = timeout
        if self.is_alive() and not self._stopping:
            self._stopping = True
            self._src.put(self._src.EXIT_EVENT, block=True, timeout=wait_time)
            elapsed_time = time.time() - start_time
            wait_time = timeout and max(timeout - elapsed_time, 0)
        if self._src.EXIT_EVENT.wait(timeout=wait_time):
            return time.time() - start_time  # time taken to stop
