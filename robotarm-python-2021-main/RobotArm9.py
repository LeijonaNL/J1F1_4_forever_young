from RobotArm import RobotArm

robotArm = RobotArm('exercise 9')

robotArm.speed = 2

# Jouw python instructies zet je vanaf hier:

for x in range(1,5):
    for i in range(x):
        robotArm.grab()
        for i in range(5):
            robotArm.moveRight()
        robotArm.drop()
        for i in range(5):
            robotArm.moveLeft()
    robotArm.moveRight()





# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()