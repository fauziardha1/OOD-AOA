import math
from object import Fitness, Limit
import numpy as np

def mainFunction(X): 
    arr = []
    for x in X:
        temp =x**2 
        ntemp = 10 - (10 * math.cos(2*np.pi*x))
        arr.append(temp + ntemp) 
    return sum(arr) 


limitInputs = []
dimention = 10
fitness = Fitness.minimum
limitFunction = None
for count in range(dimention):
    limitInputs.append(Limit(-5.12,5.12))
