from RobotArm import RobotArm

robotArm = RobotArm('exercise 7')

robotArm.speed = 3

# Jouw python instructies zet je vanaf hier:

robotArm.moveRight()
for i in range(5):
    for i in range(6):
        robotArm.grab()
        robotArm.moveLeft()
        robotArm.drop()
        robotArm.moveRight()
    for i in range(2):
        robotArm.moveRight()
    




# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()