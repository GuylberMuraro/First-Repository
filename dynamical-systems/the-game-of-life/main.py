import numpy as np

#Parameters
N = 8
array = np.random.randint(0,2, size=(N,N))

#Functions
def neighbors(array):
    kn = array.copy() # neighbors number
    n = len(array)
    for i in range(n):
        for j in range(n):
            #counting neighbors
            x = array[(i+1)%n,j] + array[(i-1)%n,j]
            y = array[i,(j+1)%n] + array[i,(j-1)%n]
            p = array[(i-1)%n,(j+1)%n] + array[(i+1)%n,(j-1)%n]
            s = array[(i-1)%n,(j-1)%n] + array[(i+1)%n,(j+1)%n]

            kn[i,j] = x + y + p + s

            #applying the rules
            if array[i,j] == 1 and (kn == 2 or kn == 3):
                array[i,j] = 1
            if array[i,j] == 0 and kn == 3:
                array[i,j] = 1
            else:
                array[i,j] = 0

