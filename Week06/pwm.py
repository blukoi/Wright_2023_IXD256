"""

breathe.py

"""

from time import sleep
from machine import Pin, PWM

pwm = PWM(Pin(27))
pwm.freq(1000)

while True:
    for i in range(0,101,1):
        if i == 0:
            print("inhale")
        pwm.duty(i)
        sleep(0.001)
    for i in range(100, -1, -1):
        if i == 100:
            print("exhale")
        pwm.duty(i)
        sleep(0.001)