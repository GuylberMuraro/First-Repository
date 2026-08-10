import numpy as np
import matplotlib.pylab as plt

a = [0,1]
N = 8
replace = True
prob = [0.99,0.01]

'''
x = np.random.choice(a, size=(N,N), p=prob)

'''
'''
x = np.random.binomial(1, 0.5, size=(N,N))

y = np.random.binomial(1000,0.5, 1000000)

print(x)


plt.hist(y, bins = 50, density=True)
plt.show()
'''

import matplotlib.animation as animation

fig = plt.figure()
axis = plt.axes(xlim=(-50,50),
                ylim=(-50,50))

line, = axis.plot([],[], lw=2)

def init(): 
    line.set_data([], []) 
    return line,

xdata, ydata = [], []

def animate(i): 
    # t is a parameter which varies 
    # with the frame number 
    t = 0.1 * i 
    
    # x, y values to be plotted 
    x = t * 5
    y = t * 5
    
    # appending values to the previously 
    # empty x and y data holders 
    xdata.append(x) 
    ydata.append(y) 
    line.set_data(xdata, ydata) 
    
    return line, 

# calling the animation function     
anim = animation.FuncAnimation(fig, animate, 
                            init_func = init, 
                            frames = 500,
                            interval = 20, 
                            blit = True) 

# saves the animation in our desktop 
anim.save('growingCoil.mp4', writer = 'ffmpeg', fps = 30) 