# -*- coding: utf-8 -*-
"""
Created on Tue May 27 16:02:21 2025

@author: Zbook
"""
import numpy as np
import scipy
import matplotlib.pyplot as plt


# Задатак 1
"""
E1 = 33
E2 = 18
Ig1 = 0.03
Ig2 = 0.01
R1 = 300
R2 = 500
R3 = 120
R4 = 300
R5 = 200
R6 = 180
R7 = 520

G11 = 1/R1 + 1/R3 + 1/R5
G12 = -1/R3
G13 = -1/R1
G22 = 1/R3 + 1/R4 + 1/R2
G23 = -1/R4
G33 = 1/R1 + 1/R4 + 1/(R6 + R7)

I1 = E1/R1 - Ig1
I2 = -E2/R2 - Ig2
I3 = -E1/R1 + Ig1

G = np.array([[G11, G12, G13], [G12, G22, G23], [G13, G23, G33]])
I = np.array([I1, I2, I3])

V = np.linalg.solve(G, I)

print(V)
"""


# Задатак 2
"""
R = 1000
L = 1
C = 6.25*10**(-6)
I = 2*10**(-3)

def delta(t):
    sigma = 0.01
    return 1 / (sigma * np.sqrt(2 * np.pi)) * np.exp(-t**2 / (2 * sigma**2))

def rlc(t, x):
    x0, x1 = x  # x0 -> i_LC; x1 -> di_LC/dt
    dx0dt = x1
    dx1dt = (R*I*delta(t) - R*x1 - x0/C) / L
    return [dx0dt, dx1dt]

ilc0 = [0, 0] # почетни услови

# време
t_span = (0, 0.1)
t_eval = np.linspace(*t_span, 100000000)

# решење диференцијалне једначине
ilc = scipy.integrate.solve_ivp(rlc, t_span, ilc0, t_eval=t_eval)

print(ilc)

# цртање графика
plt.plot(ilc.t, ilc.y[0], label='i_LC')
plt.xlabel('Vreme (s)')
plt.ylabel('Odziv (А)')
plt.title('Vremenski oblik struje i_LC')
plt.grid(True)
plt.legend()
plt.show()
"""

# Задатак 3
"""
f = lambda x : (x**2 + 1)/(x**3 + 3*x + 1)**2

solution, error = scipy.integrate.quad(f, 0, 1)

print(solution)

print(4/15)
"""




