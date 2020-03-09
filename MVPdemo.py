#!//home/pi/Desktop/MetaBell
#motion button camera trigger
import RPi.GPIO as GPIO
from picamera import PiCamera
import time


#global number

GPIO.setmode(GPIO.BOARD)



numberPic = 0 
numberVid = 0

GPIO.setup(29,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(16,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
temp = 0
camera = PiCamera()
while True:
    if GPIO.input(29) == GPIO.HIGH:
        print("doorbell")
        filenom = "/home/pi/Desktop/MetaBell/vid"+time.strftime("%d-%m-%Y|%H:%M:%S")+".h264"
        camera.start_recording(filenom)
        time.sleep(10)
        camera.stop_recording()

    if GPIO.input(16) == GPIO.HIGH:
        print("motion")
        print(numberPic)
        filename = "/home/pi/Desktop/MetaBell/test"+time.strftime("%d-%m-%Y|%H:%M:%S")+".jpg"
        camera.exposure_mode = 'sports'
        camera.capture(filename)
        time.sleep(10)

    
#     if GPIO.input(29) == GPIO.HIGH or GPIO.input(16) == GPIO.HIGH :
#         temp = 1
#     if ((GPIO.input(29) == GPIO.LOW) and (temp==1)) or ((GPIO.input(16) == GPIO.LOW) and temp == 1):
#         temp = 0
#         print("puh")
#         print(number)
#         
#         filename = "/home/pi/Desktop/MetaBell/test"+str(numberPic)+".jpg"
#         print(filename)
#         #camera.start_preview()
#         camera.capture(filename)
#         numberPic += 1
        
          