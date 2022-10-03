# -*- coding: utf-8 -*-

import numpy as np
import time
import timeit

#store stating time
begin=time.time()

def yk(x):
    return (1-x**2)

start_time= print(timeit.timeit('output=1-x**2','x=2'))

def integral(n):
    sum = 0
    h = 2/n
    xval= np.arrange(-1,1,n)
    
    for x in xval:
        xk = -1 + (h*k)
    sum = h*xk(yk)
    return (sum)
print(integral)

#store end time

end=time.time()

#total time taken
print(f'Total runtime of the program is {end-begin}')
