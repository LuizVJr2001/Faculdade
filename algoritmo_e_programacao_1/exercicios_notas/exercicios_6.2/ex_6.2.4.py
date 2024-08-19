#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 22:01:43 2024

@author: luizdevjr
"""

import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot()

x = np.linspace(-np.pi, 0)
f1 = lambda x: np.cos(x)
ax.plot(x, f1(x), label='cos(x)')

x = np.linspace(0, 2)
f1 = lambda x: 1-x**2
ax.plot(x, f1(x), label='1-x**2')

ax.set_xlabel('x')
ax.set_ylabel('y')

ax.annotate('mín. local', xy=(0,1), xytext=(0,0), arrowprops={'arrowstyle':'->'})

ax.grid()
ax.legend()