from machine import Pin
from time import sleep
from neopixel import NeoPixel
import math


button = Pin(17, Pin.IN, Pin.PULL_DOWN)
is_pressed = False
zahl = 0

pixelpin = 16
leds = 64

red = 2
blue = 1
green = 1

speed = 50

np = NeoPixel(Pin(pixelpin, Pin.OUT), leds)
  
def pixelFromCoords(x,y):
    edgelength = int(math.sqrt(leds))
    x = 0 if x > (edgelength - 1) else x
    y = 0 if y > (edgelength - 1) else y
    return edgelength*y + x


def hsv2rgb(h, s, v):
    
    """HSV to RGB
    
    :param float h: 0.0 - 360.0
    :param float s: 0.0 - 1.0
    :param float v: 0.0 - 1.0
    :return: rgb 
    :rtype: list
    
    """
    
    c = v * s
    x = c * (1 - abs(((h/60.0) % 2) - 1))
    m = v - c
    
    if 0.0 <= h < 60:
        rgb = (c, x, 0)
    elif 0.0 <= h < 120:
        rgb = (x, c, 0)
    elif 0.0 <= h < 180:
        rgb = (0, c, x)
    elif 0.0 <= h < 240:
        rgb = (0, x, c)
    elif 0.0 <= h < 300:
        rgb = (x, 0, c)
    elif 0.0 <= h < 360:
        rgb = (c, 0, x)
    else:
        rgb = (0,0,0)
        
    return list(map(lambda n: (n + m) * 255, rgb)) 

def clear():
    np.fill((0,0,0))
    np.write()
    
def singlePixel(pixel):
    np.fill((0,0,0))
    np[pixel] = (red,green,blue)
    np.write()


while True:
    for i in range(0,59):
        rgb = hsv2rgb(i*6,1,0.2)
        rgb = tuple(map(lambda x: int(x), rgb))
        print(i, rgb)
        np.fill(rgb)
        np.write()
        sleep(0.1)


while True:
    if button.value() and not is_pressed:
        print(zahl)
        is_pressed = True
        singlePixel(zahl)
        zahl = zahl + 1 if zahl < 63 else 0
    if not button.value() and is_pressed:
        is_pressed = False
    sleep(0.05)


