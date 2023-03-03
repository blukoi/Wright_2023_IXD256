from m5stack import *
import unit
from time import *
from machine import Pin, ADC
from servo import Servo
from neopixel import NeoPixel
from easyIO import *

analog_pin = Pin(33, Pin.IN) # configure input pin on pin 33
adc = ADC(analog_pin) # create analog input
adc.atten(ADC.ATTN_11DB) # enable full-range on ADC pin

# angle = unit.get(unit.ANGLE, (23,33));

servo_obj = Servo(Pin(26)); # create a Servo object on G26 (yellow wire)
# 2000 or 1000 (depending on direction) seem to be the fastest for m5stack servo
# 1600 ~ moves counter clockwise
# servo_obj.write_us(2000);
# print("1. Servo going counter clockwise");
# sleep(10);
# 1400 ~ moves clockwise
# servo_obj.write_us(1000);
# print("2. Servo going clockwise");
# sleep(10);
# 1500 ~ stops
# servo_obj.write_us(1500);
# print("3. Servo has stopped");

'''# map an input value (v_in) between min/max ranges:
def map_value(in_val, in_min, in_max, out_min, out_max):
    v = out_min + (in_val - in_min) * (out_max - out_min) / (in_max - in_min);
    if (v < out_min):
        v = out_min;
    elif (v > out_max):
        v = out_max;
    return int(v);'''

while True:
    analog_val = adc.read(); # read analog value (0-1024)
    servo_val = map_value(analog_val, 0, 4095, 1000, 1500);
    servo_obj.write_us(servo_val);
    print(servo_val);
    sleep(.1);
