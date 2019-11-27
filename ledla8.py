import RPi.GPIO as GPIO
from time import sleep
x=100
GPIO.setmode(GPIO.BCM)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(24,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(25,GPIO.IN,pull_up_down=GPIO.PUD_UP)
sleep (0.1)

#print("GPIO%d = %d; GPIO%d = %d" % (24, GPIO.input(24))

p = GPIO.PWM(23,100)
p.start(0)
while (x<=100 and x>=0):
    p.ChangeDutyCycle(x)
    print("x ",x)
    if GPIO.input(24) == GPIO.HIGH:
        x=x+10
        sleep(0.5)
    if GPIO.input(25) == GPIO.LOW:
        x=x-10
        sleep(0.5)
GPIO.cleanup()