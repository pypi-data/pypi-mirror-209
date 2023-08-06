from pioreactor.background_jobs.monitor import Monitor
from pioreactor.background_jobs.temperature_control import TemperatureController


TemperatureController.MAX_TEMP_TO_REDUCE_HEATING = 81.5
TemperatureController.MAX_TEMP_TO_DISABLE_HEATING = 83.5
TemperatureController.MAX_TEMP_TO_SHUTDOWN = 85.0

Monitor.MAX_TEMP_TO_SHUTDOWN = 85.0
