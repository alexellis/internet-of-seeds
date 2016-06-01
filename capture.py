#!/usr/bin/python

import config as cfg
#import fakecamera as picamera
import picamera
from camera import Camera
from watermark import Watermark
from logreader import LogReader

class Capture:
    def __init__(self, config):
        self.config = config
        self.camera = Camera(cfg.config, picamera)
        self.watermark = Watermark(cfg.config)
        self.log_reader = LogReader(cfg.config)

    def process(self):
        latest_image = self.config["working_directory"] + "latest.jpg"
        file_name = self.camera.capture()
        sensor_data = self.log_reader.read()
        print("Marking sensor data: " + sensor_data)
        self.watermark.mark(latest_image, sensor_data)

capture = Capture(cfg.config)
capture.process()
