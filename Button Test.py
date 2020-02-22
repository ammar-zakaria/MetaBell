import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

while True:
    if GPIO.input(11) == GPIO.HIGH:
        print("pushed")
