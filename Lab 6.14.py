# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import scipy.constants as cons


V=20
w=1e-9
E=np.linspace(0,20,100) #this is a range from 0 to 20eV

#e=cons.eV
def quantity1(E):
    return np.tan(((w**2*cons.electron_mass*E*cons.e)/(2*cons.hbar**2))**0.5)

def quantity2(E):
    return ((V-E)/E)**0.5

def quantity3(E):
    return -((E/(V-E)))**0.5

#second program
    
def difference1_2(E): 
    return float(quantity1(E)-quantity2(E))

def difference1_3(E):
    return float(quantity1(E)-quantity3(E))

plt.title("Solutions for Values in a Square Potential Well")
plt.xlabel('eV of E')
plt.plot(E,quantity1(E), label='General State')
plt.plot(E,quantity2(E), label= 'Even Numbered State')
plt.plot(E,quantity3(E), label= 'Odd Number State')
plt.ylim([-10,10])
plt.legend()
plt.show

def Solutions(g1,g2,func):

    g1= float(input("Enter a guess from the graph:"))
    g2= float(input("Enter another guess from the graph:"))  
    f1= difference1_2(g1)
    f2= difference1_3(g2)

    if f1>0 and f2>0:
        print('Both entries are positive')
   
    elif f1<0 and f2<0:
        print('Both entries are negative')
  
    else:
        if f1>0 and f2<0:
            xpos=g1
            xneg=g2
        else:
            xpos=g2
            xneg=g1
        while abs(xpos-xneg)>=1e-6:
            x=0.5*(xpos+xneg)
            f3=quantity1(x)-quantity3(x)
            if f3>0:
                xpos=x
            else:
                xneg=x
        return(x)
    
#Use the values located on the right side of Solutions and insert them into the program to obtain a result
print('1st Result',Solutions(0.7,1.4,difference1_3))
print('2nd Result',Solutions(2.6,2.9,difference1_2))
print('3rd Result',Solutions(5.1,5.2,difference1_3))
print('4th Result',Solutions(3.1,3.5,difference1_2))
print('5th Result',Solutions(11,12.4,difference1_3))
print('6th Result',Solutions(14.9,15.4,difference1_2))

