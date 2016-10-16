from matplotlib import pyplot as plt
import pyximport; pyximport.install()
import CythonMaybe as CM


# # Implementing Kinetic Monte Carlo Simulations


Runs = 10

foxMaxTime, maxFoxMC, secondPeakMax, secondPeakTime, foxPopulationDied = CM.cainjaCython(Runs)


movingAverage = []
for i in range(len(secondPeakMax)):
    movingAverage.append(sum(secondPeakMax[:i+1])/len(secondPeakMax[:i+1]))

print('Fox Population Died out {0} times out of {1}'.format(foxPopulationDied, Runs))

if len(secondPeakMax) != 0:
    print('Average maximum fox population (2nd Peak) was {}'.format(sum(secondPeakMax)/len(secondPeakMax)))
    plt.plot(movingAverage)
    plt.show()
