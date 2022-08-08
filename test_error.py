import numpy as np
import matplotlib.pyplot as plt
from odesolve import solveto, euler, rk4


def f(x, t):
    return x


x0 = 1
t1, t2 = 0, 1
hmax_array = np.logspace(-5, -1, 100)
gt_value = np.e
error_euler, error_rk4 = [], []
for hmax in hmax_array:
    guess_euler = solveto(f, x0, t1, t2, hmax, euler)
    guess_rk4 = solveto(f, x0, t1, t2, hmax, rk4)
    error_euler.append(gt_value - guess_euler)
    error_rk4.append(gt_value - guess_rk4)

plt.scatter(hmax_array, error_euler, label='Euler', s=5)
plt.scatter(hmax_array, error_rk4, label='RK4', s=5)
plt.xscale("log")
plt.yscale("log")
plt.xlabel("h")
plt.ylabel("error")
plt.legend()
plt.title('Comparison of errors for Euler and RK4')
plt.show()
