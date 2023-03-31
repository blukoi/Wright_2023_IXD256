from m5stack import *
import unit
from time import *
from machine import Pin, ADC
from easyIO import *
import wifiCfg
from m5mqtt import M5mqtt

analog_pin = Pin(32, Pin.IN) # configure input pin on pin 33
adc = ADC(analog_pin) # create analog input
adc.atten(ADC.ATTN_11DB) # enable full-range on ADC pin

# M5Stack Atom Matrix : APIKEY : B3C8AA16

wifiCfg.doConnect(
    'ACCD', # WIFI name
    'tink1930' #WIFI password
);
mqtt_feed = M5mqtt(
    'testclient', # name the device whatever you want
    'io.adafruit.com', # url
    1883, # port
    'theblukoi', # username
    'aio_kpwm55RLdTB1wh14xjtJxQwqu3oF', # key
    300 # timeout
);

mqtt_feed.start();

while True:
    analog_val = adc.read(); #read analog value (0-4095 range)
    print(analog_val);
    mqtt_feed.publish(
        'theblukoi/feeds/test', # path
        str(analog_val) # turn variable into a string to publish
    );
    sleep(3);