class PiCamera:
    def __init__(self):
        self.resolution = (0,0)
        self.hflip = False
        self.vflip = False
    def capture(self, filename, quality):
        print("Capturing " + filename)
        with open(filename, 'wb') as f2:
            f2.write("True")
