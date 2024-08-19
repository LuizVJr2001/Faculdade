# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 13:52:42 2024

@author: F115
"""

import numpy as np
import numpy.linalg as npla

a = np.array([[1,2,3],[4,-5,6],[7,8,9]])

b = np.array([[-1,2],[4,-5]])


def mod(x):
    if x < 0:
        x = x*-1
    return x


def norma(arr):
    soma = 0
    
    for i in range(len(arr)):
        for j in range(arr[i].size):
            soma += mod(arr[i][j])

    return soma


#teste

print(norma(a))

'''
Avaliação - Nota: 2,5
'''

