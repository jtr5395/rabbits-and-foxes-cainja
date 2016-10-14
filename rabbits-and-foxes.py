
# coding: utf-8

# # Rabbits and foxes
# 
# There are initially 400 rabbits and 200 foxes on a farm (but it could be two cell types in a 96 well plate or something, if you prefer bio-engineering analogies). Plot the concentration of foxes and rabbits as a function of time for a period of up to 600 days. The predator-prey relationships are given by the following set of coupled ordinary differential equations:
# 
# \begin{align}
# \frac{dR}{dt} &= k_1 R - k_2 R F \tag{1}\\
# \frac{dF}{dt} &= k_3 R F - k_4 F \tag{2}\\
# \end{align}
# 
# * Constant for growth of rabbits $k_1 = 0.015$ day<sup>-1</sup>
# * Constant for death of rabbits being eaten by foxes $k_2 = 0.00004$ day<sup>-1</sup> foxes<sup>-1</sup>
# * Constant for growth of foxes after eating rabbits $k_3 = 0.0004$ day<sup>-1</sup> rabbits<sup>-1</sup>
# * Constant for death of foxes $k_1 = 0.04$ day<sup>-1</sup>
# 
# Also plot the number of foxes versus the number of rabbits.
# 
# Then try also with 
# * $k_3 = 0.00004$ day<sup>-1</sup> rabbits<sup>-1</sup>
# * $t_{final} = 800$ days
# 
# *This problem is based on one from Chapter 1 of H. Scott Fogler's textbook "Essentials of Chemical Reaction Engineering".*
# 

# # Solving ODEs
# 
# *Much of the following content reused under Creative Commons Attribution license CC-BY 4.0, code under MIT license (c)2014 L.A. Barba, G.F. Forsyth. Partly based on David Ketcheson's pendulum lesson, also under CC-BY. https://github.com/numerical-mooc/numerical-mooc*
# 
# Let's step back for a moment. Suppose we have a first-order ODE $u'=f(u)$. You know that if we were to integrate this, there would be an arbitrary constant of integration. To find its value, we do need to know one point on the curve $(t, u)$. When the derivative in the ODE is with respect to time, we call that point the _initial value_ and write something like this:
# 
# $$u(t=0)=u_0$$
# 
# In the case of a second-order ODE, we already saw how to write it as a system of first-order ODEs, and we would need an initial value for each equation: two conditions are needed to determine our constants of integration. The same applies for higher-order ODEs: if it is of order $n$, we can write it as $n$ first-order equations, and we need $n$ known values. If we have that data, we call the problem an _initial value problem_.
# 
# Remember the definition of a derivative? The derivative represents the slope of the tangent at a point of the curve $u=u(t)$, and the definition of the derivative $u'$ for a function is:
# 
# $$u'(t) = \lim_{\Delta t\rightarrow 0} \frac{u(t+\Delta t)-u(t)}{\Delta t}$$
# 
# If the step $\Delta t$ is already very small, we can _approximate_ the derivative by dropping the limit. We can write:
# 
# $$\begin{equation}
# u(t+\Delta t) \approx u(t) + u'(t) \Delta t
# \end{equation}$$
# 
# With this equation, and because we know $u'(t)=f(u)$, if we have an initial value, we can step by $\Delta t$ and find the value of $u(t+\Delta t)$, then we can take this value, and find $u(t+2\Delta t)$, and so on: we say that we _step in time_, numerically finding the solution $u(t)$ for a range of values: $t_1, t_2, t_3 \cdots$, each separated by $\Delta t$. The numerical solution of the ODE is simply the table of values $t_i, u_i$ that results from this process.
# 

# # Euler's method
# *Also known as "Simple Euler" or sometimes "Simple Error".*
# 
# The approximate solution at time $t_n$ is $u_n$, and the numerical solution of the differential equation consists of computing a sequence of approximate solutions by the following formula, based on Equation (10):
# 
# $$u_{n+1} = u_n + \Delta t \,f(u_n).$$
# 
# This formula is called **Euler's method**.
# 
# For the equations of the rabbits and foxes, Euler's method gives the following algorithm that we need to implement in code:
# 
# \begin{align}
# R_{n+1} & = R_n + \Delta t \left(k_1 R_n - k_2 R_n F_n \right) \\
# F_{n+1} & = F_n + \Delta t \left( k_3 R_n F_n - k_4 F_n \right).
# \end{align}
# 

