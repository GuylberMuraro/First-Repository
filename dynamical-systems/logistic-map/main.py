import numpy as np
import matplotlib.pyplot as plt

N1 = 4
N2 = 1000
dt = 0.01
r_list = np.arange(0, N1 + dt, dt)
rs = len(r_list)
x = np.zeros(N2+1)
X = []
R = []


for i,r in enumerate(r_list):
    x[0] = 0.5
    for j in range(N2):
        x[j+1] = r * x[j] * (1 - x[j])
    c = (x[-10:].copy()).flatten()
    X.append(c)
    ri = np.tile(r,10)
    R.append(ri)

Xrr = np.array(X)
Rrr = np.array(R)

#Xf = Xrr.flatten()
#Rf = Rrr.flatten()

print(Xrr)
#plt.scatter(Rf,Xf)
#plt.show()
'''
R_list = r_list[-10:]
# keep trying implementing tile method
Y.tile(R_list,(rs,1))

print(Y)


plt.scatter(RM, X)
plt.show()
'''