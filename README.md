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