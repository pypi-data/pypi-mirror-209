from vsp_model_insight_influxdb.common.protocol import BaseObject


class Options(BaseObject):
    def __init__(self, *args, **kwargs):
        super(Options, self).__init__(*args, **kwargs)

    _default = BaseObject(
        bucket=None,
        org=None,
        token=None,
        url=None,
        application_id=None,
        # enable_local_storage=False,
        export_interval=15.0,
        grace_period=5.0,
        logging_sampling_rate=1.0,
        max_batch_size=25,
        queue_capacity=8192,
    )
