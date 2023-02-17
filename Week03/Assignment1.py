from time import *
from machine import Pin

led_off = Pin(32, Pin.OUT);
led_on = Pin(25, Pin.OUT);
# timer_ms = ticks_ms();
# program_state = 'OFF'
btn = Pin(26, Pin.IN, Pin.PULL_UP);

while True:
    if(btn.value() == 1):
        led_on.on();
        led_off.off();
    elif(btn.value() == 0):
        led_off.on();
        led_on.off();