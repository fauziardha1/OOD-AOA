import math
from object import Limit, Fitness

# Problem using appendix D

def mainFunction(inputs):
    x1 = inputs[0]
    x2 = inputs[1]
    x3 = inputs[2]
    x4 = inputs[3]
    return 0.6224*x1*x2*x3*x4 + 1.7781*x2*(x3**2) + 3.1661*(x1**2)*x4 + 19.84*(x1**2)*x3

dimention = 4
fitness = Fitness.minimum

def g1(x1,x2,x3,x4):
    statement = -x1 + 0.0193*x3 
    
    if(statement <= 0):
        return True
    return False

def g2(x1,x2,x3,x4):
    statement = -x2 + 0.00954*x3 
    if(statement <= 0):
        return True
    return False

def g3(x1,x2,x3,x4):
    statement =  -math.pi*(x3**2)*x4 - (4/3)*math.pi*(x3**3) + 1296000  
    if(statement <= 0):
        return True
    return False

def g4(x1,x2,x3,x4):
    statement = x4 - 240
    if(statement <= 0):
        return True
    return False
 


def limitFunction(inputs):
    x1 = inputs[0]
    x2 = inputs[1]
    x3 = inputs[2]
    x4 = inputs[3]
    return len(inputs) > 0 and g1(x1,x2,x3,x4) and g2(x1,x2,x3,x4) and g3(x1,x2,x3,x4) and g4(x1,x2,x3,x4)

# create input limitation as much as many inputs or dimention
limitInputs = [Limit(0,100),Limit(0,100),Limit(10,200),Limit(10,200)]