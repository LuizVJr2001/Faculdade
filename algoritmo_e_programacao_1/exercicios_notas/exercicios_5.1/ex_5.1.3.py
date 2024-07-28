#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 12:34:25 2024

@author: luizdevjr
"""

import numpy as np

v = np.array([5, 6 ,1 , 4, 4, 8 ,9 ,10, 15, 16, 12])

print(f"Array original = {v}")

print(f"Indices que ordenam o array com numpy.argsort = {np.argsort(v)}")

def argBubbleSort(arr):  #Função deve retornar uma lista com os indices que ordenam o array passado como parametro
     
    ind = [] 

    for i in range(1,arr.size):
        if arr[i] > arr[i-1]:
            print("maior")
            
        else:
            print("menor ou igual")





argBubbleSort(v)