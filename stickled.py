from machine import Pin, ADC
from time import sleep
from neopixel import NeoPixel
import math
from random import randint
from analog_stick import AnalogStick
from led_matrix import NeoPixelMatrix



astick = AnalogStick(ADC(27), ADC(26))
pixelpin = 16
matrix = NeoPixelMatrix(Pin(pixelpin, Pin.OUT),16,16)




while True:
    x, y = astick.getCoords()
    matrix.setPixel(min(int((x+1)*8), 15),min(int((y+1)*8),15), 160*(x+1.1),1.0, 0.1)    
    print(astick.getCoords())
         



