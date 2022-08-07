# -*- coding: utf-8 -*-
"""
Created on Sun Aug  7 15:41:21 2022

@author: ASUS
"""

import numpy as np
import matplotlib.pyplot as plt
from odesolve import odesolve
def f (X, t ):
    x,y = X
    dxdt = y
    dydt = -x    
    return np.array([dxdt,dydt])
x0 = 1
y0 = 0
X0 = np.array([x0,y0])
h = 0.01 
t = np.linspace(0,10,100)
Xt = odesolve(f,X0,t,h)
plt.plot( t,Xt.T[0])
plt.plot(t,Xt.T[1])
plt.savefig('shm.pdf')
plt.show()
