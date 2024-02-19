
import matplotlib.pyplot as plt
import numpy as np

class Robot:
    def __init__(self, xposition, yposition):
        self.xposition = xposition
        self.yposition = yposition
        self.position = [xposition, yposition]

    def changeX(self, newX):
        self.xposition = newX
        self.position =[self.xposition,self.yposition]

    def changeY(self, newY):
        self.yposition = newY
        self.position = [self.xposition,self.yposition]

    def printPosition(self):
        print("Current position is:")
        print(self.position)

    def availableMoves(self):
        if self.xposition != goal[0]:
            if noObstacle(self.xposition +1, self.yposition):
                self.changeX(self.xposition+1)
                xArray.append(self.xposition)
                yArray.append(self.yposition)
                print("Robot moves to:")
                print(self.position)
            else:
                print("There's an obstacle to the right")
        if self.yposition != goal[1]:
            if noObstacle(self.xposition, self.yposition+1):
                self.changeY(self.yposition+1)
                xArray.append(self.xposition)
                yArray.append(self.yposition)
                print("Robot moves to:")
                print(self.position)
            else:
                print("There's an obstacle above")

def noObstacle(x, y):
    for o in obstacles:
        if o == [x,y]:
            return False
    return True

#Initializing robot and variables
robot = Robot(0,0)
obstacles = [[1,1], [1,2], [2,2]]
goal = [3,3]
xArray = ([0])
yArray = ([0])

#Start of the robot's journey
print("Starting position is:")
print(robot.position)

while robot.position != goal:
    robot.availableMoves()

print("The robot has reached the goal!")

print("Arrays that show the path:")
print(xArray)
print(yArray)

plt.plot(xArray, yArray)
plt.xticks(np.arange(0, 4, step=1))
plt.yticks(np.arange(0, 4, step=1))
plt.grid(axis='both')
plt.show()



