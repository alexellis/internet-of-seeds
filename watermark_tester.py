#!/usr/bin/python

import config as cfg
import fakecamera as picamera
from camera import Camera
from watermark import Watermark
from logreader import LogReader

watermark = Watermark(cfg.config)
watermark.mark("./latest.jpg", "No data uplink..")









