# PART ONE: Using a button and LED circuit on breadboard

'''from time import *
from machine import Pin

led_R = Pin(32, Pin.OUT);
led_Y = Pin(25, Pin.OUT);
led_G = Pin(21, Pin.OUT);
btn = Pin(26, Pin.IN, Pin.PULL_UP);

timer_ms = ticks_ms();                      # create a timer variable and save current time
program_state = 'GREEN'

led_pin = Pin(32, Pin.OUT);
pwm = PWM(Pin(32));
btn = Pin(26, Pin.IN, Pin.PULL_UP);

while True:
    for i in range(100):
        pwm.duty(i);
        sleep_ms(10);
    for i in range(100):
        pwm.duty(100-i);
        sleep_ms(10);

while True:
    if(ticks_ms() > timer_ms + 500):
        if(btn.value() == 0):
            if(program_state == 'GREEN'):
                led_G.off();
                led_Y.on();
                program_state = 'YELLOW';
                print(program_state)
            elif(program_state == 'YELLOW'):
                led_Y.off();
                led_R.on();
                program_state = 'RED';
                print(program_state)
            elif(program_state == 'RED'):
                led_R.off();
                led_G.on();
                program_state = 'GREEN';
                print(program_state)
        timer_ms = ticks_ms();

    led_R.on();
    sleep_ms(500);
    led_R.off();
    sleep_ms(500);
    
    led_Y.on();
    sleep_ms(500);
    led_Y.off();
    sleep_ms(500);

    led_G.on();
    sleep_ms(500);
    led_G.off();
    sleep_ms(500);'''

# PART TWO: Starting to use LED strip

from machine import Pin
from time import *
from neopixel import NeoPixel

neo_pin = Pin(26, Pin.OUT);                 # Create an output on pin G26
neo_strip = NeoPixel(neo_pin, 16);     # Calls the number of LEDs to turn on

# neo_strip[0] = (255, 0, 0)                  # Set pixel at index 0 to red color
# neo_strip.write()

# neo_strip[0] = (0, 0, 0)                  # Set pixel at index 0 to black color, or off
# neo_strip.write()

rainbow = [
  (126 , 1 , 0),(114 , 13 , 0),(102 , 25 , 0),(90 , 37 , 0),(78 , 49 , 0),(66 , 61 , 0),(54 , 73 , 0),(42 , 85 , 0),
  (30 , 97 , 0),(18 , 109 , 0),(6 , 121 , 0),(0 , 122 , 5),(0 , 110 , 17),(0 , 98 , 29),(0 , 86 , 41),(0 , 74 , 53),
  (0 , 62 , 65),(0 , 50 , 77),(0 , 38 , 89),(0 , 26 , 101),(0 , 14 , 113),(0 , 2 , 125),(9 , 0 , 118),(21 , 0 , 106),
  (33 , 0 , 94),(45 , 0 , 82),(57 , 0 , 70),(69 , 0 , 58),(81 , 0 , 46),(93 , 0 , 34),(105 , 0 , 22),(117 , 0 , 10)]

while True:
    rainbow = rainbow[-1:] + rainbow[:-1]
    for i in range(16):
        neo_strip[i] = rainbow[i];
    neo_strip.write();
    sleep_ms(100);

    '''for i in range(255):
        for pixel_index in range(16):
            neo_strip[pixel_index] = (i, 0, 0);
        neo_strip.write();
        sleep_ms(10);
    sleep_ms(500);
    neo_strip[0] = (0, 0, 0);
    neo_strip.write();
    sleep_ms(500);'''