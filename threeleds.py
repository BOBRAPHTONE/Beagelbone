import Adafruit_BBIO.GPIO as GPIO
import time

GPIO.setup("P8_10",GPIO.OUT)
GPIO.setup("P8_11",GPIO.OUT)
GPIO.setup("P8_12",GPIO.OUT)

GPIO.setup("P8_13",GPIO.OUT)
GPIO.setup("P8_14",GPIO.OUT)
GPIO.setup("P8_15",GPIO.OUT)

temperature = float(input('What is the temperature? '))
    if temperature > 70:
        print('Wear shorts.')
    else:
        print('Wear long pants.')
    print('Get some exercise outside.')

while True:
        GPIO.output("P8_10",GPIO.HIGH)
        GPIO.output("P8_12",GPIO.HIGH)
        GPIO.output("P8_14",GPIO.LOW)
        time.sleep(0.5)
        GPIO.output("P8_10",GPIO.LOW)
        GPIO.output("P8_12",GPIO.LOW)
        GPIO.output("P8_14",GPIO.HIGH)
        time.sleep(0.5)

# Function definition is here
def printme( str ):
   "This prints a passed string into this function"
   print str
   return;

# Now you can call printme function
printme("Turn Left")
printme("Turn Right")
	