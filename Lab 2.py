# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 09:04:44 2022

@author: Edwin
"""
import numpy as np
import matplotlib.pyplot as plt

#Deltoid Curve

theta_1 = np.linspace(0.0,2*np.pi)

x_1=2*np.cos(theta_1)+(np.cos(theta_1*2))
y_1=2*np.sin(theta_1)-np.sin(theta_1*2)

plt.plot(x_1,y_1)
_=plt.title('Deltoid Curve')
plt.show()

#Galilean Spiral

theta_2 = np.linspace(0,10*np.pi,1500)
r = theta_2*2

x_2 = r*np.cos(theta_2)
y_2 = r*np.sin(theta_2)

plt.plot(x_2,y_2)
_=plt.title ("Galilean Spiral")
plt.show()

#Fey's Function

theta_3 = np.linspace(0,24*np.pi,1500)
r_1 = (np.exp(np.cos(theta_3))) - 2*np.cos(theta_3*4) + np.sin(theta_3/12)**5

x_3 = r_1*np.cos(theta_3)
y_3 = r_1*np.sin(theta_3)

plt.plot(x_3,y_3)
_=plt.title ("Fey's Function")
plt.show()



fig,axs = plt.subplots(3)
axs[0].plot(x_1,y_1)
axs[1].plot(x_2,y_2)
axs[2].plot(x_3,y_3)