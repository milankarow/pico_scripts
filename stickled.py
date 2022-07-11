import machine
from machine import Pin
import utime
from neopixel import NeoPixel
import math

pixelpin = 28
leds = 16

red = 100
blue = 100
green = 100

speed = 50

np = NeoPixel(Pin(pixelpin, Pin.OUT), leds)

xpin = machine.ADC(27)
ypin = machine.ADC(26)

while True:
    for i in range(leds):
        np[i] = (0,0,0)
        
    xcoord = xpin.read_u16()-32600
    ycoord = ypin.read_u16()-33200
    angle = math.atan2(xcoord,ycoord) + math.pi
    active_led = int((16*angle/(2*math.pi)))
    #print(active_led)
    np[active_led] = (red,green,blue)
    np.write()
    #print(':::')
    utime.sleep(0.1)

