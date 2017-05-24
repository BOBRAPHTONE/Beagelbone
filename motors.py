import Adafruit_BBIO.PWM as PWM
servoPin="P9_14"
PWM.start(servoPin,5,50)
while(1):
        dutyCycle=input("What Duty Cycle? ")
        PWM.set_duty_cycle(servoPin,dutyCycle)