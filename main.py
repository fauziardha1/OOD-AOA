from aoa import AOA 
import problem 

numOfObj            = 10
lowerBound          = -10
upperBound          = 10
maximumIteration    = 1000
C1 = 2
C2 = 6
C3 = 2  # coc engineering problem
C4 = 0.5 # coc engineering problem // sesuai dengan paper

# standar optimization problem for constants C3 and C4
# C3=1
# C4=2

function        = problem.mainFunction
dim             = problem.dimention
positionLimit   = problem.limitInputs
limitFunction   = problem.limitFunction
fitness         = problem.fitness

solution, population = AOA(numOfObj,lowerBound,upperBound,maximumIteration,C3,C4, function, dim,positionLimit,limitFunction,fitness)

print(f"Restrigin Solution \nBestScore: {solution.score} \n x or position: {solution.position}")
