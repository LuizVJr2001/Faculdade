#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 14:41:38 2024

@author: luizdevjr
"""

import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0.1, 5.,100)
y = np.log(x)

fig = plt.figure() #Cria uma figure

ax = fig.add_subplot() #Define um subplot na figure

ax.plot(x,y, ls='-',label = 'y=ln(x)') #É possivel usar Latex na Label
ax.plot(x, 1/x, ls='--', color='red',label = 'y=ln\'(x)')
ax.legend()
ax.set_xticks(np.linspace(0.1, 5.,10))
ax.set_xlabel('x', fontsize=20)
ax.set_ylabel('y')
#plt.savefig('fig.png')  #Salva a imagem do gráfico