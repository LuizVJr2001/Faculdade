#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 21:44:44 2024

@author: luizdevjr
"""

import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot()

x1 = np.linspace(-2, 0)
f1 = lambda x: 1/x 
ax.plot(x1, f1(x1), color='blue')

x2 = np.linspace(0,2)
ax.plot(x2, f1(x2), color='blue')

ax.plot((0,0), (-50, 50), color='gray', ls='--')

ax.set_ylim(-10,10)

ax.grid()