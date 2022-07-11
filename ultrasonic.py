import sys
import time
from machine import Pin
 
usleep = lambda x: time.sleep(x / 1000000.0)
 
_TIMEOUT1 = 1000
_TIMEOUT2 = 10000
 
class GroveUltrasonicRanger(object):
    def __init__(self, pin):
        self.pin = pin
 
    def _get_distance(self):
        self.dio = Pin(self.pin,Pin.OUT)
        self.dio.value(0)
        usleep(2)
        self.dio.value(1)
        usleep(10)
        self.dio.value(0)
 
        self.dio = Pin(self.pin, Pin.IN, Pin.PULL_DOWN)
 
        t0 = time.ticks_us()
        count = 0
        while count < _TIMEOUT1:
            if self.dio.value():
                break
            count += 1
        if count >= _TIMEOUT1:
            return None
 
        t1 = time.ticks_us()
        count = 0
        while count < _TIMEOUT2:
            if not self.dio.value():
                break
            count += 1
        if count >= _TIMEOUT2:
            return None
 
        t2 = time.ticks_us()
 
        dt = int((t1 - t0))
        if dt > 530:
            return None
 
        distance = ((t2 - t1) / 29 / 2)    # cm
 
        return distance
 
    def get_distance(self):
        while True:
            dist = self._get_distance()
            if dist:
                return dist
 
Grove = GroveUltrasonicRanger
 
def main():
    
    pin = 15
    sonar = GroveUltrasonicRanger(pin)
 
    print('Detecting distance...')
    while True:
        print('{} cm'.format(sonar.get_distance()))
        time.sleep(0.5)
 

main()
