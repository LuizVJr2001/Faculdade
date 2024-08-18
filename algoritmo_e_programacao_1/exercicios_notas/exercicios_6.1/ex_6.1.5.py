# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 15:15:21 2024

@author: luizd
"""

import numpy as np

A = np.array([[1,-1,2],[2,1,3],[-3,-1,-2]])

np.save("arquivos_txt/matriz_ex_6.1.5.npy", A)

matriz = np.load("arquivos_txt/matriz_ex_6.1.5.npy")

def traco(m):
    soma = 0
    for i in range(3):
        soma += m[i][i]
    
    return soma

print(f"traço da matriz 3x3 = {traco(matriz)}")