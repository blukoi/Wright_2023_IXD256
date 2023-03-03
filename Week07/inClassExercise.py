from m5stack import *
import unit
from time import *
from machine import Pin, ADC
from servo import Servo
from neopixel import NeoPixel
from easyIO import *

btn = Pin(39, Pin.IN)
btn_timer = ticks_ms();

neopixel_pin = Pin(27, Pin.OUT)  # configure output on pin G27 (atom matrix display)
neopixel_strip = NeoPixel(neopixel_pin, 25)  # create NeoPixel object with 25 pixels

state = "RED";

code1 = 1;
code2 = 0;
codemax = 6;
code_timer = ticks_ms();

while True:
    if state == "RED":
        for i in range(25):
            neopixel_strip[i] = (255,0,0);
            neopixel_strip.write();
        if code1 > code2 and btn.value() == 0:
            state = "YELLOW";
            code2 += 1;
            print("Button Pressed");
            sleep(.1);
    if state == "YELLOW":
        for i in range(25):
            neopixel_strip[i] = (255,255,0);
            neopixel_strip.write();
        if code1 > code2 and btn.value() == 0:
            state = "YELLOW";
            code2 += 1;
            print("Button Pressed");
            sleep(.1);
    if code1 == codemax:
        code1 = 1;
        code2 = 0;