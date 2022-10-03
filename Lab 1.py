# -*- coding: utf-8 -*-

g=9.8
h= float(input('What is the height'));
d=(0.5)*g*h**2;
t=((2*d)/g)**0.5;
print(d,t)

light_year=.99
v=10
Gamma= 1/((1-v**2)**0.5)
Time_Dilation=light_year/Gamma
Earth = light_year/v
Ship = Time_Dilation/v

print("The time in years that the spaceship takes to reach its destination in the rest frame of an observer on Earth", Earth)
print("The time,in years,that the spaceship takes as perceived by a passenger on board the ship ",Ship)