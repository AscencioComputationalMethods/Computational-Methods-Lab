# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


rng = np.random.default_rng(seed=50) 
N = 100000 
i = 0
j = 0

def move_up(i,j):
    return i,j+1

def move_down(i,j):
    return i,j-1

def move_left(i,j):
    return i-1,j

def move_right(i,j):
    return i+1,j

move = {0:move_up, 1:move_down, 2:move_left, 3:move_right} 

position = []
position.append([i,j])

motion = rng.integers(low=0,high=3,size=N) 
for k in range (len(motion)):
    i,j = (move[motion[k]](i,j))
    
    if i<=-50:
        i=i+1
    elif i>=50:
        i=i-1
    elif j<=-50:
        j=j+1
    elif j>=50:
        j=j-1
    position.append([i,j]) 

fig = plt.figure()
ax = plt.axes(xlim=(-100, 100), ylim=(-100, 100))
particle = plt.Circle((0,0),radius=5,facecolor='black')
ax.add_patch(particle)

def start():
    particle.center = (0,0)
    ax.add_patch(particle)
    return particle,

def create_animate(i):
    x = position[i][0]
    y = position[i][1]
    particle.center = (x,y)
    return particle,
    
anim = animation.FuncAnimation(fig,create_animate,
init_func=start,frames=360,interval=20,blit=True)
anim.save('brownian_motion.ipy') 

