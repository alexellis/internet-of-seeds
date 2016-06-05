from PIL import Image, ImageFont, ImageDraw
import datetime

class Watermark:
    def __init__(self, config):
        self.config = config
        self
    def mark(self, filename, values):
        print("Applying watermark to: " + filename)

        img = Image.open(filename)
        img = img.resize((1438, 1080))

        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype(self.config["working_directory"] + '/roboto/Roboto-Regular.ttf', 36)
        draw.text((10, 10), values, (0, 0, 0), font=font)
        print("Writing image back to: " + filename)
        img.save(filename)

#import config as cfg

#w = Watermark(cfg.config)
#w.mark("./latest.jpg", "Sensor data being worked on")

