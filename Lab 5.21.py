# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import scipy.constants as cons


Charge_1 = [65,70] #the charges
Charge_2 = [75,70]
N = 100
h = 10

def r(deltax,deltay): 
    return (deltax**2+deltay**2)**0.5

x = np.linspace(65,75,N)
xgrid, ygrid = np.meshgrid(x,x)

potential = np.zeros((N, N))
for i in range(N):
    for j in range(N):
        position_1 = ((xgrid[i][j]-Charge_1[0])**2+(ygrid[i][j]-Charge_1[1])**2)**0.5
        position_2 = ((xgrid[i][j]-Charge_2[0])**2+(ygrid[i][j]-Charge_2[1])**2)**0.5
        potential[i][j] = (1/ 4*np.pi*cons.epsilon_0)*(1/position_1-1/position_2)

plt.imshow(potential)
plt.title("Electric Field Potential")
plt.show()


dist_x1, dist_y1 = xgrid-Charge_1[0], ygrid-Charge_1[1]
dist_x2, dist_y2 = xgrid-Charge_2[0], ygrid-Charge_2[1]

def Partials(q,deltax, deltay):
    return q*(1/ 4*np.pi*cons.epsilon_0)*(1/r(deltax, deltay))

partialx = ((Partials(1,(dist_x1 + h / 2),dist_y1)-Partials(1,(dist_x2-h/2),dist_y2))/h)+((Partials(-1,(dist_x2 + h/2), dist_y2)-Partials(-1,(dist_x2-h/2),dist_y2))/h)
partialy = ((Partials(1,dist_x1,(dist_y1 + h / 2))-Partials(1,dist_x1,(dist_y1-h/2)))/h)+((Partials(-1,dist_x2,(dist_y2 + h / 2))-Partials(-1,dist_x2,(dist_y2-h / 2)))/h)

plt.streamplot(xgrid, ygrid, partialx, partialy)
plt.title("Electric Field")
plt.show()