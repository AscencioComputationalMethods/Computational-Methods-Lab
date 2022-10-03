# -*- coding: utf-8 -*-


from random import random
import matplotlib.pyplot as plt
import numpy as np

rng = np.random.default_rng(seed=50)

def p(x):
    return 1/((x)*2)**0.5

def f(x):
    return (2/(np.exp(x)+1))

N = 1000000
z = rng.random(1000)
x = z**2
answer = np.mean(f(x))
print("The value for the integral when using Monte Carlo integration is ",answer)

histogram = plt.hist 
plt.hist(x)
plt.title("Probability Distribution for the Integral")
plt.show()