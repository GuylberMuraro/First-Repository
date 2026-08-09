import numpy as np
import matplotlib.pyplot as plt

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
arrays = []
RA(array)
for i in range(50):
    array1 = array.copy()
    arrays.append(array1)

    SNN(array)
    rules(array)


#output
for i in range(0,25):
    print(f'Figura{i+1}')
    plt.imshow(arrays[i], cmap='gray')
    plt.colorbar()
    plt.show()

