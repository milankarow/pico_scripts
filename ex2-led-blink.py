from machine import Pin
from time import sleep

pin = 16 #25 für eingebaute LED
led = Pin(pin,Pin.OUT)


while True: #Endlosschleife
    led.toggle()
    sleep(0.2)