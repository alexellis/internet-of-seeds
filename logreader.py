import time
from envir import Envir

class LogReader:
    def __init__(self, config):
        self.config = config
        self.envir = Envir()

    def read(self):
        vals = self.envir.read()
        current_time = time.strftime(time.ctime())
        formatted = "Ambient: " + vals["ambient"] +" deg C, " + vals["pressure"] +" hPa, " + current_time
        return formatted