# In[1]:


import numpy as np
from matplotlib import pyplot as plt


# In[2]:


R = 400
F = 200
k1 = 0.015
k2 = 0.00004
k3 = 0.0004
k4 = 0.04

endtime = 600*24*60

Rlist = [R]
Flist = [F]
dRlist = []
dFlist = []
tlist = [0]

for t in range(endtime):
    dR = (k1*R) - (k2*R*F)
    dF = (k3*R*F) - (k4*F)
    R += dR/(endtime/600)
    F += dF/(endtime/600)
    if t%(24*60) == 0: #clean up the plots a little bit
        Rlist.append(R)
        Flist.append(F)
        tlist.append((t+1)/(endtime/600))

fig, ax = plt.subplots(1,1)
rabbits, = ax.plot(tlist, Rlist, '.', markersize = 5, label = 'Rabbits')
foxes, = ax.plot(tlist, Flist, '^', markersize = 5, label = 'Foxes' )
ax.legend(loc=7) #move the legend to above the graph
ax.set_title('Rabbits and Foxes v. Time')
ax.set_xlabel('Time (day)')
ax.set_ylabel('Number')

fig.tight_layout()
plt.show()


# #### With changes to k3, and time duration to 800.

# In[3]:


R = 400
F = 200
k1 = 0.015
k2 = 0.00004
k3 = 0.00004
k4 = 0.04

endtime = 800*24*60

Rlist = [R]
Flist = [F]
dxlist = []
dylist = []
tlist = [0]

for t in range(endtime):
    dR = (k1*R) - (k2*R*F)
    dF = (k3*R*F) - (k4*F)
    R += dR/(endtime/800)
    F += dF/(endtime/800)
    if t%(endtime/800) == 0:
        Rlist.append(R)
        Flist.append(F)
        tlist.append((t+1)/(endtime/800))

fig, (ax, ay) = plt.subplots(1,2)
rabbits, = ax.plot(tlist, Rlist, '.', markersize = 5, label = 'Rabbits')
foxes, = ax.plot(tlist, Flist, '^', markersize = 5, label = 'Foxes')
ax.legend()
ax.set_title('Rabbits and Foxes v. Time')
ay.plot(Rlist, Flist)
ay.set_title('Foxes vs. Rabbits')
ax.set_xlabel('Time (day)')
ax.set_ylabel('Number')
ay.set_ylabel('Number of Foxes')
ay.set_xlabel('Number of Rabbits')

fig.tight_layout()
plt.show()


# ### Using odeint from scipy.integrate

# In[4]:

from scipy.integrate import odeint 

R = 400
F = 200
k1 = 0.015
k2 = 0.00004
k3 = 0.0004
k4 = 0.04

def riseAndFall(RandF, t):
    R, F = RandF
    dR = (k1*R) - (k2*R*F)
    dF = (k3*R*F) - (k4*F)
    return [dR, dF]

days = 600

# t = [days * float(i) / ((days*24*60) - 1) for i in range(days*24*60)]
t = range(days)
wickedList = odeint(riseAndFall, [R,F], t)
# I didn't know it returned an array...too late now...

plt.plot(t, wickedList)
plt.show()


# In[5]:

import operator
rabbits, foxes = wickedList.T
rabbitTime, maxRabbits = max(enumerate(rabbits[200:]), key=operator.itemgetter(1))
foxTime, maxFoxes = max(enumerate(foxes[200:]), key=operator.itemgetter(1))


# In[6]:

print('The maximum number of foxes was {0} at {1} days.'.format(maxFoxes, foxTime+200))


# # Implementing Kinetic Monte Carlo Simulations

# In[45]:

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


# In[57]:

n = 1000

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


# In[58]:


movingAverage = []
for i in range(len(secondPeakMax)):
    movingAverage.append(sum(secondPeakMax[:i+1])/len(secondPeakMax[:i+1]))
    
plt.plot(movingAverage)


# In[ ]:



