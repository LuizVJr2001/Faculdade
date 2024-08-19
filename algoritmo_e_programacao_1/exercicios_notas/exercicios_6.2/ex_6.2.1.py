# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 15:39:35 2024

@author: luizd
"""
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()

ax = fig.add_subplot()

x = np.linspace(-2, 2)
f1 = lambda x: x**2
ax.plot(x, f1(x))

x = np.linspace(-3, 0)
f2 = lambda x: 2*x**3+2
ax.plot(x, f2(x))

x = np.linspace(-np.pi, np.pi)
f3 = lambda x: np.sin(x)
ax.plot(x, f3(x))

ax.grid()