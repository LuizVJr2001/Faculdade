# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 19:59:36 2024

@author: luizd
"""
import numpy as np
import matplotlib.pyplot as plt

Ax = float(input("Entre com o valor da coordenada x do ponto A = "))
Ay = float(input("Entre com o valor da coordenada y do ponto A = "))
A = np.array([Ax, Ay])
#A = np.array([1, 0])



fig = plt.figure()
ax = fig.add_subplot()
ax.grid()

x = np.linspace(-1, 2)
ax.plot(x, x**2-x)

ax.plot(x, -x*(x-1))


def corDentro(A):
    x = A[0]
    y = A[1]
    
    
    y1 = x**2-x
    y2 = -x*(x-1)
    
    if x >= 0 and x <= 1:  #dentro
        if y >= y1 and y <= y2:
            return 'blue'
        
    return 'red'


ax.plot(A[0],A[1], 'o', color=corDentro(A))
