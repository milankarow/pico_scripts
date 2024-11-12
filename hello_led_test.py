from machine import Pin
from time import sleep

pin = 25
led = Pin(pin,Pin.OUT)


while True:
    led.toggle()
    sleep(1)