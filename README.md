# Wright_2023_IXD256

## Assignment 1

**The prompt:**
- Create a "button" or complete a circuit in a way which did not resemble a typical "push button" that you might find on an appliance.

**The idea:**
I didn't necessarily have a purpose in mind, but I wanted to complete a circuit using coins.

[This is the original sketch I drew to prep for making the actual circuit using some copper tape and wiring.](/../main/Week03/Week02_Concept.jpg)

While making the circuit I decided to change the idea to have a red LED to show when the circuit is incomplete and a second, green, LED to show when the circuit is complete.

**Final, physical prototype:**
- [A schematic for the final circuit.](/../main/Week03/QuarterCircuit_schem.jpg)
- [The circuitry from the Atom Matrix to the breadboard.](/../main/Week03/IMG_1936.JPG)
- [The completed prototype with the red LED on.](/../main/Week03/IMG_1937.JPG)
- [The completed prototype with 4 quarters completing the circuit.](/../main/Week03/IMG_1938.JPG)
- Click through for [a short video clip](https://github.com/blukoi/Wright_2023_IXD256/blob/main/Week03/IMG_1939.mov) showing the physical model working.

---

## Assignment 2

**The prompt:**
- Create a prototype using some form of analog to digital input, such as a potentiometer, light sensor, motion sensor, pressure sensor, etc.
- The final prototype must go beyond simple on/off states.

**The idea:**
The idea that I came up with was for an ambient lighting desk lamp with a button to progress through color modes, a potentiometer to control brightness, and a time-of-flight sensor to adjust brightness when you walk away from the computer. To do this, I knew that I would need to laser cut some MDF (.25 inch thick wood, similar to a plywood) for the overall form/body of the lamp. The lamp would have to house the neopixel strip which, at 30 LEDs in length, measures roughly 20 inches long with some wiring at the ends as well as the button, the time of flight sensor, the potentiometer, as well as all the wiring running through the body to an external breadboard and M5stack Atom Matrix chip housing.

[This is the original sketch I drew to prep for the laser cutting and figuring out size and amount of wiring.](/../main/Project2/WrightMax_Week4Concept1.jpg)

The original idea also included 4x LEDs (1x red, 1x green, 1x blue, and 1x white) as indicators of which color mode is active but after turning on the lamp the first time it became clear that the neopixels were bright enough (even at the lowest brightness setting allowed in the code) that the indicator LEDs were not necessary. This ended up being beneficial, however, as the Atom Matrix board has a somewhat limited number of pins and with the other hardware there weren't enough pins for all 4 of the LEDs anyway.

**Final, physical prototype:**
- [A schematic for the final circuit.](/../main/Project2/LampSchematic_schematic.png)
- [A visual schematic for the final circuit.](/../main/Project2/LampSchematic_breadboard.png)
- Click through for a [short video clip](https://github.com/blukoi/Wright_2023_IXD256/blob/main/Project2/video_0_abdb23ff86a8461cb4ceb66c09ab165b.MP4) of the first test of the lamp turning on.
- [Final wiring, including disconnected LED wires and a test button on the breadboard.](/../main/Project2/IMG_2025.JPG)
- Click through for a [short video clip](https://github.com/blukoi/Wright_2023_IXD256/blob/main/Project2/IMG_2017%20copy%202.mov) of the physical prototype working.

---

**Using the M5Stack Core2:**

With extension modules added, the core2 should not power on unless connected to power, although it will utilize the battery to stay on once it’s been turned on. (Without extension modules, you may not have these problems.)

1. To begin: Have the device powered off and unlisted in VSCode's m5stack extension (If listed, close VSCode)
2. Connect the Core2 with a USB-C cable
3. When the Core2 is connected it should power on (If not, power it on)
4. Check connected devices (in terminal, vscode, etc.) to make sure its showing up
5. Open VSCode; click the “Add M5Stack” button at the bottom of the window; Select the Core2 (should read as “/dev/tty.wchusbserial############”)
6. With the device added, open the “M5STACK DEVICE” workspace
7. Select the “main.py” file to begin adding/editing code
8. To run the file, press the filled-in arrow in the top-right of the VSCode window
9. There’s no available terminal; the simplest way to test new code is to change the color of the screen
10. You will have to reset the device every time you want to run new code; to reset device, press the reset button while it’s still plugged in; the device and python file should remain open and available in VSCode but to be safe, copy code to a local file for major changes
11. If the device is unplugged you will need to restart from step number 1 to begin editing and testing new code; in this case, any unsaved changes to code will not be saved

---

# Final Project

**Introduction**
The idea that I had was an auxiliary computer device that would implement a full-color display with either a numpad or macropad. You can see below that both ideas involve a keypad and a screen.

The leftmost idea would be a macropad connected to an esp32 which would have a 4-line display along with 3 rotary encoders. Macropads are keypads which are meant to be customized, allowing the user to map a key command or macro (such as ctrl+c, volume up, etc.) to one of the keys. Of the small rotary encoders, the leftmost would allow the user to "scroll" through a list of different macro sets (one set for macros when working in Photoshop, another set for macros when video editing, etc.) while the rightmost would allow the user to scroll between the rows or columns as a way to check which keys were mapped to what commands. The large rotary encoder would be mappable.

The rightmost idea would be a preexisting numpad that would be connected to an esp32 which would also have a display, potentiometer, and time-of-flight sensor. The esp32 would be connected to Bungie's API for the game Destiny 2 (a game which I play quite a bit of) as a way to utilize the display to show in-game information, such as character or inventory information. The potentiometer would allow the user to "scroll" between different screen states while the TOF sensor would allow the user to interact with the information on screen, such as by sending the information currently displayed as a notification.

I decided to pursue the numpad idea as there are macropads with similar features that already exist, while the idea of connecting a numpad to a display screen was more novel and would give me more work to actually accomplish.

![Two concept sketches for final project.](../main/Final/Final_Concepts.png)

## Implementation

**Hardware**
* *M5Stack Core2*: Initially I had planned to use a relatively large ~4-inch display connected to the m5stack Atom Matrix board I already had. This proved somewhat difficult to find so after a week I chose to use the m5stack's Core2 device, which is a pre-made device housing an esp32 connected to a 320x240-pixel, full-color display, along with a battery, variety of sensors, grove ports, on/off button, reset button, usb-c port, SD card slot, as well as the ability to add modules.
* *M5Stack USB Module*: This module attachs to the Core2 and adds several inputs, inputs, and a USB-B port, specifically built as a way to add USB host functionality to the Core2. This ended up being impossible for my setup; m5stack has a program which can be used to install USB host for specific devices (keyboards, led strips, etc.) to the esp32 on your Core2, but the program itself only runs on Windows, which I don't have. This forced me to scale back the numpad from the working prototype; the numpad can still be connected to the computer but can't be used for interactions on the Core2.
* *M5Stack Extension Port Module*: The Core2 only has one grove port natively, so in order to attach an additional sensor this extension port is necessary, which adds four more grove ports.
* *M5Stack Time of Flight Sensor*: This TOF sensor would be used for simple interactions. The idea was that be holding your hand over the sensor you could send yourself reminders in the form of a notification.
* *M5Stack Angle Sensor*: This angle sensor, as a potentiometer, would allow for simple state switches without having to rely on buttons.
* *Numpad*: The numpad was originally intended to serve both as a workable numpad for the connected computer as well as an input for the Core2 device. Since the USB Host doesn't work, the keypad isn't wired/connected to the Core2 at all and instead will have to simply be connected to the computer, meaning that it will work as a numpad for the computer but not as an input for the Core2 prototype.

![Fritzing diagram next to wiring schematic.](../main/Final/Final_Hardware.png)

**Firmware**

[Here is the complete, working code](https://github.com/blukoi/Wright_2023_IXD256/blob/main/Final/NumpadAux.py) which will work without changes and [here's a working file](https://github.com/blukoi/Wright_2023_IXD256/blob/main/Final/NumpadAux_Testing.py) which I was using to test improvements, make changes, and add functionality.

``` Python
timelabel = M5Label('', x=40, y=70, color=0x000000, font=FONT_MONT_48, parent=None)
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
```

The way that M5Stack's library for their propietary displays works, text labels need to be setup in the headers similar to a variable. It's possible to set them up exactly like a variable, e.g. `timelabel = None` and then turn them into a text label when the loop starts, but M5Stack has another function, `set_text` which allows existing text labels to simply change the text. To make use of their library, all existing text labels are setup in the headers with a blank string. Then, depending on the screen state the text is changed to the necessary variables while any unnecessary text labels are changed to a blank string.

``` Python
angle = unit.get(unit.ANGLE, (35,34))
x = angle.read()
x_adj = map_value(x, in_min = 0, in_max = 1024, out_min = 1, out_max = 4)
```

The potentiometer needs the minimum and maximum values changed (using a `map_value` function) to reflect the possible screen states. Because I want 4 different screen states the maximum is changed to 4.

``` Python
if x_adj == 1:
    screenmode = 'CLOCK'
if screenmode == 'CLOCK':
    # screen.clean_screen()
    screen.set_screen_bg_color(0xFFFFFF)
    ...

    # Don't need these variables for this screen
    datelabel.set_text('')
    ...

    # Fill out this screen
    time = urequests.get(url='https://timeapi.io/api/Time/current/zone?timeZone=America/Los_Angeles')
    timedata = time.json()
    hour = timedata['hour']
    minute = timedata['minute']
    timelabel.set_text(str(hour) + ':' + str(minute))
    wait(1)
```

Here you can see that the potentiometer value sets a screen state, and then whenever the screen state is set to `"CLOCK"` (among other things) it clears unnecessary text labels such as `datelabel` by setting them to a blank string, then the code makes an API get request to the necessary API, in this case a time API with a specification for the necessary time zone. The retrieved JSON file is parsed and two variables `hour` and `minute` are set from the parsed JSON file, and the necessary label `timelabel` is populated with these variables, resulting in a display of the current time as a `HH:MM` string.

There are 4 different screen states, so there are 4 different sets of variables with accompanying API requests.

``` Python
hover = unit.get(unit.TOF, (19,27))
y = hover.distance
y_adj = map_value(y, in_min = 0, in_max = 8191, out_min = 1, out_max = 10)
```

Here is where some of the problems start: the TOF sensor. The Core2 has no problems reading the values from the TOF sensor itself; this code is all standard to start reading from the TOF sensor. Let's break it down:

``` Python
if y_adj <= 4 and ticks_ms() > (timer + 5000):
```

So, if the time of flight sensor reads below a certain value and hasn't been triggered in the past 5 seconds, then...

``` Python
    notifforecast = urequests.get(url='https://api.weatherapi.com/v1/forecast.json?key=f6fb81c6e7e5488081c173341231404&q=Los_Angeles&days=2&aqi=no&alerts=yes')
    forecastdata = notifforecast.json()
```

...an API get request will be made to a weather API, with the resulting JSON file parsed into a readable list. Then...

``` Python
    selected = forecastdata['location']['localtime']
    selectedhour = ((int(selected[11:12]) + y_adj) + 1)
    if selectedhour >= 24:
        selectedday = 0
    elif selectedhour < 24:
        selectedday = 1
```

As part of the weather API, the JSON file also includes the current local time, so the local time is used to do some simple math to figure out which part of the JSON file to read. The JSON file is a weather forecast which includes 48 objects separated into separate lists, so we need to pick the right object.

``` Python
    forecasttemp = str(forecastdata['forecast']['forecastday'][selectedday]['hour'][selectedhour]['temp_f']) + "°"
    forecastfeelslike = str(forecastdata['forecast']['forecastday'][selectedday]['hour'][selectedhour]['feelslike_f']) + "°"
    forecastcond = forecastdata['forecast']['forecastday'][selectedday]['hour'][selectedhour]['condition']['text']
```

After getting the necessary object, it's parsed into a series of strings, then...

``` Python
    notif = urequests.post(url='http://maker.ifttt.com/trigger/sensor_triggered/with/key/diWDBFMm06kX77GMorkg7g',json={'Hours from now' : y_adj, 'Temp' : forecasttemp, 'Will Feel Like' : forecastfeelslike, 'Weather' : forecastcond}, headers={'Content-Type':'application/json'})
    timer = ticks_ms()
```

...an API post request is pushed to IFTTT's Maker Service which includes a JSON packet with 3 variables represented as strings. IFTTT is then meant to take this post request and send a notification.

I never managed to get this to work. There's something messed up in the way that I've written my code so that there are too many API requests happening in such a way that the board can't handle it when the code for the TOF sensor is running. Since the code for the screen states is happening actively but the TOF sensor function is running in the background, it means that the program could end up trying to make too many different API requests at once, which results in an error and the post request never gets made.

**Integrations**

* [This is the time API](https://timeapi.io/) that I used and [you can see the documentation here](https://timeapi.io/swagger/index.html)
* [This is the weather API](https://www.weatherapi.com/) that I used and [you can see the documentation here](https://www.weatherapi.com/docs/); you have to make an account to see the retrievable JSON files

![Screenshot of IFTTT applet structure](../main/Final/ifttt_screen.png)

I also incorporated an IFTTT applet as a way to get a notification from the TOF sensor (which I never got working). It makes use of their Maker service's webhooks service to send a JSON object as part of the API post request URL.

**Enclosure/Mechanical Design**

![Wireframes for laser cuts to make a box](../main/Final/Final_Box.png)

At the same time as I took this class I also took a class on Rapid Prototyping, which involves using SolidWorks to physically produce objects from laser cutting and 3D printing. Because of that, and because the physyical prototype I would need is fairly simple, I was easily able to create an Adobe Illustrator file consisting of the simple shapes I would need to laser cut.

I took this file and laser cut out of 1/8-inch MDF, then it was a simple process to glue these pieces together. I had thought about 3D printing this as well but the cost would've been over $40 whereas it was under $2 for 2 ft² of 1/8-inch MDF plus an additional $0.45 of laser cutting.

![Completed prototype, straight on](../main/Final/Box1.jpg)
![Completed prototype, side view](../main/Final/Box2.JPG)
![Completed prototype, close up](../main/Final/Box3.JPG)

You can find the Adobe Illustrator file [here](https://github.com/blukoi/Wright_2023_IXD256/blob/main/Final/Box.ai). I made one small error in my measurements before laser cutting, where the interior angled supports to hold the numpad PCB and the Core2 up to their respective openings were cut without accounting for the 1/8-inch thick walls at the top and bottom, but that's since been fixed. This file also includes extra cuts which are meant to be used to ensure that, while gluing the walls to the floor, they're at a flush 90°.

## Project Outcome

The final prototype has the Core2 device connected to the TOF sensor, located above the screen, and the potentiometer, located below the screen. All 3 are to the left of the numpad, but the numpad is connected to the computer, not the Core2. All 4 of these (Core2, TOF sensor, potentiometer, and numpad) are housed in an MDF enclosure, with the face at a slight angle.

The numpad couldn't be connected to the Core2 because I couldn't get USB host working on my board. Additionally, the code for the TOF sensor needs to be commented out (hidden) while the prototype is running; if the code for the TOF sensor is running then, when it triggers and runs, there are too many concurrent API calls and the Core2 crashes.

With that in mind, the 4 screens displaying the current time, date, weather, and the day's forecast are all working as intended. There's some slight lag between screens as a new API call has to be made to populate the necessary variables (lag is most noticeable when switching to the day's forecast, since the returned JSON file is quite a big larger than any other returned JSON file for the other screens). However, with wait statements preventing too many API calls, the screens will update, as far as the user is concerned, in real time.

[In this video you can see the display changing between screen modes](../main/Final/Final_Video.mov) and in the fourth screen you can see the increased lag between changing the screen mode and populating the API information.

![Photo of final prototype from 1/4 angle, showing clock](../main/Final/Box_Final1.JPG)
![Photo of final prototype from 3/4 angle, showing date](../main/Final/Box_Final2.JPG)
![Photo of final prototype from straight on, showing current weather](../main/Final/Box_Final3.JPG)
![Close up photo of final prototype, showing weather forecast](../main/Final/Box_Final4.JPG)

## Conclusion

This entire project has been a huge learning opportunity and there were multiple instances when I had to scale back from what I had hoped to accomplish.

The original concept, to connect to Bungie's Destiny 2 API and use the potentiometer, TOF sensor, and numpad to interact is very far from where I ended up. My first "mistake" was in choosing the Core2 board, which was very finnicky and had a learning curve in and of itself because it connected and worked slightly differently than the Atom Matrix, which we had been using previously. The board itself had some minor issues as well, like not being able to connect to my home wi-fi but only connecting to my phone's hot spot, which made testing code a slow, cumbersome process. The Core2 also had issues with USB host, which meant I couldn't use the numpad for prototype interactions. Additionally, because of how complex the Destiny 2 API is, I had to pivot to a simpler API, that being the Time and the Weather APIs.

However, this has been a very insightful process. I'm quite interested in exploring Raspberry Pi in the future, as I think that it offers many advantages over the system that I currently have. There's certainly a lot of lessons I can take from my code, as well. There are things about getting/posting API requests which I'm certain are going to be useful in the future. Mostly, though, I'm glad that despite the issues I was able to build some level of a working prototype which connected to an API to display different amounts of information depending on different states.
