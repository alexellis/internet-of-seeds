import time
import config as cfg
#import fakecamera as picamera
from camera import Camera

import picamera
camera1 = Camera(cfg.config, picamera)
print(camera1.capture())
