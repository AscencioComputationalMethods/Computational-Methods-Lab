# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as  plt
#Constant
m= float(input("Enter a mass:")) #changing the mass will show you different trajectory of the cannon ball
R= 0.08 #meters
degree= 30
IV=100
p=1.22
C=0.47
g=9.81
h=1e-4 #steps

def Trajectory(r):
    vx=r[2]
    dx1=vx
    vy=r[3]
    dy1=vy
    dx2=(-(np.pi*R**2*p*C)/(2*m))*vx*((vx**2+vy**2)**0.5)
    dy2=-g-((np.pi*R**2*p*C)/(2*m))*vy*((vx**2+vy**2)**0.5)
    return np.array([dx1,dy1,dx2,dy2],float)
    return(dy2(r)),(dx2(r))


tpoints= np.arange(0,2,h) 
xpoints=[]
ypoints=[]
vxpoints=[]
vypoints=[]

r=np.array([0,0,100*np.cos(30*np.pi/180),100*np.sin(30*np.pi/180)],float)
for t in tpoints:
   xpoints.append(r[0])
   ypoints.append(r[1])
   vxpoints.append(r[2])
   vypoints.append(r[3])
   
   k1=h*Trajectory(r)
   k2=h*Trajectory(r+0.5*k1)
   k3=h*Trajectory(r+0.5*k2)
   k4=h*Trajectory(r+k3)
   r += (k1+2*k2+2*k3+k4)

plt.plot(tpoints,xpoints,label=("first derivative of x"))  
plt.plot(tpoints,ypoints,label=("first derivative of y"))  
plt.plot(tpoints,vxpoints,label=("second derivative of x (vx)"))  
plt.plot(tpoints,vypoints,label=("second derivative of y (vy)"))  
plt.legend()