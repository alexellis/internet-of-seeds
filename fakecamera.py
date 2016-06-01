class PiCamera:
    def __init__(self):
        self.resolution = (0,0)
        self.hflip = False
        self.vflip = False
    def capture(self, filename, quality):
        print("Capturing " + filename)
