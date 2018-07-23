from w1thermsensor import W1ThermSensor
import time

while True:
   for sensor in W1ThermSensor.get_available_sensors([W1ThermSensor.THERM_SENSOR_DS18B20]):
      print("Sensor %s has temperature %.2f" % (sensor.id, sensor.get_temperature()))
   time.sleep(1)
