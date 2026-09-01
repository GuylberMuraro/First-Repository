import numpy as np

N = 10

'''
f = lambda x: x - 2*np.sin(x)
x = [2, 1.9]
'''

f = lambda x: x**3 - 5*x + 3
x = [0.5, 2]


for i in range(N):
    n = i + 1
    xn = x[n] - f(x[n]) * (x[n] - x[n-1])/(f(x[n]) - f(x[n-1]))
    x.append(xn)
    print(f'{xn:.6f}')