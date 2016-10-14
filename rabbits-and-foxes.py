from matplotlib import pyplot as plt
import operator

# # Implementing Kinetic Monte Carlo Simulations

R = 400
F = 200
k1 = 0.015
k2 = 0.00004
k3 = 0.0004
k4 = 0.04

days = 600

import random

class Population:
    '''
    This class represents the population that we are modeling with the rate of rabbits and foxes
    dying and the current population is stored and accessible at any point
    '''
    def __init__(self, R, F):
        self.R = R
        self.F = F

    def RabbitBorn(self):
        return k1*self.R
    
    def RabbitDies(self):
        return k2*self.R*self.F 

    def FoxBorn(self):
        return k3*self.F*self.R
    
    def FoxDies(self):
        return k4*self.F

    def rateOfExpectedEvents(self):
        return self.RabbitDies() + self.RabbitBorn() + self.FoxDies() + self.FoxBorn()

    def event(self): 
        
        totalRate = self.rateOfExpectedEvents()
        pRabbitDeath = self.RabbitDies()/totalRate
        pRabbitBirth = self.RabbitBorn()/totalRate
        pFoxDeath = self.FoxDies()/totalRate
        pFoxBirth = self.FoxBorn()/totalRate
        referenceList = [pRabbitDeath, pRabbitDeath + pRabbitBirth, pRabbitDeath+pRabbitBirth+pFoxDeath, 1]
        
        u = 1 - random.uniform(0,1)
        
        for n, probability in enumerate(referenceList):
            if u <= probability:
                break
                
        if n == 0:
            self.R -= 1
        elif n == 1:
            self.R += 1
        elif n == 2:
            self.F -= 1
        else:
            self.F += 1


n = 100

secondPeakMax = []
secondPeakTime = []
foxPopulationDied = 0

for i in range(n):
    t = 0
    tList = [0]
    RabbitList = [R]
    FoxList = [F]

    Simulation = Population(R, F)
    while t < days:
        timing = random.uniform(0,1)
        j = random.uniform(0,1)
    #     t += math.log(1/(1-j))/(Simulation.rateOfExpectedEvents())
        t += random.expovariate(Simulation.rateOfExpectedEvents())
        tList.append(t)
        Simulation.event()
        RabbitList.append(Simulation.R)
        FoxList.append(Simulation.F)
        if Simulation.F == 0:
#             print('Fox Population has Died at {} days'.format(t))
            break
    else:
        foxMaxTime, maxFoxMC = max(enumerate(FoxList[200:]), key=operator.itemgetter(1))
        secondPeakMax.append(maxFoxMC)
        secondPeakTime.append(tList[foxMaxTime])
        continue

    foxPopulationDied += 1
    
print('Fox Population Died out {0} times out of {1}'.format(foxPopulationDied, n))
print('Average maximum fox population (2nd Peak) was {}'.format(sum(secondPeakMax)/len(secondPeakMax)))

movingAverage = []
for i in range(len(secondPeakMax)):
    movingAverage.append(sum(secondPeakMax[:i+1])/len(secondPeakMax[:i+1]))
    
plt.plot(movingAverage)
