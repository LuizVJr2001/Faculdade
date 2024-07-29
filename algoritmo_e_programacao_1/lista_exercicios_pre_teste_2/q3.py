#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 14:48:01 2024

@author: luizdevjr
"""

import numpy as np

n = int(input("n = ")) # qntd de termos do array principal
m = int(input("m = ")) # qntd de termos dos arrays internos
r = np.random.randint(1, n+m,(n,m))


def indMenor(arr):
    ind = []
    valor = n+m
    
    for i in range(len(arr)-1): # termo do array principal
        
        for j in range(arr[i].size): # termo do array interno
            if arr[i][j] < valor:
                    valor = arr[i][j]
                    ind = [i, j]
    return ind[0]*m + ind[1]

def valMenor(arr):
    ind = []
    valor = n+m
    
    for i in range(len(arr)-1): # termo do array principal
        
        for j in range(arr[i].size): # termo do array interno
            if arr[i][j] < valor:
                    valor = arr[i][j]
                    ind = [i, j]
    return valor


print(indMenor(r))


print(valMenor(r))

print(f"comparar com {np.argmin(r)}")
print(f"comparar com {np.min(r)}")