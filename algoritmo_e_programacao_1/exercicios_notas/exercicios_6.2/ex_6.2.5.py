#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 22:11:39 2024

@author: luizdevjr
"""

import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot()

x = np.linspace(-20, 20, 500)
f1 = lambda x: x+1
ax.plot(x, f1(x), label='x+1')

f1 = lambda x: x**2
ax.plot(x, f1(x), label='x**2')

ax.set_ylim(-10,10)
ax.set_xlim(-10,10)

x1 = ((1+5**0.5)/2)
x2 = ((1-5**0.5)/2)

ax.plot(x1 , f1(x1), marker='o')
ax.plot(x2 , f1(x2), marker='o')

ax.annotate('pto. de interseção',xy=(x1,f1(x1)), xytext=(4, 2.5), arrowprops={'arrowstyle':'->'})
ax.annotate('pto. de interseção',xy=(x2,f1(x2)), xytext=(0, -2.5), arrowprops={'arrowstyle':'->'})

ax.grid()
ax.legend()