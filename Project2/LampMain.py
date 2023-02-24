from m5stack import * # import m5stack libraries
import unit # import m5stack unit library
from machine import Pin, ADC
from time import *
from neopixel import NeoPixel

'''analog_pin = Pin(32, Pin.IN)  # configure input on pin G32 (white wire)
adc = ADC(analog_pin)  # create analog-to-digital converter (ADC) input
adc.atten(ADC.ATTN_11DB)  # set 11dB attenuation (2.45V range)'''

# neopixel_pin = Pin(27, Pin.OUT) #configure output to G27 to use the 5x5 screen on Atom Matrix
                                    #If using G27, change 30 to 25
neopixel_pin = Pin(25, Pin.OUT) #configure output on pin G26 (yellow wire)
neopixel_strip = NeoPixel(neopixel_pin, 30) #create NeoPixel object with 30 pixels

red = 0;
green = 0;
blue = 0;

'''led1 = Pin(22, Pin.OUT);
led2 = Pin(19, Pin.OUT);
led3 = Pin(23, Pin.OUT);
led4 = Pin(33, Pin.OUT);'''

mode = "OFF";

sensor_timer = ticks_ms();
code1 = 1;
code2 = 0;
codemax = 6;
code_timer = ticks_ms();
light_timer = ticks_ms();

btn = Pin(21, Pin.IN, Pin.PULL_UP);

tof = unit.get(unit.TOF, unit.PORTA);

# map an input value (v_in) between min/max ranges:
def map_value(in_val, in_min, in_max, out_min, out_max):
    v = out_min + (in_val - in_min) * (out_max - out_min) / (in_max - in_min);
    if (v < out_min):
        v = out_min;
    elif (v > out_max):
        v = out_max;
    return int(v);

# TEST AREA
'''while True:
    print("Testing:")
    sleep(.5);
    if (mode == "0") and (btn.value() == 0):
        print("Button is working");
        led1.off();
        led2.off();
        led3.off();
        led4.off();
        sleep_ms(100);
    if (mode == "0") and (btn.value() == 1):
        print("Broken button");
        sleep(.5);'''

while True:
    d = tof.distance;
    d_55 = map_value(d, in_min = 0, in_max = 8192, out_min = 0, out_max = 50);
    b = 0;
    brightness = map_value(b, in_min = 0, in_max = 4056, out_min = 0, out_max = 100);
    if (code1 > code2) and (ticks_ms() > sensor_timer+500):
        print('PART ONE WORKING');
        print(d_55);
        if btn.value() == 0:
            print('part 2 worked');
            if mode == "OFF":
                mode = "RED";
                code2 += 1;
                '''led1.on();
                led2.off();
                led3.off();
                led4.off();'''
                for i in range(30):
                    red = (205 + int(d_55));
                    green = 0;
                    blue = 0;
                    neopixel_strip[i] = (red, green, blue);
                    neopixel_strip.write();
                    sleep(.05);
            elif mode == "RED":
                mode = "GREEN";
                code2 += 1;
                '''led1.off();
                led2.on();
                led3.off();
                led4.off();'''
                for i in range(30):
                    red = 0;
                    green = (205 + int(d_55));
                    blue = 0;
                    neopixel_strip[i] = (red, green, blue);
                    neopixel_strip.write();
                    sleep(.05);
            elif mode == "GREEN":
                mode = "BLUE";
                code2 += 1;
                '''led1.off();
                led2.off();
                led3.on();
                led4.off();'''
                for i in range(30):
                    red = 0;
                    green = 0;
                    blue = (205 + int(d_55));
                    neopixel_strip[i] = (red, green, blue);
                    neopixel_strip.write();
                    sleep(.05);
            elif mode == "BLUE":
                mode = "WHITE";
                code2 += 1;
                '''led1.off();
                led2.off();
                led3.off();
                led4.on();'''
                for i in range(30):
                    red = (105 + int(d_55) - int(brightness));
                    green = (205 + int(d_55));
                    blue = (205 + int(d_55));
                    neopixel_strip[i] = (red, green, blue);
                    neopixel_strip.write();
                    sleep(.05);
            elif mode == "WHITE":
                mode = "OFF";
                code2 += 1;
                '''led1.off();
                led2.off();
                led3.off();
                led4.off();'''
                for i in range(30):
                    red = 0;
                    green = 0;
                    blue = 0;
                    neopixel_strip[i] = (red, green, blue);
                    neopixel_strip.write();
                    sleep(.05);
        sensor_timer = ticks_ms()
    elif (code1 == code2) and (ticks_ms() > code_timer+500):
        code1 += 1;
        code_timer = ticks_ms();
    elif code1 >= codemax:
        code1 = 1;
        code2 = 0;

'''
    if (mode == "0") and (btn.value() == 1):
        led1.off();
        led2.off();
        led3.off();
        led4.off();
        sleep(.5);
    if (mode == "0") and (btn.value() == 0) and (code1 > code2):
        mode = "1";
        code2 += 1;
        led1.on();
        led2.off();
        led3.off();
        led4.off();
        sleep(.5);
    elif (mode == "1") and (btn.value() == 0) and (code1 > code2):
        mode = "2";
        code2 += 1;
        led1.off();
        led2.on();
        led3.off();
        led4.off();
        sleep(.5);
    elif (mode == "2") and (btn.value() == 0) and (code1 > code2):
        mode = "3";
        code2 += 1;
        led1.off();
        led2.off();
        led3.on();
        led4.off();
        sleep(.5);
    elif (mode == "3") and (btn.value() == 0) and (code1 > code2):
        mode = "4";
        code2 += 1;
        led1.off();
        led2.off();
        led3.off();
        led4.on();
        sleep(.5);
    elif (mode == "4") and (btn.value() == 0) and (code1 > code2):
        mode = "0";
        code2 += 1;
        led1.off();
        led2.off();
        led3.off();
        led4.off();
        sleep(.5);
    elif (code1 == code2):
        code1 += 1;'''