# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 19:20:55 2024

@author: luizd
"""

import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) # 3x3 (n x m)

x = np.array([1, 2, 3]) # 3x1 (m x 1)


def produto(a, x):
    nA = len(a)
    mA = len(a[0])
    mX = len(x)
    AX = np.empty(x.shape)
    if mA != mX:
        return print("Dimensões incorretas!")

    for n in range(nA):
        soma = 0
        for m in range(mA):
            soma += a[n][m]*x[m]
        
        AX[n] = soma
            
    return AX
            

print(produto(a, x))


#Testando

'''
M = np.random.randint(1, 10,(3,3))

v = np.random.randint(1, 10, 3)

print(produto(M,v))

print(f'\n Deve ser igual a \n\n {M@v}')

'''