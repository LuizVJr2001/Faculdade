# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 19:13:14 2024

@author: luizd
"""

import numpy as np
import numpy.linalg as npAlg

a = np.array([[1,5,7],[8,5,2]])

#a = np.array([[3,3,3],[3,3,3]])
#testando o valor correto

print(npAlg.norm(a))


def normaL2(arr):
    soma = 0
    for i in range(len(arr)):
        for j in range(arr[i].size):
            soma += arr[i][j]**2
            
    return soma**0.5
        

print(normaL2(a))