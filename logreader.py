class LogReader:
    def __init__(self, config):
        self.config = config
    def get_last_line(self, log_file):
        lines = log_file.readlines()
        return lines[len(lines)-1]

    def read(self):
        l = None
        fn = self.config["working_directory"] + 'sensors.log'
        with open(fn) as log_file:
            l = self.get_last_line(log_file)

        ## Format the sensor values nicely for tweeting, run the tweet_pic function.
        sensor_vals = l.rstrip().split('\t')
        valid = False
        status = None
        
        if(len(sensor_vals) == 7):
            status = '%s: Temp: %s C, Press: %s hPa, Light: %s lux, RGB: %s,%s,%s.' % tuple(sensor_vals)
        else:
            status = "No data"
        return status
