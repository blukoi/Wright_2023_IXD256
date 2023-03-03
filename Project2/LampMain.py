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
counter = 0;

btn = Pin(21, Pin.IN, Pin.PULL_UP);

tof = unit.get(unit.TOF, unit.PORTA);

angle = unit.get(unit.ANGLE, (23,33));
b = None;
brightness = None;

# map an input value (v_in) between min/max ranges:
def map_value(in_val, in_min, in_max, out_min, out_max):
    v = out_min + (in_val - in_min) * (out_max - out_min) / (in_max - in_min);
    if (v < out_min):
        v = out_min;
    elif (v > out_max):
        v = out_max;
    return int(v);

def turnRed():
    counter = 0;
    for i in range(30):
        red = (5 + int(d_55) + int(brightness));
        green = 0;
        blue = 0;
        neopixel_strip[i] = (red, green, blue);
        neopixel_strip.write();
        counter += 1;
        sleep(.05);

def breatheRed():
    for i in range(30):
        red = (5 + int(d_55) + int(brightness));
        green = 5 + int(d_55);
        blue = 5 + int(d_55);
        neopixel_strip[i] = (red, green, blue);
        neopixel_strip.write();

def turnGreen():
    for i in range(30):
        red = 0;
        green = (5 + int(d_55) + int(brightness));
        blue = 0;
        neopixel_strip[i] = (red, green, blue);
        neopixel_strip.write();
        sleep(.05);

def turnBlue():
    for i in range(30):
        red = 0;
        green = 0;
        blue = (5 + int(d_55) + int(brightness));
        neopixel_strip[i] = (red, green, blue);
        neopixel_strip.write();
        sleep(.05);

def turnWhite():
    for i in range(30):
        red = (5 + int(d_55) + int(brightness));
        green = (5 + int(d_55) + int(brightness));
        blue = (5 + int(d_55) + int(brightness));
        neopixel_strip[i] = (red, green, blue);
        neopixel_strip.write();
        sleep(.05);

def turnOff():
    for i in range(30):
        red = 0;
        green = 0;
        blue = 0;
        neopixel_strip[i] = (red, green, blue);
        neopixel_strip.write();
        sleep(.05);

while True:
    d = tof.distance;
    d_55 = map_value(d, in_min = 0, in_max = 8192, out_min = 0, out_max = 150);
    b = angle.read();
    brightness = map_value(b, in_min = 0, in_max = 775, out_min = 0, out_max = 100);
    red = 0;
    green = 0;
    blue = 0;
    if (code1 == code2) and (ticks_ms() > code_timer+500):
        code1 += 1;
        code_timer = ticks_ms();
    if code1 >= codemax:
        code1 = 1;
        code2 = 0;
    if mode == "OFF":
        print("LIGHTS OFF");
        turnOff();
        if (code1 > code2) and (ticks_ms() > sensor_timer+100) and (btn.value() == 0):
            print('SWITCHING');
            mode = "RED";
            code2 += 1;
            sensor_timer = ticks_ms();
    if mode == "RED":
        print("RED");
        if counter < 29:
            turnRed();
            print("TURNING");
        if counter >= 29:
            breatheRed();
            print("BREATHING");
        if (code1 > code2) and (ticks_ms() > sensor_timer+100) and (btn.value() == 0):
            print('SWITCHING');
            mode = "GREEN";
            code2 += 1;
            sensor_timer = ticks_ms();
    if mode == "GREEN":
        print("GREEN");
        turnGreen();
        counter = 0;
        if (code1 > code2) and (ticks_ms() > sensor_timer+100) and (btn.value() == 0):
            print('SWITCHING');
            mode = "BLUE";
            code2 += 1;
            sensor_timer = ticks_ms();
    if mode == "BLUE":
        print("BLUE");
        turnBlue();
        counter = 0;
        if (code1 > code2) and (ticks_ms() > sensor_timer+100) and (btn.value() == 0):
            print('SWITCHING');
            mode = "WHITE";
            code2 += 1;
            sensor_timer = ticks_ms();
    if mode == "WHITE":
        print("WHITE");
        turnWhite();
        counter = 0;
        if (code1 > code2) and (ticks_ms() > sensor_timer+100) and (btn.value() == 0):
            print('SWITCHING');
            mode = "OFF";
            code2 += 1;
            sensor_timer = ticks_ms();
    '''if (code1 > code2) and (ticks_ms() > sensor_timer+500):
        print('PART ONE WORKING');
        # print(d_55);
        if btn.value() == 0:
            print('part 2 worked');
            if mode == "OFF":
                mode = "RED";
                code2 += 1;
                counter = 0;
                turnRed();
            elif mode == "RED":
                mode = "GREEN";
                code2 += 1;
                counter = 0;
                turnGreen();
            elif mode == "GREEN":
                mode = "BLUE";
                code2 += 1;
                counter = 0;
                turnBlue();
            elif mode == "BLUE":
                mode = "WHITE";
                code2 += 1;
                counter = 0;
                turnWhite();
            elif mode == "WHITE":
                mode = "OFF";
                code2 += 1;
                counter = 0;
                turnOff();
        sensor_timer = ticks_ms()'''