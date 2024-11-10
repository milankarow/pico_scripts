from machine import Pin, PWM, ADC
from time import sleep

#analog pin for control
pot = ADC(Pin(26))



# Set up PWM Pin for servo control
servo_pin = machine.Pin(20)
servo = PWM(servo_pin)

# Set Duty Cycle for Different Angles
max_duty = 6900
min_duty = 1700
half_duty = int((min_duty+max_duty)/2)

#Set PWM frequency
frequency = 50
servo.freq (frequency)

while True:
    pot_value = pot.read_u16() # read value, 0-65535 across voltage range 0.0v - 3.3v
    duty_value = pot_value/12.6 + min_duty
    #print(duty_value)
    servo.duty_u16(int(duty_value))
    sleep(0.05) 


'''
try:
    while True:
        #Servo at 0 degrees
        servo.duty_u16(min_duty)
        print(str(min_duty))
        sleep(1)
        #Servo at 90 degrees
        servo.duty_u16(half_duty)
        print(str(half_duty))
        sleep(1)
        #Servo at 180 degrees
        servo.duty_u16(max_duty)
        print(str(max_duty))
        sleep(1)    
      
except KeyboardInterrupt:
    print("Keyboard interrupt")
    # Turn off PWM 
    servo.deinit()
'''