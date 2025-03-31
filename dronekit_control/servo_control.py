import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setup(3, GPIO.OUT)
servo=GPIO.PWM(3, 50)
servo.start(0)


def SetAngle(angle):
    duty = angle / 18 + 2
    GPIO.output(3, True)
    servo.ChangeDutyCycle(duty)
    sleep(1)
    GPIO.output(3, False)
    servo.ChangeDutyCycle(0)
    
#SetAngle(200)
#sleep(5)
#SetAngle(0)

def close():
    SetAngle(200)
def open_box():
    SetAngle(0)
"""
open_box()
sleep(3)
close()
"""
servo.stop()
#GPIO.cleanup()
