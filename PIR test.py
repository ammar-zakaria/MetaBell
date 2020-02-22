from gpiozero import LED
from gpiozero import MotionSensor
from picamera import PiCamera
from time import sleep #not sure whether we'll use this

camera = PiCamera()

# camera.start_preview()
# sleep(5)
# camera.stop_preview()

red_led = LED(17)
pir = MotionSensor(4)
red_led.off()

while True:
    pir.wait_for_motion() #for some reason the commands are mixed up
    print("Motion Detected")# I think it depends on what state it starts up in
    red_led.on()
    pir.wait_for_no_motion()
    red_led.off()
    print("Motion Stopped")#

#Its kinda slow to respond should play around with sensitivity on the sensor