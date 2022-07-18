import time
from gpiozero import LineSensor

# Set variables for the GPIO pins
pinLineFollower = 25
sensor = LineSensor(pinLineFollower)

def lineseen():
    print("Line seen")
def linenotseen():
    print("No line seen")

# Tell the program what to do with a line is (un)seen
sensor.when_line = lineseen
sensor.when_no_line = linenotseen

# Repeat the next indented block forever
while True:
    time.sleep(10)
