
import numpy as np
import matplotlib.pyplot as plt

g=9.8
l= 0.1 #length 
time_start=0
time_end=7
omega0=0
theta0= np.cos(np.radians(179))
N=10000
h=(time_end-time_start)/N

def f(r,t):
    theta =r[0]
    omega = r[1]
    ftheta= omega
    fomega = (g/l)*np.sin(theta)
    return np.array([ftheta,fomega],float)

pendulum_time = np.arange(time_start,time_end,h) 
thetapoints = [] 
x = np.array([theta0, omega0],float)

for t in pendulum_time: #Runge-Kutta!
    thetapoints.append(x[0])
    k1 = h*f(x,t)
    k2 = h*f(x+0.5*k1,t+0.5*h)
    k3 = h*f(x+0.5*k1,t+0.5*h)
    k4 = h*f(x+k3,t+h)
    x += (k1+2*k2+2*k3+k4)/6
    
plt.plot(pendulum_time,thetapoints)
plt.xlabel('Time')
plt.ylabel('Displacement in Seconds')
plt.show()