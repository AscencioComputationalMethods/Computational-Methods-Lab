# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 10:45:09 2022

@author: Student
"""

import numpy as np
import scipy.constants as cons
import gaussxw as gauss

h=cons.h
c=cons.c
kb=cons.Boltzmann
CoolCons=((kb^4)/(4*np.pi^2*c^2*h^3))

def f(z):
    return (x**3)/(np.exp(x)-1)
N=10
a=0
b=1
x,w= gauss.ab(N,a,b)
s=0
for k in range(N):
    s+=w[k]*f(x*[k])
print (s)


print (CoolCons)