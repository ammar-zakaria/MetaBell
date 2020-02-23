#!//home/pi/Desktop/MetaBell

import RPi.GPIO as GPIO
from gpiozero import LED
from gpiozero import MotionSensor
from picamera import PiCamera





GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
temp = 0
while True:
    if GPIO.input(11) == GPIO.HIGH:
        temp = 1
    if (GPIO.input(11) == GPIO.LOW) and (temp==1):
        temp = 0
        print("puh")
        camera = PiCamera()
        camera.start_preview()
        camera.capture('/home/pi/Desktop/MetaBell/test.jpg')
        camera.stop_preview()
        
