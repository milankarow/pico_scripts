from neopixel import NeoPixel

class NeoPixelMatrix(object):
    def __init__(self,pin,rows,columns):
        self.pin = pin
        self.rows = rows
        self.columns = columns
        self.leds = rows * columns
        self.np = NeoPixel(pin,rows*columns)
        
    def clear(self):
        self.np.fill((0,0,0))
        self.np.write()
        
    
    def fillColor(self,hue,saturation,brightness):
        self.np.fill(self.hsv2rgb(hue,saturation, brightness))
        self.np.write()        

    def pixelFromCoords(self,x,y):
        if y % 2 == 0:
            return (x + y *self.rows)
        else:
            return (self.columns - x - 1 + y * self.rows)

    def singlePixel(self, xpos, ypos, hue, saturation, brightness):
        self.np.fill((0,0,0))
        self.setPixel(xpos, ypos, hue, saturation, brightness)
        
    def setPixel(self, xpos, ypos, hue, saturation, brightness):
        self.np[self.pixelFromCoords(xpos,ypos)] = self.hsv2rgb(hue,saturation,brightness)
        self.np.write()


    def hsv2rgb(self,h, s, v):
        
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
            rgb = (0,0,0) #should be unreachable, only there to prevent unbound warning
            
        return tuple(map(lambda n: int((n + m) * 255), rgb)) 





