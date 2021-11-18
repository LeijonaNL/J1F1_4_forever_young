from RobotArm import RobotArm

robotArm = RobotArm()
robotArm.randomLevel(1,7)

robotArm.speed = 2

# Jouw python instructies zet je vanaf hier:

x = 1
while robotArm.grab():
    color = robotArm.scan()
    if color == '':
    else:
        for i in range(x):
            robotArm.moveRight()
        robotArm.drop()
        for i in range(x):
            robotArm.moveLeft()
    x = x + 1




# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()