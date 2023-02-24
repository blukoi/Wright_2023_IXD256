from m5stack import * # import m5stack libraries
import unit # import m5stack unit library
from machine import Pin, ADC
from time import *
from neopixel import NeoPixel

tof = unit.get(unit.TOF, unit.PORTA);
questionmark = ([
    0, 0xff0000, 0xff0000, 0xff0000, 0,
    0, 0,        0,        0xff0000, 0,
    0, 0,        0xff0000, 0xff0000, 0,
    0, 0,        0,        0,        0,
    0, 0,        0xff0000, 0,        0
    ]);
happy = ([
    0,0x0004ff,0,0x0004ff,0,
    0,0,0,0,0,
    0,0,0x0004ff,0,0,
    0x0004ff,0,0,0,0x0004ff,
    0,0x0004ff,0x0004ff,0x0004ff,0
    ]);
# rgb.set_screen(happy);

state = "?";

# neopixel_pin = Pin(27, Pin.OUT)  # configure output on pin G27 (atom matrix display)
# neopixel_display = NeoPixel(neopixel_pin, 25)  # create NeoPixel object with 25 pixels

# map an input value (v_in) between min/max ranges:
def map_value(in_val, in_min, in_max, out_min, out_max):
    v = out_min + (in_val - in_min) * (out_max - out_min) / (in_max - in_min)
    if (v < out_min): 
        v = out_min 
    elif (v > out_max): 
        v = out_max
    return int(v)

while True:
    d = tof.distance; # get distance from time of flight sensor and turn it into variable d
    print(d);
    # brightness = map_value(d, in_min = 0, in_max = 8192, out_min = 0, out_max = 255);
    # print(brightness);

    if state == "?":
        rgb.set_screen(happy);
        if(d < 1000):
            print("detected proximity!");
            sleep_ms(100);
            state = "happy";
    if state == "happy":
        rgb.set_screen(questionmark);
        if(d > 1000):
            print("unknown prox");
            sleep_ms(100);
            state = "?";

    '''# change of brightness of 30 pixels using ADC value:
    for pixel_index in range(25):
        r = (brightness, 0, 0)  # red color that changes with ADC value
        neopixel_display[pixel_index] = r  # assign pixel to red color
    neopixel_display.write()  # write color data to neopixels'''
    
    sleep_ms(100);
