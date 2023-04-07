from time import *
from machine import *
from m5stack import *
import unit
from m5stack_ui import *
from uiflow import *
import urequests
import wifiCfg
# import datetime
import sys
# import requests
import json
# import logging

# GENERAL VARIABLES

screen = M5Screen()
screen.clean_screen()
screen.set_screen_bg_color(0x000)
screenmode = "TEST"
test = None
testarea = "WORKING"

# change arguments below to connect to the WiFi network, such as 'ACCD':
wifiCfg.doConnect('ACCD', 'tink1930')
# check WiFi connection status:
if wifiCfg.wlan_sta.isconnected():
    screen.set_screen_bg_color(0x00FF00)
    print('connected to WiFi network..')

# SENSORS
angle = unit.get(unit.ANGLE, (35,34));
hover = unit.get(unit.TOF, (19,27));
def map_value(in_val, in_min, in_max, out_min, out_max):
    v = out_min + (in_val - in_min) * (out_max - out_min) / (in_max - in_min);
    if (v < out_min):
        v = out_min;
    elif (v > out_max):
        v = out_max;
    return int(v);

# CLOCK VARIABLES
hours = 14
mins = 27
secs = 0
label0 = None
label1 = None
label2 = None
label3 = None
label4 = None
currenttime = None

# DESTINY VARIABLES
# 25 requests per second !!!
HEADERS = {"X-API-Key":'5324217822ec4b6fbb6c9524520d15bb'}

# username = 

label5 = None
label6 = None
label7 = None

# TEST
touch_button0 = None
# def touch_button0_pressed():
#     # global params
#     screen.set_screen_bg_color(0xff0000)
#     pass

while True:
    x = angle.read();
    x_adj = map_value(x, in_min = 0, in_max = 1024, out_min = 1, out_max = 4);
    y = hover.distance;
    y_adj = map_value(y, in_min = 0, in_max = 8191, out_min = 1, out_max = 10);
    '''if x_adj == 1:
        screedmode = "CLOCK"
    if x_adj == 2:
        screedmode = "DESTINY1"
    if x_adj == 3:
        screedmode = "DESTINY2"
    if x_adj == 4:
        screedmode = "DESTINY3"'''
    if screenmode == "TEST":
        try:
            screen.clean_screen()
            screen.set_screen_bg_color(0xFF0000)
            # touch_button0 = M5Btn(text='Change', x=112, y=198, w=96, h=42, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_14, parent=None)
            # touch_button0.pressed(touch_button0_pressed)
            time = urequests.request(method='GET', url = "http://www.worldtimeapi.org/api/timezone/America/Los_Angeles")
            currenttime = time.json()
            # print(currenttime)
            label0 = M5Label(currenttime['datetime'], x=26, y=96, color=0xFFFFFF, font=FONT_MONT_14, parent=None)
            wait(1)
        except:
            screen.clean_screen()
            screen.set_screen_bg_color(0xFF00FF)
            wait(1)
        '''try:
            response = urequests.request(method='GET', url = "https://timeapi.io/api/Time/current/zone?timeZone=America/Los_Angeles");
            screen.clean_screen()
            screen.set_screen_bg_color(0xFF0000)
        except:
            screen.clean_screen()
            screen.set_screen_bg_color(0x0000FF)
        screen.clean_screen()
        inventoryItem = r.json()
        test = M5Label(inventoryItem['Response']['data']['inventoryItem']['itemName'], x=26, y=96, color=0xFFFFFF, font=FONT_MONT_48, parent=None)
        print(inventoryItem['Response']['data']['inventoryItem']['itemName'])'''
        wait(1)
    if screenmode == "CLOCK":
        if secs >= 59:
            mins += 1
            secs = -1
            if mins >= 59:
                hours += 1
                mins = 0
                if hours >= 24:
                    mins = 0
                    secs = 0
                    hours = 0
        wait(.9230)
        screen.clean_screen()
        secs += 1
        label0 = M5Label(str(hours), x=26, y=96, color=0xFFFFFF, font=FONT_MONT_48, parent=None)
        label1 = M5Label(':', x=103, y=96, color=0xFFFFFF, font=FONT_MONT_48, parent=None)
        label2 = M5Label(str(mins), x=128, y=96, color=0xFFFFFF, font=FONT_MONT_48, parent=None)
        label3 = M5Label(':', x=204, y=96, color=0xFFFFFF, font=FONT_MONT_48, parent=None)
        label4 = M5Label(str(secs), x=231, y=96, color=0xFFFFFF, font=FONT_MONT_48, parent=None)
    if screenmode == "CLOCK2":
        screen.clean_screen()
        # currenttime = datetime.time.now()
        label0 = M5Label(str(currenttime), x=26, y=96, color=0xFFFFFF, font=FONT_MONT_48, parent=None)