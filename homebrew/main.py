#raspi lib
import RPi.GPIO as GPIO

#std lib
import threading

#user lib
import motor
import gpio
import program
import tempControl
import tempSens
import gui, gui_auto, gui_man

#global variables
isOn = False

#local variables
_isAuto = False
_loopDelayTimer = 1.0

#general GPIO Settings
GPIO.cleanup()
GPIO.setmode(GPIO.BCM)

#define methods
def _mainLoop():
    threading.Timer(_loopDelayTimer, _mainLoop).start()
    print("test1")

    if _isAuto:
        if isOn:
            program.update()
    if(isOn):
        tempControl.update(tempSens.get())
    else:
        tempControl.off()

def setMode(isAuto):
    _isAuto = isAuto
    gui.load(isAuto)


#initialisation script
_mainLoop() #start mainLoop
gui.load(False) #load manual user interface

