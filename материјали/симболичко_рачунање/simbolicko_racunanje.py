# -*- coding: utf-8 -*-
"""
Created on Sun Jun  1 21:34:11 2025

@author: Zbook
"""
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
# може и овако:
#from matplotlib import pyplot as plt

# Први задатак
"""
x = sp.Symbol('x',  real=True)

f = sp.cos(x**2 + 2*x + 3) * sp.sin(x - 1)

f_d = f.diff()
#f_d = f.diff(x)
f_dd = f.diff(x, 2)  # или f_d.diff(x), или sp.diff(f_d, x)

print(f_d)
#print()
print(f_dd)

xx = np.linspace(-10, 10, 10000)
fig, ax = plt.subplots(nrows=3)
ax[0].plot(xx, sp.lambdify(x, f)(xx))
ax[1].plot(xx, sp.lambdify(x, f_d)(xx))
ax[2].plot(xx, sp.lambdify(x, f_dd)(xx))
plt.show()
"""

# Други задатак
"""
x = sp.Symbol('x')

f = (1 + x**2 + 2*x**4) / (2 * x**2) 

rezultat = sp.integrate(f, x)

print(rezultat)
"""


# Трећи задатак
"""
E, k, t, Tp, tau = sp.symbols('E k t Tp tau')
wp = 2 * sp.pi / Tp

# правоугаони импулс
c_r = sp.integrate((1/Tp)*(E * sp.exp(-sp.I * k * wp * t)), (t, -tau/2, tau/2))

# тестерасти импулс
c_t = sp.integrate((1/Tp)*(E * t * sp.exp(-sp.I * k * wp * t)), (t, 0, Tp))

print(c_r.simplify())
print(c_t.simplify())

# Питање: Да ли се ови изрази могу поједноставити? Да, уколико је k целобројно!
# дефинисати k као k = sp.Symbol('k', integer=True)

# други део проблема
c_r, c_t = c_r.subs({E: 3, Tp: 2, tau: 1}), c_t.subs({E: 3, Tp: 2})
c0_r, c0_t = float(c_r.subs(k, 0)), float(c_t.subs(k, 0))
ck_r, ck_t = sp.lambdify(k, c_r), sp.lambdify(k, c_t)

wp = np.pi
t = np.linspace(-4, 4, 2048)
for N in [3, 10, 20]:
    x_r, x_t = 0, 0
    for k in range(-N, N+1):
        if k == 0:
            x_r += c0_r
            x_t += c0_t
        else:
            x_r += ck_r(k) * np.exp(1j*k*wp*t)
            x_t += ck_t(k) * np.exp(1j*k*wp*t)

    fig, ax = plt.subplots(nrows=2)
    ax[0].plot(t, x_r)
    ax[1].plot(t, x_t)
    plt.show()
"""
