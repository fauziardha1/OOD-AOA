from object import Object, Fitness
from numpy import random
import math

def AOA(numOfObj,lowerBound,upperBound,maximumIteration,C3,C4, mainFunction,dim,positionLimit,limitFunction,fitness):
    C1 = 2 # C1 is constanst and equals to 2
    C2 = 6 # C1 is constanst and equals to 6

    # 1 : initialieze objects population using (4),(5), and (6)
    population = generatePopulation(numOfObj,lowerBound,upperBound,mainFunction,dim,positionLimit,limitFunction)    
    
    # 1.2 get object with miminum scores atributes and set it as bestObject
    bestObject = ''
    if fitness == Fitness.maximum :
        bestObject = getBestObjectByMaxScore(population)
    else :
        bestObject = getBestObjectByMinScore(population)

    # 1.3 update every object in maximumIteration times
    iteration = 1
    while iteration <= maximumIteration:
        
        for obj in population:
            # 2 : update density and volume using (7)
            obj.density = obj.density + random.rand() * (bestObject.density - obj.density)
            obj.volume = obj.volume + random.rand() * (bestObject.volume - obj.volume)

            # 3 : Transfer operator and density factor using (8) and (9)
            TF = math.exp((iteration - maximumIteration)/maximumIteration)
            denDecFactor = math.exp((maximumIteration-iteration)/maximumIteration) - (iteration/maximumIteration)

            
            randomObject = population[int(random.rand()*len(population))]
            minAcceleration, maxAcceleration = getMinMaxAcceleration(population)
            if TF <= 0.5 :
                # 4.1 : Exploration phase (collision occure) using (10)
                obj.acceleration = (randomObject.density + randomObject.volume * randomObject.acceleration)/(obj.density * obj.volume)

                #  4.3 : Normalize acceleration using (12)  ### TODO: not test yet
                # u and l are range of normalization and set to 0.9 and 0.1 respectively
                u = 0.9
                l = 0.1
                accNorm = u * (obj.acceleration - minAcceleration) / (maxAcceleration - minAcceleration) +l

                # 5 : update position using (13) # TODO : not test yet
                if dim > 0 :
                    for count in range(dim):
                        obj.position[count] = obj.position[count] + C1 * random.rand() * accNorm * denDecFactor * abs(randomObject.position[count] - obj.position[count])
                else:
                    obj.position = obj.position + C1 * random.rand() * accNorm * denDecFactor * (randomObject.position - obj.position)
            else : 
                # Exploitation Phase # TODO: not test yet
                # 4.2 : Exploitation Phase ( no collision between objects) using (11)
                obj.acceleration = (bestObject.density + bestObject.volume * bestObject.acceleration)/(obj.density + obj.volume)

                #  4.3 : Normalize acceleration using (12)  ### TODO: not test yet
                # u and l are range of normalization and set to 0.9 and 0.1 respectively
                u = 0.9
                l = 0.1 
                accNorm = u * (obj.acceleration - minAcceleration) / (maxAcceleration - minAcceleration) +l

                # 5 : Update ddiraction flag F using(15) # TODO : not test yet
                T = C3 * TF 
                P = 2 * random.rand() - C4

                F = 1 if P <= 0.5  else -1

                # 5 : Update position using (14)
                if dim >0 :
                    for count in range(dim):
                        bestPosition = bestObject.position[count]
                        objPosition = obj.position[count]
                        obj.position[count] = bestPosition + F * C2 * random.rand() * accNorm * denDecFactor * (T * bestPosition - objPosition)
                else : 
                    obj.position = bestObject.position + F * C2 * random.rand() * accNorm * denDecFactor * (T * bestObject.position - obj.position)

            # end of if


            # update object score
            # obj.setScore(mainFunction(obj.position)) # it can be run , but not give an impact for all

        # end of for

        # check position and make sure position in range 
        # and update score of each object
        # printAllPopulation(population,"before Check Position")
        population = checkPosition(dim,population,lowerBound,upperBound,mainFunction,positionLimit)
        # printAllPopulation(population,"after Check Position")

        # Evaluate each object and select the one with the best fitness value
        if fitness == Fitness.maximum :
            bestObject = getBestObjectByMaxScore(population)
        else :
            bestObject = getBestObjectByMinScore(population)


        iteration  = iteration + 1
    # end of while
    # exit()
    #  return object with the best fitness value
    return bestObject, population

