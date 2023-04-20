from time import *
from machine import *
from m5stack import *
import unit
from m5stack_ui import *
from uiflow import *
import urequests
import wifiCfg
import sys
import json
from m5mqtt import M5mqtt  # M5Stack MQTT library

import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

# SETUP
screen = M5Screen()
screen.clean_screen()
screen.set_screen_bg_color(0x000)
screenmode = None
timer = ticks_ms()

# CONNECT TO WIFI
# change arguments below to connect to the WiFi network, such as 'ACCD':
wifiCfg.doConnect('Maximus Prime', 'maxisthebest')
# check WiFi connection status:
if wifiCfg.wlan_sta.isconnected():
    screen.set_screen_bg_color(0x00FF00)

# create the MQTT feed by inserting your Adafruit IO username and key:
mqtt_feed = M5mqtt(
    client_id = 'testclient',  # any name for your device (MQTT client)
    server = 'io.adafruit.com',  # MQTT broker address
    port = 1883,  # port to use for the connection
    user = 'theblukoi',  # your Adafruit IO username 
    password = 'aio_kpwm55RLdTB1wh14xjtJxQwqu3oF',  # your Adafruit IO key (check yellow key icon)
    keepalive = 300  # keep alive timeout  
)
mqtt_feed.start()

# BACKGROUNDS
line0 = M5Line(x1=0, y1=0, x2=0, y2=0, color=0xd55b5b, width=0, parent=None)
line1 = M5Line(x1=0, y1=0, x2=0, y2=0, color=0x639d67, width=0, parent=None)
line2 = M5Line(x1=0, y1=0, x2=0, y2=0, color=0xf9ff64, width=0, parent=None)
line3 = M5Line(x1=0, y1=0, x2=0, y2=0, color=0x3fbfed, width=0, parent=None)

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

# WORKING VARIABLES
time = None
timedata = None
hour = None
minute = None
day = None
month = None
dayofweek = None
weather = None
weatherdata = None
weathernow = None
weathercondition = None
lowdeg = None
highdeg = None
weathertoday = None
timelabel = M5Label('', x=40, y=70, color=0x000000, font=FONT_MONT_48, parent=None)
# M5Textarea(text='', x=0, y=0, w=None, h=None)
# timelabel = M5Textarea()
selected = None
selectedhour = None
selectedday = None
forecasttemp = None
forecastfeelslike = None
forecastcond = None

# timelabel = M5Label('', x=40, y=82, color=0x000000, font=FONT_MONT_48, parent=None)
daylabel = M5Label('', x=40, y=74, color=0x000000, font=FONT_MONT_22, parent=None)
datelabel = M5Label('', x=40, y=104, color=0x000000, font=FONT_MONT_48, parent=None)
currently = M5Label('', x=40, y=76, color=0x000000, font=FONT_MONT_22, parent=None)
currentdegree = M5Label('', x=40, y=110, color=0x000000, font=FONT_MONT_48, parent=None)
condition = M5Label('', x=40, y=164, color=0x000000, font=FONT_MONT_22, parent=None)
low = M5Label('', x=40, y=100, color=0x000000, font=FONT_MONT_22, parent=None)
high = M5Label('', x=160, y=100, color=0x000000, font=FONT_MONT_22, parent=None)
lowdegree = M5Label('', x=40, y=130, color=0x000000, font=FONT_MONT_48, parent=None)
highdegree = M5Label('', x=160, y=130, color=0x000000, font=FONT_MONT_48, parent=None)
forecast = M5Label('', x=40, y=184, color=0x000000, font=FONT_MONT_22, parent=None)

