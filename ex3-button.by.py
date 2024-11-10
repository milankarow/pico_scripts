from machine import Pin
from time import sleep

pin = 16 #25 für eingebaute LED
button = Pin(pin,Pin.IN, Pin.PULL_DOWN)


while True: #Endlosschleife
    if button.value() == 1:
        print("ping")
        sleep(0.2)