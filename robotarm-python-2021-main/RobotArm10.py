from RobotArm import RobotArm

robotArm = RobotArm('exercise 10')

robotArm.speed = 2

# Jouw python instructies zet je vanaf hier:

for x in range(9,0,-2):
    robotArm.grab()
    for i in range(x):
        robotArm.moveRight()
    robotArm.drop()
    for i in range(x):
        robotArm.moveLeft()
    robotArm.moveRight()



# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()