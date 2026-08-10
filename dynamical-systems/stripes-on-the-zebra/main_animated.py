import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

N = 75
array = np.zeros([N,N])

#Functions
def RA(array): #Random Array
    for j in range(len(array)):
        for i in range(len(array)):
            array[j][i] = np.random.randint(2)

def SNN(array): #Sum Nearest Neighbors
    narray = array.copy()
    for j in range(len(narray)):
        for i in range(len(narray)):
            x = narray[(i+1)%len(narray),j] + narray[(i-1)%len(narray),j]
            y = narray[i,(j+1)%len(narray)] + narray[i,(j-1)%len(narray)]
            xy = narray[(i+1)%len(narray), (j+1)%len(narray)] + narray[(i+1)%len(narray), (j-1)%len(narray)] 
            yx = narray[(i-1)%len(narray), (j+1)%len(narray)] + narray[(i-1)%len(narray), (j-1)%len(narray)]

            sum = x + y + xy + yx
            array[i,j] += sum

def rules(array): #rules to update matrix
    narray = array.copy()
    accept = [4,6,7,8,9]
    for i in range(len(narray)):
        for j in range(len(narray)):
            if narray[i,j] in accept:
                array[i,j] = 1
            else:
                array[i,j] = 0

#simulation
RA(array)
fig, ax = plt.subplots()  #create the figure

im = ax.imshow(array, cmap='gray')  # set the function to draw the map

def init():  # this is important to the anmation function format
    return im,


def animate(i): # Simulation in animation

    # Instead of loop, we have this
    SNN(array)
    rules(array)
    im.set_data(array) # just update the data without delete the image entirely

    return im,

# calling the animation function     
anim = animation.FuncAnimation(fig, animate, 
                            init_func = init, 
                            frames = 500,
                            interval = 20, 
                            blit = True) 

plt.show()