# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import numpy.fft as fft

x = np.linspace(0, 1000, 1000)

def fourier(x): 
    fourier_transform = np.fft.rfft(x) 
    fourier_array = int(len(fourier_transform)) 
    new_array = len(fourier_transform)-fourier_array 
    fourier_transform = (fourier_transform[:fourier_array]) 
    fourier_transform= np.pad(fourier_transform,(0,new_array),'constant')
    inverse_fourier = np.fft.irfft(fourier_transform) 
    return inverse_fourier 

def square_wave(x): 
    y = np.zeros(len(x))
    for k in range(len(x)):
        if x[k] < 0.5*x[-1]:
            y[k] = 1
        else:
            y[k] = -1
    return(y)
                           
plt.plot(x,square_wave(x))
plt.title('Square Wave')
plt.show()
    
def sawtooth_wave(x):
    y = x
    return(y)

plt.plot(sawtooth_wave(x))
plt.title('Sawtooth Wave')
plt.show()
   
def modulated_wave(x):
    N = (len(x))
    c = np.zeros(len(x))
    for k in range(N):
        c[k] = np.sin(np.pi*k/N)*np.sin(20*np.pi*k/N)
    return(c)
        
plt.plot(modulated_wave(x))
plt.title('Modulated Sine Wave')
plt.show()

plt.plot (fourier(square_wave(x)))
plt.title ('FT Square Wave')
plt.show()

plt.plot (fourier(sawtooth_wave(x)))
plt.title('FT Sawtooth Wave')
plt.show()

plt.plot(fourier(modulated_wave(x)))
plt.title('FT Modulated Sine Wave')
plt.show()