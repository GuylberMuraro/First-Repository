#imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#parameters
Nb = 40 #board number
board = np.zeros(Nb) #board {we can change it later, choosing it into a function}


#functions
def die(n):  #this is the die
    return np.random.randint(1,n+1)

def count(list, number): # find a number in a list (we can improve it making it searching for more numbers)
    c = 0
    for i in list:
        if i == number:
            c += 1
        else:
            pass
    return c

def next_step(position): # periodic boundery condition (old school)
    d = die(6)
    position = position + d
    if position > Nb:
        position = position - Nb
    else:
        pass
    return position, d

def simple_probability(number, list):  #calculate the probability
    x = count(list, number)
    P = x/(len(list))
    return P

#initial conditions
Nq = 1  # first position
Ninf = int(1e6)  #number of loop steps
Nchance = 1
list_die = []  # list of thrown dice
list_position = []  # list of ocuupied positions

#simulations
for i in range(Ninf):
    Nq, dice = next_step(Nq)  # throw the die and change position
    board[Nq-1] += 1  # accumulate in array
    list_die.append(dice)  # save die number
    list_position.append(Nq)  #save position number

#exports
bins = np.arange(1,42)  # creating bins
plt.hist(list_position,bins, density=True, histtype='bar', rwidth=0.9)  # making the histogram
plt.axis([1,41,0,0.05])  #  delimitering boundary
plt.show()


'''------------------------'''
'''Let's add a prison here!'''
'''------------------------'''

#initial conditions
Nq = 1
Ninf = int(1e6)  #number of steps
Nchance = 1
list_die_prison = []
list_position_prison = []

#simulations
for i in range(Ninf):
    Nq, dice = next_step(Nq)
    if Nq == 30:  # If the player landed in 30 position, move it to 10 position
      Nq = 10
    board[Nq-1] += 1
    list_die_prison.append(dice)
    list_position_prison.append(Nq)


#exports
bins = np.arange(1,42)
plt.hist(list_position_prison,bins, density=True, histtype='bar', rwidth=0.9)
plt.axis([1,41,0,0.06])
plt.show()