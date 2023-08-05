from six.moves import queue

import logging
import threading
import time

logger = logging.getLogger(__name__)


class QueueEvent(object):
    def __init__(self, name):
        self.name = name
        self.event = threading.Event()

    def __repr__(self):
        return ('{}({})'.format(type(self).__name__, self.name))

    def set(self):
        return self.event.set()

    def wait(self, timeout=None):
        return self.event.wait(timeout)


class QueueExitEvent(QueueEvent):
    pass


class Queue(object):
    def __init__(self, capacity):
        self.EXIT_EVENT = QueueExitEvent('EXIT')
        self._queue = queue.Queue(maxsize=capacity)

    def _gets(self, count, timeout):
        start_time = time.time()
        elapsed_time = 0
        cnt = 0
        while cnt < count:
            try:
                item = self._queue.get(block=False)
                yield item
                if isinstance(item, QueueEvent):
                    return
            except queue.Empty:
                break
            cnt += 1
        while cnt < count:
            wait_time = max(timeout - elapsed_time, 0)
            try:
                item = self._queue.get(block=True, timeout=wait_time)
                yield item
                if isinstance(item, QueueEvent):
                    return
            except queue.Empty:
                break
            cnt += 1
            elapsed_time = time.time() - start_time

    def gets(self, count, timeout):
        return tuple(self._gets(count, timeout))

    def is_empty(self):
        return not self._queue.qsize()

    def flush(self, timeout=None):
        if self._queue.qsize() == 0:
            return 0
        start_time = time.time()
        wait_time = timeout
        event = QueueEvent('SYNC(timeout={})'.format(wait_time))
        try:
            self._queue.put(event, block=True, timeout=wait_time)
        except queue.Full:
            return
        elapsed_time = time.time() - start_time
        wait_time = timeout and max(timeout - elapsed_time, 0)
        if event.wait(wait_time):
            return time.time() - start_time  # time taken to flush

    def put(self, item, block=True, timeout=None):
        try:
            self._queue.put(item, block, timeout)
        except queue.Full:
            logger.warning('Queue is full. Dropping telemetry.')

    def puts(self, items, block=True, timeout=None):
        if block and timeout is not None:
            start_time = time.time()
            elapsed_time = 0
            for item in items:
                wait_time = max(timeout - elapsed_time, 0)
                self.put(item, block=True, timeout=wait_time)
                elapsed_time = time.time() - start_time
        else:
            for item in items:
                self.put(item, block, timeout)
