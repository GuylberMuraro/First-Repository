import numpy as np
import matplotlib.pyplot as plt

n1 = 0
N =100000
R = 0.5

rn = np.zeros(2)
nx_c = []
ny_c = []
par_n = []

#Functions
r = lambda x,y: np.sqrt(x*x + y*y)

def circle(R):
    theta = np.linspace(0, 2*np.pi)
    X = R*np.cos(theta)
    Y = R*np.sin(theta)
    plt.plot(X,Y)

def square(R):
    L = np.linspace(-R,R)
    Rn = R*np.ones(len(L))
    plt.plot(Rn, L)
    plt.plot(-Rn, L)
    plt.plot(L, Rn)
    plt.plot(L, -Rn)

def pi_estimation(n1,N):
    return 16*n1/N # multiply for 4 cause r vector just take one quarter of the square

#Simulation
for i in range(N):
    rn1 = rn.copy()
    x = (2*np.random.random() - 1)
    y = (2*np.random.random() - 1)


    if (r(x,y) or (r(x, y))) <= 0.5:
        n1 += 1
        nx_c.append(x)
        ny_c.append(y)

    par_n.append(r(x,y))


#Export

print(f'{pi_estimation(n1,N)}')

circle(R)
square(R)

plt.scatter(nx_c, ny_c)
plt.show()