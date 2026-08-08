import numpy as np

N = 8
array = np.random.randint(0,2, size=(N,N))


def step(array):
    array1 = array.copy()
    n = len(array)
    for i in range(n):
        for j in range(n):
            x = array[(i+1)%n,j] + array[(i-1)%n,j]
            y = array[i,(j+1)%n] + array[i,(j-1)%n]
            p = array[(i-1)%n,(j+1)%n] + array[(i+1)%n,(j-1)%n]
            s = array[(i-1)%n,(j-1)%n] + array[(i+1)%n,(j+1)%n]

            array1[i,j] = x + y + p + s