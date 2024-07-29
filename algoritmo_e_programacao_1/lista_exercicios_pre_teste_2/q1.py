#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 13:34:36 2024

@author: luizdevjr
"""

import numpy as np

n = int(input("n = "))

repete = n<1
while repete:
    n = int(input("n precisa ser >= 1 = "))
    repete = n<1    
    
r = np.random.randint(1, n, n)

lista = np.array([40, 5, 6, 10, 2])

#teste
print(np.argmax(r))

print(np.max(r))

def indMaior(lista):
    ind = 0
    valor = 0
    
    for i in range(lista.size-1):
        if lista[i] > valor:
            valor = lista[i]
            ind = i
    return ind            


def valMaior(arr):
    ind = 0
    valor = 0
    
    for i in range(arr.size-1):
        if arr[i] > valor:
            valor = arr[i]
            ind = i
    return valor

print(indMaior(r))
print(valMaior(r))