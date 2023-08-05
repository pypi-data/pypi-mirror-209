VSP Model Insight
==================================


Installation
------------

::

    pip install vsp-model-insight-influxdb

Prerequisites
-------------

* Create an VSP Model Monitor resource and get the connection string, more information can be found in the official docs.
* Place your connection string directly into your code.
  
Usage
-----

Log
~~~

The **Model Performance Log Handler** allows you to export Python logs to `VSP`.

This example shows how to send a warning level log to Azure Monitor.

.. code:: python

    import logging
    from datetime import datetime
    import time
    import random

    from vsp_model_insight_influxdb.influxdb import ModelPerformanceLogHandler

    logging.basicConfig(level=logging.DEBUG)
    rootlogger = logging.getLogger()
    handler = ModelPerformanceLogHandler(application_id="co",
        bucket='mybucker',org='myorg',token="*****",url="http://localhost:8086")
    rootlogger.addHandler(handler)

    properties = {'model_signature': 'corrosion','model_performance': {'drt': 0.9, 'mat': 0.1}}
    logging.info(f"{datetime.now()}",extra=properties)


References
----------


* `Examples <https://pypi.org/project/vsp_model_insight_influxdb/>`_
