import numpy as np
import matplotlib.pyplot as plt

#Parameters
N1 = 4
N2 = 1000
dt = 0.01
r_list = np.arange(0, N1 + dt, dt)
x = np.zeros(N2+1)
X = []
R = []

#Simulation
for i,r in enumerate(r_list):
    x[0] = 0.5
    for j in range(N2):
        x[j+1] = r * x[j] * (1 - x[j])
    c = (x[-10:].copy()).flatten()
    X.append(c)
    ri = np.tile(r,10)
    R.append(ri)

#Data Adjust
Xrr = np.array(X)
Rrr = np.array(R)

Xf = Xrr.flatten()
Rf = Rrr.flatten()

#Export
plt.scatter(Rf, Xf, s=2)
plt.show()
