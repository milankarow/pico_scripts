from machine import Pin
from time import sleep
from neopixel import NeoPixel
import math
from random import randint

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
        
    return tuple(map(lambda n: int((n + m) * 255), rgb)) 

def clear():
    np.fill((0,0,0))
    np.write()
    
def getRainbow(leds,value):
    huelist = list(map(lambda z: int(z*(360/leds)),list(range(0,leds))))
    return list(map(lambda f: hsv2rgb(f, 1, value),huelist))

def fillRandomColors(leds,value):
    huelist = [randint(0,360) for i in range(0,leds)]
    return list(map(lambda f: hsv2rgb(f, 1, value),huelist))    

def singlePixel(pixel):
    np.fill((0,0,0))
    np[pixel] = (red,green,blue)
    np.write()
    
def shiftRight(leds):
    end = np[leds - 1]
    for x in range(0,leds):
        np[leds - 1 - x] = np[leds - x - 2] if x < 63 else end
    np.write()


clear()
#rblist = fillRandomColors(leds,0.01)
rblist = getRainbow(leds,0.01)
for v in range (0,leds):
    np[v] = rblist[v]
#np = getRainbow(leds)
np.write()

while True:
    shiftRight(leds)
    sleep(0.1)


#while True:
#    for i in range(0,59):
#        rgb = hsv2rgb(i*6,1,0.2)
#        rgb = tuple(map(lambda x: int(x), rgb))
#        print(i, rgb)
#        np.fill(rgb)
#        np.write()
#        sleep(0.1)


#while True:
#    if button.value() and not is_pressed:
#        print(zahl)
#        is_pressed = True
#        singlePixel(zahl)
#        zahl = zahl + 1 if zahl < 63 else 0
#    if not button.value() and is_pressed:
#        is_pressed = False
#    sleep(0.05)