# end of procedure AOA





def generatePopulation(numOfObj,lowerBound,upperBound,mainFunction,dim,positionLimit,limitFunction):
    population = []
    for i in range(numOfObj):
        objPosition = []
        if dim >0 :
            isPositionValidate = False

            while not isPositionValidate :
                objPosition = []
                for count in range(dim):
                    objPosition.append(positionLimit[count].lowerBound + random.rand() * (positionLimit[count].upperBound - positionLimit[count].lowerBound))
                isPositionValidate = True if limitFunction == None else limitFunction(objPosition)

        # TODO : What if position is not an array

        # objPosition = lowerBound + random.rand() * (upperBound - lowerBound)
        objAcceleration = lowerBound + random.rand() * (upperBound - lowerBound)
        anObject = Object(objPosition, objAcceleration)
        anObject.setScore(mainFunction(anObject.position))
        population.append(anObject)
    return population


def getBestObjectByMaxScore(population): 
    minPosition = minAcceleration = minVolume = -math.inf
    minDensity = minScore = -math.inf
    
    for anObject in population:
        if anObject.score > minScore:
            minPosition = anObject.position
            minAcceleration = anObject.acceleration
            minVolume = anObject.volume
            minDensity = anObject.density
            minScore = anObject.score
        
    bestOne = Object(minPosition,minAcceleration)
    bestOne.setDensity(minDensity)
    bestOne.setVolume(minVolume)
    bestOne.setScore(minScore)
    return bestOne

def getBestObjectByMinScore(population): 
    minPosition = minAcceleration = minVolume = math.inf
    minDensity = minScore = math.inf
    
    for anObject in population:
        if anObject.score < minScore:
            minPosition = anObject.position
            minAcceleration = anObject.acceleration
            minVolume = anObject.volume
            minDensity = anObject.density
            minScore = anObject.score
        
    bestOne = Object(minPosition,minAcceleration)
    bestOne.setDensity(minDensity)
    bestOne.setVolume(minVolume)
    bestOne.setScore(minScore)
    return bestOne


def getMinMaxAcceleration(population):
    minAcceleration = 9999
    maxAcceleration = -9999

    for obj in population:
        minAcceleration = obj.acceleration if obj.acceleration < minAcceleration else minAcceleration
        maxAcceleration = obj.acceleration if obj.acceleration > maxAcceleration else maxAcceleration

    # TODO : bagaimana cara menghindari pembagian dengan nol
    while minAcceleration == maxAcceleration :
        tempAcc = random.rand()
        if tempAcc > minAcceleration:
            maxAcceleration = tempAcc
        else :
            minAcceleration = tempAcc

    return minAcceleration, maxAcceleration

def checkPosition(dim,population,lowerBound,upperBound,mainFunction,positionLimit):
    updatePopulation = []
    for obj in population :
        for count in range(dim):
            obj.position[count] = positionLimit[count].lowerBound if obj.position[count] < positionLimit[count].lowerBound else obj.position[count]
            obj.position[count] = positionLimit[count].upperBound if obj.position[count] > positionLimit[count].upperBound else obj.position[count]
        
        # TODO : make condition for obj that only has one position alias position is not array   
        obj.setScore(mainFunction(obj.position))
        updatePopulation.append(obj)

    return updatePopulation

def printAllPopulation(population,message):
    print(message)
    count = 1
    for obj in population:
        print (f"objek ke-{count} : {obj.position}")
    print("\n")