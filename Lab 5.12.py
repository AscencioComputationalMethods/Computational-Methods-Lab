# -*- coding: utf-8 -*-

import scipy.constants as cons
import numpy as np

"""
In this laboratory activity, the goal is to derive the Stefan-Boltzmann constant by evaluating an integral.
"""
a = 0.1
b = 10
N=10000
h=(b-a)/N
SB = cons.Stefan_Boltzmann

def term(T):
    x=(cons.k**4)/(4*np.pi**2)*(cons.c**2)*(cons.hbar**3)
    return (T**4*x)

def integral(x):
    return (x**3)/(np.exp(x)-1)

def f(a,b,N): 
    h=(b-a)/N
    s = (0.5*integral(a)+0.5*integral(b))

    for k in range(N):
        s+=integral(a+k*h)
        
    return (h*s)

W=term(1)*f(a,b,N)

print("Using the Trapezoidal integration method we obtain: ",W)
print("Our code evaulates the Stefan-Boltzmann constant as: ",SB)
