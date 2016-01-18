import picamera as pc
from time import time, sleep
from datetime import datetime as dt
from datetime import timedelta as td
import os

def wait():
    # Calculate the delay to the start of the next hour
    next_minute = (dt.now() + td(minutes=1)).replace(second=0, microsecond=0)
    delay = (next_minute - dt.now()).seconds
    sleep(delay)



if __name__ == "__main__":

    if "images" not in os.listdir('/home/pi/data/'):
        os.mkdir('/home/pi/data/images')
    
    imgdir = '/home/pi/data/images'


    while True:
        now = dt.now()
        with pc.PiCamera(resolution=(2560,1920)) as p:
            
            p.framerate = 30
            sleep(2)
            # Now fix the values
            p.shutter_speed = p.exposure_speed
            p.exposure_mode = 'off'
            g = p.awb_gains
            p.awb_mode = 'off'
            p.awb_gains = g
            
            p.capture('{0}/{1}.jpg'.format(imgdir, str(now)), format='jpeg')
        wait()
    
