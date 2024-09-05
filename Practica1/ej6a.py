
"""Imports numpy and matplotlib"""
import numpy as np
from Functions.plot import plot
from Functions.heaviside import heaviside

def triangle(arr:np.ndarray):
    """Creates a tringle signal"""
    result=np.zeros(arr.size)
    for i,x in enumerate(arr):
        result[i]=(x+1)*((x>=-1)&(x<1))+(-x+3)*((x>=1)&(x<3))
    return result


t=np.arange(-3,8,0.001)
h=triangle(t/2)
plot([(-2,8),(-4,4)], "t", "f(t)", "", "Ejercicio 6a", 11, "r", 1.5,t,h*(heaviside(t+2)-heaviside(t-2)))
