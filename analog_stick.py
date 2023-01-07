import machine
from machine import Pin
import math



class AnalogStick(object):
    def __init__(self, xpin, ypin):
        self.xpin = xpin
        self.ypin = ypin
        
    def getAngle(self):
        xcoord = self.xpin.read_u16()-32600
        ycoord = self.ypin.read_u16()-33200
        angle = math.atan2(xcoord,ycoord) + math.pi
        return angle
    
    def getCoords(self):
        xcoord = round((self.xpin.read_u16()-32600)/16000, 2)
        ycoord = round((self.ypin.read_u16()-33200)/16000, 2)
        return xcoord, ycoord
