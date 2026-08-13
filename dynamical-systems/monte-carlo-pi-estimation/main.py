import numpy as np
import matplotlib.pyplot as plt

n1 = 0
N =10000
R = 0.5

rn = np.zeros(2)
par_n = []

#Functions
r = lambda x,y: np.sqrt(x*x + y*y)

def circle(R):
    theta = np.linspace(0, 2*np.pi, N)
    X = R*np.cos(theta)
    Y = R*np.sin(theta)
    plt.plot(X,Y)
    

def square(R):
    L = np.linspace(-R,R,N)
    Rn = R*np.ones(len(L))
    plt.plot(Rn, L)
    plt.plot(-Rn, L)
    plt.plot(L, Rn)
    plt.plot(L, -Rn)

for i in range(N):
    rn1 = rn.copy()
    x = np.random.random()
    y = np.random.random()
    rn1[0],rn1[1] = x,y

    if r(x,y) <= 0.5:
        n1 += 1

    par_n.append(rn1)

print(par_n)

circle(R)
square(R)

plt.show()