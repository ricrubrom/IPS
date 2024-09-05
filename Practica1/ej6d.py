
import numpy as np
from Functions.plot import plot
from Functions.heaviside import heaviside

def svic(phi,a,f0:float, t:np.ndarray):
    result=a*np.sin(2*np.pi*f0*t+phi)
    return result

def svid(n:np.ndarray):
    result=np.pow(1/2,n)*heaviside(n)
    return result

t=np.arange(-10000,10000,.001)
y1=svic(0, 1, 1/2, t)
plot([(-6,8),(-4,4)], "t", "f[n]", "", "Ejercicio 6d", 11, "r", 1.5,t,y1)
print(np.trapezoid(np.pow(np.abs(y1),2),x=t, dx=.001, axis=0))

n=np.arange(-100,100,1)
y2=svid(n)
plot([(-10,10),(-4,4)], "t", "f[n]", "", "Ejercicio 6d", 11, "ro", 1.5,n,y2)
print(np.sum(np.pow(np.abs(y2),2)))
