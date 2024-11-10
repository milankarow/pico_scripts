from machine import Pin
from neopixel import NeoPixel
import time

pin = Pin(20, Pin.OUT)
anzahl_leds = 16
ring = NeoPixel(pin,anzahl_leds)
ring.fill((50,50,10))
ring.write()
time.sleep(1)


def rainbow(ring, anzahl_leds):
    for i in range(0,anzahl_leds):
        ring[i] = ((i*16,124-i*8,0))
        #ring[i] = ((255-i*16,0,i*8))
        ring.write()
        
        
rainbow(ring, anzahl_leds)