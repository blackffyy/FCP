# -*- coding: utf-8 -*-
"""
Created on Sun Aug  7 14:15:04 2022

@author: ASUS
"""

from odesolve import solveto, euler, rk4
def f ( x , t ) :
    return x
x0 = 1
t0 = 0
t1 = 1
hmax = 0.3
x1 = solveto(f,x0,t0,t1,hmax)
print(x1)

