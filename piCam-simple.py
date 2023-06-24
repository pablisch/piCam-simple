from picamera import PiCamera
from time import sleep

camera = PiCamera()


for i in range(5):
    camera.start_preview()
    sleep(5)
    camera.capture('/home/pi/image%s.jpg' % i)
    sleep(1)
    camera.stop_preview()
    sleep(1)