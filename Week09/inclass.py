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

button_pin = Pin(39, Pin.IN) # configure input on pin G39 (Matrix display button)

# M5Stack Atom Matrix : APIKEY : B3C8AA16

wifiCfg.doConnect(
    'ACCD', # WIFI name
    'tink1930' #WIFI password
);

mqtt_feed = M5mqtt(
    client_id = 'testclient', # name the device whatever you want
    server = 'io.adafruit.com', # url
    port = 1883, # port
    user = 'theblukoi', # username
    password = 'aio_kpwm55RLdTB1wh14xjtJxQwqu3oF', # key
    keepalive = 3000 # timeout
);

def feedcallback(topic_data):
    print('received... ' + topic_data)

mqtt_feed.subscribe('theblukoi/feeds/togglefeed', feedcallback);
mqtt_feed.start();

while True:
    print('Working');
    analog_val = adc.read(); #read analog value (0-4095 range)
    print(analog_val);
    '''mqtt_feed.publish(
        'theblukoi/feeds/test', # path
        str(analog_val) # turn variable into a string to publish
    );'''
    if(button_pin.value() == 0):    # if input pin is low
        print('button pressed');
        mqtt_feed.publish(
            'theblukoi/feeds/test', # path
            str(analog_val) # turn variable into a string to publish
        );
        sleep(3);
    sleep(.5);