import time

class Camera:
    def __init__(self, config, picamera):
        self.config = config
        self.picamera = picamera

    def clone(self, source, destination):
        with open(source, 'rb') as f1: 
            with open(destination, 'wb') as f2:
                f2.write(f1.read())

    def capture(self):
       cam = self.picamera.PiCamera()
       cam.resolution = (2048, 1536)
       cam.hflip = True
       cam.vflip = True
       filename = self.config["working_directory"] + 'images/image-' + self.get_ts() + '.jpg'
       cam.capture(filename, quality=self.config["image_quality"])
       self.clone(filename, self.config["working_directory"] + "latest.jpg")

       return filename

    def get_ts(self):
       ts = time.strftime('%Y-%m-%d-%H-%M')
       return ts

import config as cfg
#import fakecamera as picamera
import picamera
camera1 = Camera(cfg.config, picamera)
print(camera1.capture())
