import time
from gpiozero import CamJamKitRobot

robot = CamJamKitRobot()

robot.forward(0.5)
time.sleep(1)  # Pause for 1 second

robot.backward()
time.sleep(1)

robot.left()
time.sleep(0.5)  # Pause for half a second

robot.right()
time.sleep(0.5)

robot.stop()
