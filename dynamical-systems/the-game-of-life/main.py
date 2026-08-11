import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

#Parameters
N = 100
array = np.random.randint(0,2, size=(N,N))

#Functions
def neighbors(array): #counting neighbers
    kn = array.copy() # neighbors number
    array1 = array.copy()
    n = len(array)
    for i in range(n):
        for j in range(n):
            #counting neighbors
            x = array1[(i+1)%n,j] + array1[(i-1)%n,j]
            y = array1[i,(j+1)%n] + array1[i,(j-1)%n]
            p = array1[(i-1)%n,(j+1)%n] + array1[(i+1)%n,(j-1)%n]
            s = array1[(i-1)%n,(j-1)%n] + array1[(i+1)%n,(j+1)%n]

            kn[i,j] = x + y + p + s

            #applying the rules and update the array
            if array1[i,j] == 1 and (kn[i,j] == 2 or kn[i,j] == 3): #[alive] --> [alive]
                array[i,j] = 1
            elif array1[i,j] == 0 and kn[i,j] == 3:                   #[dead] --> [alive]
                array[i,j] = 1
            else:                                                   #[dead] --> [dead]
                array[i,j] = 0
    return kn


#Simulation and export
fig, ax = plt.subplots()
im = ax.imshow(array, cmap='binary')

def init():
    return im,

def animate(i):
    neighbors(array)
    im.set_data(array)

    return im,

anim = animation.FuncAnimation(fig, animate, init_func=init, frames=1000, interval=100, blit=True)

plt.show()