from time import *
from machine import *
from m5stack import *
from m5stack_ui import *
from uiflow import *

screen = M5Screen()
screen.clean_screen()
screen.set_screen_bg_color(0x000)

screenmode = "CALIBRATION"

hours = 00
mins = 00
secs = 00

while True:
    if screenmode == "CALIBRATION":
        label0 = M5Label(hours, x=26, y=96, color=0xFFFFFF, font=FONT_MONT_48, parent=None)
        label1 = M5Label(':', x=103, y=96, color=0xFFFFFF, font=FONT_MONT_48, parent=None)
        label2 = M5Label(mins, x=128, y=96, color=0xFFFFFF, font=FONT_MONT_48, parent=None)
        label3 = M5Label(':', x=204, y=96, color=0xFFFFFF, font=FONT_MONT_48, parent=None)
        label4 = M5Label(secs, x=231, y=96, color=0xFFFFFF, font=FONT_MONT_48, parent=None)
        if btnA.wasPressed:
            hours += 1
        if btnB.wasPressed:
            mins += 1
        if btnC.wasPressed:
            secs += 1
        touch_button0 = M5Btn(text='Set', x=85, y=168, w=150, h=36, bg_c=0x313131, text_c=0xc4c4c4, font=FONT_MONT_18, parent=None);
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
        wait(1)
        secs += 1
        label0 = M5Label(hours, x=26, y=96, color=0xFFFFFF, font=FONT_MONT_48, parent=None)
        label1 = M5Label(':', x=103, y=96, color=0xFFFFFF, font=FONT_MONT_48, parent=None)
        label2 = M5Label(mins, x=128, y=96, color=0xFFFFFF, font=FONT_MONT_48, parent=None)
        label3 = M5Label(':', x=204, y=96, color=0xFFFFFF, font=FONT_MONT_48, parent=None)
        label4 = M5Label(secs, x=231, y=96, color=0xFFFFFF, font=FONT_MONT_48, parent=None)
    '''if screenmode == "DESTINY1":
        '''