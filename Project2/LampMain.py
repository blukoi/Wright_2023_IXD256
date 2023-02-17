from machine import Pin, ADC
from time import *
from neopixel import NeoPixel

analog_pin = Pin(32, Pin.IN)  # configure input on pin G32 (white wire)
adc = ADC(analog_pin)  # create analog-to-digital converter (ADC) input
adc.atten(ADC.ATTN_11DB)  # set 11dB attenuation (2.45V range)

# neopixel_pin = Pin(27, Pin.OUT) #configure output to G27 to use the 5x5 screen on Atom Matrix
                                    #If using G27, change 30 to 25
neopixel_pin = Pin(26, Pin.OUT) #configure output on pin G26 (yellow wire)
neopixel_strip = NeoPixel(neopixel_pin, 30) #create NeoPixel object with 30 pixels

red = 255;
green = 0;
blue = 0;


led1 = Pin(22, Pin.IN);
led2 = Pin(19, Pin.IN);
led3 = Pin(23, Pin.IN);
led4 = Pin(33, Pin.IN);

mode = "0";

btn = Pin(21, Pin.IN, Pin.PULL_UP);

# map an input value (v_in) between min/max ranges:
def map_value(in_val, in_min, in_max, out_min, out_max):
    v = out_min + (in_val - in_min) * (out_max - out_min) / (in_max - in_min);
    if (v < out_min):
        v = out_min;
    elif (v > out_max):
        v = out_max;
    return int(v);

while True:
    if (mode == "0") and (btn.value() == 1):
        mode = "1";
    elif (mode == "1") and (btn.value() == 1):
        mode = "2";
    elif (mode == "2") and (btn.value() == 1):
        mode = "3";
    elif (mode == "3") and (btn.value() == 1):
        mode = "4";