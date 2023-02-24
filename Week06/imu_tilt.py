# IMU example (intertial measurement unit built into Atom Matrix)
from m5stack import * # import m5stack libraries
import unit # import m5stack unit library
import imu # import m5stack imu unit
from time import *

imu = imu.IMU();

left = ([
    0,0,0xffffff,0,0,
    0,0xffffff,0,0,0,
    0xffffff,0xffffff,0xffffff,0xffffff,0xffffff,
    0,0xffffff,0,0,0,
    0,0,0xffffff,0,0
    ]);
right = ([
    0,0,0xffffff,0,0,
    0,0,0,0xffffff,0,
    0xffffff,0xffffff,0xffffff,0xffffff,0xffffff,
    0,0,0,0xffffff,0,
    0,0,0xffffff,0,0
    ]);

state = "RIGHT";

while True:
    acc_x = imu.acceleration[0];
    # print(acc_x);
    if(state == "RIGHT"):
        if(acc_x < -0.25):
            state = "LEFT";
            rgb.set_screen(left);
            print("tilt left");
    elif(state == "LEFT"):
        if(acc_x > 0.25):
            state = "RIGHT";
            rgb.set_screen(right);
            print("tilt right");
    sleep_ms(100);