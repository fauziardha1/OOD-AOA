from numpy.core.fromnumeric import mean
from aoa import AOA  
import rastrigin_problem

numOfObj = 20
maximumIteration = 10
C1 = 2
C2 = 6
C3 = 2  # coc engineering problem
C4 = 0.5 # coc engineering problem // sesuai dengan paper


# standar optimization problem for constants C3 and C4
# C3=1
# C4=2

function        = rastrigin_problem.mainFunction
dim             = rastrigin_problem.dimention
positionLimit   = rastrigin_problem.limitInputs
limitFunction   = rastrigin_problem.limitFunction
fitness         = rastrigin_problem.fitness
lowerBound      = positionLimit[0].lowerBound
upperBound      = positionLimit[0].upperBound


solution, population = AOA(numOfObj,lowerBound,upperBound,maximumIteration,C3,C4, function, dim,positionLimit,limitFunction,fitness)

print(f"Restrigin Solution \nBestScore: {solution.score} \n x or position: {solution.position}\n")


# import math
# from numpy import random
# def rastrigin(x):
#     temp = x**2
#     nTemp = 10 - (10*math.cos(2*math.pi*x))
#     return temp + nTemp

# X = Y =  []


# for obyek in population :
#     X += obyek.position
#     for x in obyek.position:
#         Y.append(rastrigin(x))
# print(f"len Y:{len(Y)}, lenX : {len(X)}")

# # normalisasi 
# # for i in range(len(X)):
# #     X[i] = (X[i] - mean(X))/(max(X) - min(X))
# #     Y[i] = (Y[i] - mean(Y))/(max(Y) - min(Y))
# # for data in population:
# #     print(data.position)
# #     print("\n")



# import matplotlib.pyplot as plt

# # plt.scatter(X,Y)
# # plt.show()

# plt.scatter(X,Y)
# plt.plot(X,Y,"--")
# plt.show()
# plt.hist(Y)
# plt.show()