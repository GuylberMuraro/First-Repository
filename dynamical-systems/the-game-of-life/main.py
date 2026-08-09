import numpy as np

#Parameters
N = 8
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
            if array1[i,j] == 0 and kn[i,j] == 3:                   #[dead] --> [alive]
                array[i,j] = 1
            else:                                                   #[dead] --> [dead]
                array[i,j] = 0
    return kn
            
            

#Simulation

print(f'{array}\n\n')

neighbors(array)


print(array)