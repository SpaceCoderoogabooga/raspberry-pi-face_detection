import RPi.GPIO as GPIO
import time
import keyboard
import random

def startup_motor():
    # Set GPIO numbering mode
    GPIO.setmode(GPIO.BOARD)

    # Set pins 11 & 12 as outputs, and define as PWM servo1 & servo2
    GPIO.setup(11,GPIO.OUT)
    servo1 = GPIO.PWM(11,50) # pin 11 for servo1
    GPIO.setup(12,GPIO.OUT)
    servo2 = GPIO.PWM(12,50) # pin 12 for servo2

    # Start PWM running on both servos, value of 0 (pulse off)
    servo1.start(0)
    servo2.start(0)

current_x_position = 0
current_y_position = 0

def change_position(x, y):
    global servo1
    global servo2
    global current_x_position
    global current_y_position

    time.sleep(0.1)
    servo1.ChangeDutyCycle(round(current_x_position, 2))
    servo2.ChangeDutyCycle(round(current_y_position, 2))


def main():
    x_position = 0
    y_position = 0
    direction = '+'
    change_position(x_position, y_position)
    while x_position <= 7:
        if direction == '+' and x_position >= 6.9:
            direction = '-'
        if direction == '-' and x_position <=0.1:
            direction = '+'
        y_position = random.randint(0, 24)
        y_position = round(y_position, 2)
        if direction == '+':
            x_position += 0.05
        else:
            x_position -= 0.05
        x_position = round(x_position, 2)
        change_position(x_position, y_position)
        print(x_position)
    change_position(2, 2)
    change_position(0, 0)
    #Clean things up at the end
    servo1.stop()
    servo2.stop()
    GPIO.cleanup()
    print ("Goodbye")

