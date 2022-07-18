import time
from gpiozero import DistanceSensor

# Define GPIO pins to use on the Pi
pintrigger = 17
pinecho = 18
sensor = DistanceSensor(echo=pinecho, trigger=pintrigger)

# Check the distance every half a second
while True:
    print("Distance: %.1f cm" % (sensor.distance * 100))
    time.sleep(0.5)