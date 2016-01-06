import picamera as pc
from time import time, sleep
from datetime import datetime as dt
import os


if __name__ == "__main__":

    if "images" not in os.listdir('/home/pi/data/'):
        os.mkdir('images')
    
    imgdir = '/home/pi/data/images'

    p = pc.PiCamera()

    while True:
        now = dt.now()
        p.capture('{0}/{1}.jpg'.format(imgdir, str(now)), format='jpeg')
        sleep(30)
    