while True:
    screen.set_screen_bg_color(0xFFFFFF)
    x = angle.read()
    x_adj = map_value(x, in_min = 0, in_max = 1024, out_min = 1, out_max = 4)
    y = hover.distance
    y_adj = map_value(y, in_min = 0, in_max = 8191, out_min = 1, out_max = 10)
    if y_adj <= 4 and ticks_ms() > (timer + 5000):
        weather = urequests.get(url='https://api.weatherapi.com/v1/forecast.json?key=f6fb81c6e7e5488081c173341231404&q=Los_Angeles&days=2&aqi=no&alerts=yes')
        weatherdata = weather.json()
        selected = weatherdata['location']['localtime']
        selectedhour = ((int(selected[11:12]) + y_adj) + 1)
        if selectedhour >= 24:
            selectedday = 0
        elif selectedhour < 24:
            selectedday = 1
        forecasttemp = str(weatherdata['forecast']['forecastday'][selectedday]['hour'][selectedhour]['temp_f']) + "°"
        forecastfeelslike = str(weatherdata['forecast']['forecastday'][selectedday]['hour'][selectedhour]['feelslike_f']) + "°"
        forecastcond = weatherdata['forecast']['forecastday'][selectedday]['hour'][selectedhour]['condition']['text']
        if y_adj == 1:
            mqtt_feed.publish(
                'theblukoi/feeds/test', # path
                "In " + str(y_adj) + " hour, the temperature will be " + forecasttemp + ", will feel like " + forecastfeelslike + ", and it will be " + forecastcond + "."
            )
        elif y_adj > 1:
            mqtt_feed.publish(
                'theblukoi/feeds/test', # path
                "In " + str(y_adj) + " hours, the temperature will be " + forecasttemp + ", will feel like " + forecastfeelslike + ", and it will be " + forecastcond + "."
            )
        timer = ticks_ms()
    if x_adj == 1:
        screenmode = 'CLOCK'
    if x_adj == 2:
        screenmode = 'DATE'
    if x_adj == 3:
        screenmode = 'WEATHER'
    if x_adj == 4:
        screenmode = 'FORECAST'
    '''if screenmode == "TEST":
        try:
            screen.clean_screen()
            screen.set_screen_bg_color(0xFF0000)
            time = urequests.get(url = "http://www.worldtimeapi.org/api/timezone/America/Los_Angeles")
            req_data = time.json()
            datetime = req_data['datetime']
            label0.set_text(datetime)
            # label1.set_text('distance = ' + str(hover.distance))
            wait(1)
        except:
            screen.clean_screen()
            screen.set_screen_bg_color(0xFF00FF)
            wait(1)
        wait(1)'''
    if screenmode == 'CLOCK':
        # screen.clean_screen()
        screen.set_screen_bg_color(0xFFFFFF)
        line0 = M5Line(x1=0, y1=90, x2=20, y2=90, color=0xd55b5b, width=180, parent=None)
        line1 = M5Line(x1=0, y1=190, x2=20, y2=190, color=0x639d67, width=20, parent=None)
        line2 = M5Line(x1=0, y1=210, x2=20, y2=210, color=0xf9ff64, width=20, parent=None)
        line3 = M5Line(x1=0, y1=230, x2=20, y2=230, color=0x3fbfed, width=20, parent=None)

        # Don't need these variables for this screen
        datelabel.set_text('')
        daylabel.set_text('')
        currently.set_text('')
        currentdegree.set_text('')
        condition.set_text('')
        low.set_text('')
        high.set_text('')
        lowdegree.set_text('')
        highdegree.set_text('')
        forecast.set_text('')

        # Fill out this screen
        time = urequests.get(url='https://timeapi.io/api/Time/current/zone?timeZone=America/Los_Angeles')
        timedata = time.json()
        hour = timedata['hour']
        minute = timedata['minute']
        timelabel.set_text(str(hour) + ':' + str(minute))
        wait(1)
    if screenmode == 'DATE':
        # screen.clean_screen()
        screen.set_screen_bg_color(0xFFFFFF)
        line0 = M5Line(x1=0, y1=10, x2=20, y2=10, color=0xd55b5b, width=20, parent=None)
        line1 = M5Line(x1=0, y1=110, x2=20, y2=110, color=0x639d67, width=180, parent=None)
        line2 = M5Line(x1=0, y1=210, x2=20, y2=210, color=0xf9ff64, width=20, parent=None)
        line3 = M5Line(x1=0, y1=230, x2=20, y2=230, color=0x3fbfed, width=20, parent=None)

        # Don't need these variables for this screen
        timelabel.set_text('')
        currently.set_text('')
        currentdegree.set_text('')
        condition.set_text('')
        low.set_text('')
        high.set_text('')
        lowdegree.set_text('')
        highdegree.set_text('')
        forecast.set_text('')

        # Fill out this screen
        time = urequests.get(url='https://timeapi.io/api/Time/current/zone?timeZone=America/Los_Angeles')
        timedata = time.json()
        day = timedata['day']
        month = timedata['month']
        dayofweek = timedata['dayOfWeek']
        datelabel.set_text(str(month) + '/' + str(day))
        daylabel.set_text(str(dayofweek))
        wait(1)
    if screenmode == 'WEATHER':
        # screen.clean_screen()
        screen.set_screen_bg_color(0xFFFFFF)
        line0 = M5Line(x1=0, y1=10, x2=20, y2=10, color=0xd55b5b, width=20, parent=None)
        line1 = M5Line(x1=0, y1=30, x2=20, y2=30, color=0x639d67, width=20, parent=None)
        line2 = M5Line(x1=0, y1=130, x2=20, y2=130, color=0xf9ff64, width=180, parent=None)
        line3 = M5Line(x1=0, y1=230, x2=20, y2=230, color=0x3fbfed, width=20, parent=None)

        # Don't need these variables for this screen
        datelabel.set_text('')
        daylabel.set_text('')
        timelabel.set_text('')
        low.set_text('')
        high.set_text('')
        lowdegree.set_text('')
        highdegree.set_text('')
        forecast.set_text('')

        # Fill out this screen
        weather = urequests.get(url='https://api.weatherapi.com/v1/current.json?key=f6fb81c6e7e5488081c173341231404&q=Los_Angeles&aqi=no')
        weatherdata = weather.json()
        weathernow = weatherdata['current']['temp_f']
        weathercondition = weatherdata['current']['condition']['text']
        currently.set_text('Currently')
        currentdegree.set_text(str(weathernow) + '°')
        condition.set_text(str(weathercondition))
        # timelabel.set_text(str(weathernow))
        wait(1)
    if screenmode == 'FORECAST':
        # screen.clean_screen()
        screen.set_screen_bg_color(0xFFFFFF)
        line0 = M5Line(x1=0, y1=10, x2=20, y2=10, color=0xd55b5b, width=20, parent=None)
        line1 = M5Line(x1=0, y1=30, x2=20, y2=30, color=0x639d67, width=20, parent=None)
        line2 = M5Line(x1=0, y1=50, x2=20, y2=50, color=0xf9ff64, width=20, parent=None)
        line3 = M5Line(x1=0, y1=150, x2=20, y2=150, color=0x3fbfed, width=180, parent=None)

        # Don't need these variables for this screen
        datelabel.set_text('')
        daylabel.set_text('')
        timelabel.set_text('')
        currently.set_text('')
        currentdegree.set_text('')
        condition.set_text('')

        # Fill out this screen
        weather = urequests.get(url='https://api.weatherapi.com/v1/forecast.json?key=f6fb81c6e7e5488081c173341231404&q=Los_Angeles&days=1&aqi=no&alerts=yes')
        weatherdata = weather.json()
        lowdeg = round(weatherdata['forecast']['forecastday'][0]['day']['mintemp_f'])
        highdeg = round(weatherdata['forecast']['forecastday'][0]['day']['maxtemp_f'])
        weathertoday = weatherdata['forecast']['forecastday'][0]['day']['condition']['text']
        low.set_text('Low')
        high.set_text('High')
        lowdegree.set_text(str(lowdeg) + "°")
        highdegree.set_text(str(highdeg) + "°")
        forecast.set_text(weathertoday)
        wait(1)