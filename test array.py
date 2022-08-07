# -*- coding: utf-8 -*-
"""
Created on Sun Aug  7 15:14:52 2022

@author: ASUS
"""

from odesolve import euler, rk4, solveto, odesolve
import numpy as np
def f(X, t):
        x1, x2 = X
        dx1dt = x2
        dx2dt = -x1
        dXdt = [dx1dt, dx2dt]
        return np.array(dXdt)

X0 = np.array([1, -1])
print(np.allclose(euler(f, X0, 0, 1), np.array([0, -2])))
print(np.allclose(rk4(f, X0, 0, 1), np.array([-0.29166667, -1.375])))
print(np.allclose(solveto(f, X0, 0, 1, 0.25), np.array([-0.30859375, -1.56640625])))
print(np.allclose(solveto(f, X0, 0, 1, 0.25, rk4), np.array([-0.30112267, -1.38177358])))