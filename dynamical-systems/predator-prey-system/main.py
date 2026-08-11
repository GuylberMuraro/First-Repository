import numpy as np
import matplotlib.pyplot as plt

#Parameters

a,b,c,e = 1.1, 0.7, 2.7, 0.4

dt = 0.001
t = np.arange(0,20, dt)
N = len(t)

x = np.zeros(N)
y = np.zeros(N)

#Functions
def f(x,y):
    dxdt = a*x - b*x*y
    dydt = -c*y + e*x*y
    return dxdt,dydt

#Simulation
x[0] = 10
y[0] = 10
for i in range(N-1):
    x[i+1] = x[i] + f(x[i],y[i])[0]*dt
    y[i+1] = y[i] + f(x[i],y[i])[1]*dt

#export
fig, (ax1, ax2) = plt.subplots(2,1)

ax1.plot(x,y)
ax1.set_xlim(0,50)
ax1.set_ylim(0,50)

ax2.plot(t,x)
ax2.plot(t,y)
ax2.set_xlim(0,22)
ax2.set_ylim(0,50)

plt.show()