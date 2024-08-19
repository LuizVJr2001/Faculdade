# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 13:46:58 2024

@author: F115
"""

import numpy as np
import numpy.linalg as npla


r = np.array([0.,1,5,6,4,8,9,2,4,8,300,100, 250])

def maximo(arr):
    valor = 0
    for i in range(arr.size):
        if arr[i]>valor: #faltou verificar o valor abs
            valor = arr[i]
    return valor

#teste

print(npla.norm(r,np.inf))

print(maximo(r))

'''
Avaliação - Nota: 2,0
'''