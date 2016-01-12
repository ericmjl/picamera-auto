import picamera as pc
from time import time, sleep
from datetime import datetime as dt
import os


if __name__ == "__main__":

    if "images" not in os.listdir('/home/pi/data/'):
        os.mkdir('/home/pi/data/images')
    
    imgdir = '/home/pi/data/images'


    while True:
        with pc.PiCamera(resolution=(2560,1920)) as p:
            p.exposure_mode = 'beach'
            now = dt.now()
            p.capture('{0}/{1}.jpg'.format(imgdir, str(now)), format='jpeg')
            sleep(60)
    
