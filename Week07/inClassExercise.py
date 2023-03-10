from m5stack import *
import unit
from time import *
from machine import Pin, ADC
from servo import Servo
from neopixel import NeoPixel
from easyIO import *
from m5ui import *
from uiflow import *

btn = Pin(39, Pin.IN)
btn_timer = ticks_ms();

neopixel_pin = Pin(27, Pin.OUT)  # configure output on pin G27 (atom matrix display)
neopixel_strip = NeoPixel(neopixel_pin, 25)  # create NeoPixel object with 25 pixels

state = "RED";

code1 = 1;
code2 = 0;
codemax = 3;
code_timer = ticks_ms();
count = 0;

servo_obj = Servo(Pin(26)); # create a Servo object on G26 (yellow wire)

analog_pin = Pin(33, Pin.IN) # configure input pin on pin 33
adc = ADC(analog_pin) # create analog input
adc.atten(ADC.ATTN_11DB) # enable full-range on ADC pin

# define pixel maps for 2 different screen appearances
screenRed = [
    1,0,0,0,1,
    0,1,0,1,0,
    0,0,1,0,0,
    0,1,0,1,0,
    1,0,0,0,1
];
screenYellow = [
    0,0,1,0,0,
    0,0,1,0,0,
    1,1,1,1,1,
    0,0,1,0,0,
    0,0,1,0,0
];
screenGreen = [
    0,1,1,1,0,
    1,0,0,0,1,
    1,0,0,0,1,
    1,0,0,0,1,
    0,1,1,1,0
];

# define some colors
red = (255,0,0);
purple = (130,0,255);
yellow = (255,255,0);
pink = (255,0,255);
green = (0,255,0);
blue = (0,0,255);
black = (0,0,0);

#define a function to get color for a pixel:
def pixel_red(x):
    if(x == 0):
        return black
    else:
        return red
def pixel_yellow(y):
    if(y == 0):
        return black
    else:
        return yellow
def pixel_green(z):
    if(z == 0):
        return black
    else:
        return green

# define a function to display a digit:
def displayScreen(state):
    for i in range(25):
        if (state == "RED"):
            neopixel_strip[i] = pixel_red(screenRed[i])
        elif (state == "YELLOW"):
            neopixel_strip[i] = pixel_yellow(screenYellow[i])
        elif (state == "GREEN"):
            neopixel_strip[i] = pixel_green(screenGreen[i])
    neopixel_strip.write()

while True:
    if state == "RED":
        # print(state);
        for i in range(25):
            displayScreen("RED");
        if code1 > code2 and btn.value() == 0:
            state = "YELLOW";
            code2 += 1;
            print("Button Pressed");
            sleep(.1);
    elif state == "YELLOW":
        # print(state)
        for i in range(25):
            displayScreen("YELLOW");
        if code1 > code2 and btn.value() == 0:
            # print("Pressseeeeddddd");
            count += 1;
            print(count);
            if count >= 15:
                state = "GREEN";
                code2 += 1;
                print("Button Pressed a second time");
                sleep(.1);
        elif code1 > code2 and btn.value() == 1:
            count = 0;
    elif state == "GREEN":
        for i in range(25):
            displayScreen("GREEN");
        analog_val = adc.read(); # read analog value (0-1024)
        servo_val = map_value(analog_val, 0, 4095, 1000, 1500);
        servo_obj.write_us(servo_val);
        print(servo_val);
        sleep(.1);
        if code1 > code2 and btn.value() == 0 and ticks_ms() > code_timer+500:
            state = "RED";
            code2 += 1;
            servo_val = 1500;
            servo_obj.write_us(servo_val);
            print("Button Pressed");
            sleep(.1);
    if code1 == codemax:
        code1 = 1;
        code2 = 0;
    if (code1 == code2) and (ticks_ms() > code_timer+100):
        code1 += 1;
        code_timer = ticks_ms();