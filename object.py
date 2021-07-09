from numpy import random
import enum
class Object:
    def __init__(self,position,acc):
        self.position = position
        self.density = random.rand()
        self.volume = random.rand()
        self.acceleration = acc
        self.score = 0

    def setDensity(self,density):
        self.density = density

    def setVolume(self,volume):
        self.volume = volume

    def setScore(self,score):
        self.score = score


class Limit:
    def __init__(self,lowerBound,upperBound):
        self.lowerBound = lowerBound
        self.upperBound = upperBound

class Fitness(enum.Enum):
    minimum = True
    maximum = False
