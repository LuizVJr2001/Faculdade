#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 14:00:58 2024

@author: luizdevjr
"""
import numpy as np
import numpy.linalg as npla

v = np.array([4,3,5])
p = int(input("Entre com o valor de p: "))

def norma(v, p):
    soma = 0
    for i in range(v.size):
        soma = soma + (v[i])**p
    
    return np.float_power(soma,1/p)

print(norma(v, p))

print(npla.norm(v))