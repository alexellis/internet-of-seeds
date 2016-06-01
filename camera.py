import time

class Camera:
    def __init__(self, config, picamera):
        self.config = config
        self.picamera = picamera

    def capture(self):
       cam = self.picamera.PiCamera()
       cam.resolution = (3280, 2464)
       cam.hflip = True
       cam.vflip = True
       filename = self.config["working_directory"] + 'image-' + self.get_ts() + '.jpg'
       cam.capture(filename, quality=self.config["image_quality"])

       return filename

    def get_ts(self):
       ts = time.strftime('%Y-%m-%d-%H-%M')
       return ts

import config as cfg
import fakecamera as picamera
camera1 = Camera(cfg.config, picamera)
print(camera1.capture())
