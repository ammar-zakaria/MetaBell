
#!//home/pi/Desktop/MetaBell
#motion button camera trigger
import RPi.GPIO as GPIO
from picamera import PiCamera


#global number

GPIO.setmode(GPIO.BOARD)



number = 0 


GPIO.setup(11,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(7,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
temp = 0
camera = PiCamera()
while True:
    
    if GPIO.input(11) == GPIO.HIGH or GPIO.input(7) == GPIO.HIGH :
        temp = 1
    if ((GPIO.input(11) == GPIO.LOW) and (temp==1)) or ((GPIO.input(7) == GPIO.LOW) and temp == 1):
        temp = 0
        print("puh")
        print(number)
        
        filename = "/home/pi/Desktop/MetaBell/test"+str(number)+".jpg"
        print(filename)
        #camera.start_preview()
        camera.capture(filename)
        number += 1
        
      