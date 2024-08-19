# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 13:34:17 2024

@author: F115
"""

import numpy as np
n = int(input("n = "))
r = np.random.randint(1, n+1, n)

while n<1:
    n = int(input("n precisa ser maior ou igual a 1: n = "))

def menor(arr, n=n):
    indice = 0
    valor = n+1
    
    for i in range(arr.size):
        if arr[i] < valor:
            valor = arr[i]
            indice = i
    return valor,indice


print(menor(r))

'''
Avaliação - Nota: 1,25
Obs.: Não verificou a paridade.1,
'''