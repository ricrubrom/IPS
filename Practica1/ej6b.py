
"""Imports numpy and matplotlib"""
import numpy as np
from Functions.plot import plot
from Functions.heaviside import heaviside
from Functions.odd import odd
from Functions.even import even

def rect(arr:np.ndarray):
    """Creates a rectangular signal"""
    result=heaviside(arr, lim=1)-heaviside(arr-5, lim=1)
    return result


n=np.arange(-7,7+1,1)
h=even(n, rect)
plot([(-4,8),(-4,4)], "t", "f[n]", "", "Ejercicio 6b", 11, "ro", 1.5,n,h)
