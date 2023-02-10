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

# map an input value (v_in) between min/max ranges:
def map_value(in_val, in_min, in_max, out_min, out_max):
    v = out_min + (in_val - in_min) * (out_max - out_min) / (in_max - in_min);
    if (v < out_min):
        v = out_min;
    elif (v > out_max):
        v = out_max;
    return int(v);

while True:
    analog_val = adc.read();  # read 12-bit analog value (0 - 4095 range)
    analog_val_8bit = map_value(analog_val, in_min = 0, in_max = 4095, out_min = 0, out_max = 255);
    analog_val_30 = map_value(analog_val, in_min = 0, in_max = 4095, out_min = 0, out_max = 29);
    print(analog_val)
    # print(analog_val_30);
    for pixel_index in range(30):
        '''r = (analog_val_8bit, 0, 0); # red color that changes with ADC value
        g = (0, analog_val_8bit, 0);
        b = (0, 0, analog_val_8bit);'''
        x = (round(analog_val_30*8.5), 0, 0);
        y = (0, 0, round(analog_val_30*5));
        z = (0, 0, 0);

        if (pixel_index < analog_val_30):
            neopixel_strip[pixel_index] = x;
            neopixel_strip[pixel_index-1] = y;
        elif (analog_val_30 == 0):
            neopixel_strip[pixel_index-1] = z;
        else:
            neopixel_strip[pixel_index] = y;

        # neopixel_strip[pixel_index] = x; # assign pixel to red color
        # neopixel_strip[0, (pixel_index-1)] = y;
    neopixel_strip.write(); # write color data to neopixels
    sleep_ms(100);