import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setup(5, GPIO.OUT)
servo=GPIO.PWM(3, 50)
servo.start(0)


def SetAngle(angle):
    duty = angle / 18 + 2
    GPIO.output(3, True)
    pwm.ChangeDutyCycle(duty)
    sleep(1)
    GPIO.output(3, False)
    pwm.ChangeDutyCycle(0)
    
SetAngle(90) 
servo.stop()
GPIO.cleanup()
