from m5stack import * # import m5stack libraries
import unit # import m5stack unit library
from machine import Pin, ADC
from time import *
from neopixel import NeoPixel

angle = unit.get(unit.ANGLE, (23,33));
x = None;
x_adj = None;

# map an input value (v_in) between min/max ranges:
def map_value(in_val, in_min, in_max, out_min, out_max):
    v = out_min + (in_val - in_min) * (out_max - out_min) / (in_max - in_min);
    if (v < out_min):
        v = out_min;
    elif (v > out_max):
        v = out_max;
    return int(v);

while True:
    x = angle.read();
    x_adj = map_value(x, in_min = 0, in_max = 775, out_min = 0, out_max = 100);
    print(x_adj);
    sleep(.5);