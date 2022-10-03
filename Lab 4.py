# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 11:23:18 2022

@author: Student
"""
import numpy as np
import matplotlib.pyplot as plt

dirac= np.array([1e-2, 1e-4, 1e-6, 1e-8, 1e-10, 1e-12, 1e-14])
x=1

def deriv(x):
    return (x*(x-1))

Der=((deriv(x+dirac)-deriv(x))/(dirac))

print(Der)
plt.xscale("log")
plt.ylim([0.998,1.002])
plt.plot(dirac,Der)