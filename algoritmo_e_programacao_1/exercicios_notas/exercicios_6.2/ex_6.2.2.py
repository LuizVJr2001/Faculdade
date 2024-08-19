#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 21:25:19 2024

@author: luizdevjr
"""

import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()

ax = fig.add_subplot()

x = np.linspace(-20, 20, 100)
f1 = lambda x: 1/(1+np.e**(-x))
ax.plot(x, f1(x), label='1/(1+np.e**(-x))')

x = np.linspace(-200, 200)
ax.plot(x, np.linspace(1, 1), color='gray', ls='--')
ax.plot(x, np.linspace(0, 0), color='gray', ls='--')

ax.set_xlim(-20,20)


ax.grid()
ax.legend()