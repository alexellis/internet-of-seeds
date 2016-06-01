import time
from PIL import Image

class Camera:
    def __init__(self, config, picamera):
        self.config = config
        self.picamera = picamera

    def clone(self, source, destination):
        x = Image.open(source)
        x.save(destination)
#        with open(source, 'rb') as f1: 
 #           with open(destination, 'wb') as f2:
  #              f2.write(f1.read())

    def capture(self):
       cam = self.picamera.PiCamera()
       cam.start_preview()

       cam.resolution = (2048, 1536)
       cam.hflip = True
       cam.vflip = True
       filename = self.config["working_directory"] + 'images/image-' + self.get_ts() + '.jpg'
       cam.capture(filename, quality=self.config["image_quality"])
       cam.stop_preview()

       self.clone(filename, self.config["working_directory"] + "latest.jpg")

       return filename

    def get_ts(self):
       ts = time.strftime('%Y-%m-%d-%H-%M')
       return ts
