from pygame import Color, color
from RobotArm import RobotArm

robotArm = RobotArm('exercise 12')

robotArm.speed = 2

# Jouw python instructies zet je vanaf hier:

x = 9
for i in range(9):
    robotArm.grab()
    color = robotArm.scan()
    if color == 'red':
        for i in range(x):
            robotArm.moveRight()
        robotArm.drop()
        x = x - 1
        for i in range(x):
            robotArm.moveLeft()
    else:
        robotArm.drop()
        robotArm.moveRight()
        x = x - 1



# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()