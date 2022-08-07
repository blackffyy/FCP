# odesolve.py
#
# Author: <insert name>
# Date:   <insert date>
# Description: <insert description>
#
# You should fill out the code for the functions below so that they pass the
# tests in test_odesolve.py

def euler(f, x, t, h):
    """Perform one step of the Euler method"""#Eular Method
    return x + f (x , t )*h #functionof the Euler method
    pass


def rk4(f, x, t, h):
    """Perform one step of the RK4 method"""#RK4 method
#Four step fot the RK4:
    k1 = f(x,t)
    k2 = f(x+k1*(h/2),t+(h/2)) 
    k3 = f(x+k2*(h/2),t+(h/2)) 
    k4 = f(x+k3*h,t+h)
    return x + ( k1 + 2*k2 + 2*k3 + k4 ) * h/6#output function
    pass


def solveto(f, x1, t1, t2, hmax, method=euler):
    """Use many steps of method to get from x1,t1 to x2,t2"""
    loop = (t2 - t1)/hmax 
    loop = int(round(loop))
    Damonsb = x1
    t = t1
    for i in range(0,loop):
        if method == rk4:
            Damonsb = rk4(f, Damonsb, t, hmax)
        else:
            Damonsb = euler(f, Damonsb, t, hmax) 
        t = t+hmax  
    if t != t2:
        hmax = t2 - t
        if method == rk4:
            Damonsb = rk4(f, Damonsb, t, hmax)
        else:
            Damonsb = euler(f, Damonsb, t, hmax) 
        t = t+hmax  
    return Damonsb
    pass


def odesolve(f, X0, t, hmax, method=euler):
    """Compute the solution at different values of t"""
    import numpy as np
    t0 = t[0]
    YM = []
    try:
        Damon = X0[1]
    except:
        X0 = X0[0]
    for i in t:
        SBHY = solveto(f, X0, t0, i, hmax, method)
        YM.append(SBHY)
    YM = np.array(YM)
    return YM  
    pass
