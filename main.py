from aoa import AOA
from numpy import random
import problem

numOfObj = 30
lowerBound = -10
upperBound = 10
maximumIteration = 1000
C1 = 2
C2 = 6
C3 = 2  # coc engineering problem
C4 = 0.5 # coc engineering problem // sesuai dengan paper
function = problem.mainFunction
dim = problem.dimention
positionLimit = problem.limitInputs
limitFunction = problem.limitFunction
fitness = problem.fitness
solution, population = AOA(numOfObj,lowerBound,upperBound,maximumIteration,C3,C4, function, dim,positionLimit,limitFunction,fitness)
print(f"Solution \nBestScore: {solution.score} \nposition: {solution.position}, \nacceleration: {solution.acceleration},\ndensity: {solution.density},\nvolume: {solution.volume}")

# index = 1
# for obj in population:
#     print(f"Object ke {index}   BestScore: {obj.score}  position: {obj.position},acceleration: {obj.acceleration},density: {obj.density},volume: {obj.volume} \n")
#     index +=1

