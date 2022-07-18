import time
from gpiozero import CamJamKitRobot

robot = CamJamKitRobot()

# Turn the motors on
robot.forward()

# Wait for 1 seconds
time.sleep(1)

# Turn the motors off
robot.stop()