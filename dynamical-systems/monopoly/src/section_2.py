#imports
import numpy as np
import pandas as pd
#np.random.seed(1)

#parameters
Nb = 40 #board number
board = np.zeros(Nb) #board {we can change it later, choosing it into a function}

#print(f'test\n{board}')#test
#print(len(board))

#functions
def die(n):
    return np.random.randint(1,n+1)

def count(list, number): # find a number in a list (we can improve it making it searching for more numbers)
    c = 0
    for i in list:
        if i == number:
            c += 1
        else:
            pass
    return c

def next_step(position): # periodic boundery condition
    d = die(6)
    position = position + d
    if position > Nb:
        position = position - Nb
    else:
        pass
    return position, d

def simple_probability(number, list):
    x = count(list, number)
    P = x/(len(list))
    return P

#initial conditions
Nq = 1
Ngames = 10
Nchance = 1
list_die_global = []
list_position_global = []

#print(f'Testing next step:{next_step(Npl)}')

#simulations

for i in range(Ngames):
    Npl = 1
    list_die = []
    list_position = []
    position = Nq
    while position <= 40:
        d = die(6)
        position = position + d
        if position == 30:
            position = 10
        list_position.append(position)
        list_die.append(d)
    list_die_global.append(list_die)
    list_position_global.append(list_position)
    #print(f'Game {i+1}')
    #print(f'Field landed:{list_position}\nNumber thrown on the dice:{list_die}\nNumber of throws:{len(list_die)}')
    #print(f'Probability of falling {Nchance}: {100*simple_probability(Nchance,list_die):.1f}%')
print(list_position_global)
print('-+-+'*25)
print(list_die_global)

#exports

tables = []
for i in range(Ngames):
    tables.append(pd.DataFrame({'Thrown Dice':list_die_global[i], 'Landed Position':list_position_global[i]}))


#print(tables[1])