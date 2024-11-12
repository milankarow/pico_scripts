import machine
from machine import Pin, PWM
from time import sleep

#pin = Pin(16, Pin.OUT)
pwm = PWM(Pin(16))
pause = 0.05
c_tonleiter = [261,294,330,349,392,440,494,523]
#c_chord = [261,330,392]
#g_chord = [294,392,494]
#a_chord = [261,330,440]
#f_chord = [349,440,261]


for i in range(0,8):
    pwm.freq(c_tonleiter[i])
    pwm.duty_u16(32000)
    sleep(pause)    
for i in range(0,7):
    pwm.freq(c_tonleiter[6-i])
    pwm.duty_u16(32000)
    sleep(pause)
    
    
    
    
pwm.deinit()
