# -*- coding: utf-8 -*-
"""
Created on Sat Aug  6 22:33:56 2022

@author: ASUS
"""

from collections.abc import Callable
import numpy as np
def euler(f, x, t, h):
    """Perform one step of the Euler method"""
#Eular Method
def eular_derivative(x0,h):
#Returns the value of the derivative corresponding to x0, y0
  return 0-h**2
#Here needs to be changed to the corresponding derivative value
def eular_method(f,x,t,h):
#Returns the x, y values of Euler's formula for the given conditions
  y = [h]
  x2 = [f]
  while x2[-1]<x:
    y.append(y[-1]+eular_derivative(x2[-1],y[-1])*t)
    x2.append(x2[-1]+t)
  return x2,y
eular_x,eular_y = eular_method(0,1,0.1,1)#Here need to modify the initial values of x and y, the step size and the final value of x  
#This coode were looking online from this website: https://blog.csdn.net/weixin_47104677/article/details/121477943   
