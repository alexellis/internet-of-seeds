from Adafruit_BME280 import *

class Envir:

    def read_envir(self):
       sensor = BME280(mode=BME280_OSAMPLE_8)
       degrees = sensor.read_temperature()
       pascals = sensor.read_pressure()
       hectopascals = pascals / 100
       humidity = sensor.read_humidity()

       return {"pressure" : '{0:0.2f}'.format(hectopascals), "ambient": '{0:0.2f}'.format(degrees)  }

    def read(self):
       vals = {}
       vals["cpu"] = self.read_cpu()
       envir = self.read_envir()
       vals["pressure"] = envir["pressure"]
       vals["ambient"] = envir["ambient"]
       return vals
    def read_cpu(self):
       f = open("/sys/class/thermal/thermal_zone0/temp", "r")
       val = float(f.read())
       val = val / 1000.0
       return "{0:.2f}".format(val)

t = Envir()
print(t.read())
