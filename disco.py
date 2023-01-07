import machine
from machine import Pin
import utime
from neopixel import NeoPixel
import math
import random

pixelpin = 16
leds = 64

red = 4
blue = 0
green = 1

speed = 50

np = NeoPixel(Pin(pixelpin, Pin.OUT), leds)


while True:
    for i in range(leds):
        #np[i] = (red*(i+1),green*(i+1),blue*(i+1))
        np[i] =(random.randint(0,100),random.randint(0,100),random.randint(0,100) )
    np.write()
    utime.sleep(1)
