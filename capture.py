import config as cfg
import fakecamera as picamera
from camera import Camera
from watermark import Watermark
from logreader import LogReader

class Capture:
    def __init__(self):
        self.camera = Camera(cfg.config, picamera)
        self.watermark = Watermark(cfg.config)
        self.log_reader = LogReader(cfg.config)
    def process(self):
        file_name = self.camera.capture()
        sensor_data = self.log_reader.read()
        self.watermark.mark(file_name, sensor_data)

capture = Capture()
capture.process()
