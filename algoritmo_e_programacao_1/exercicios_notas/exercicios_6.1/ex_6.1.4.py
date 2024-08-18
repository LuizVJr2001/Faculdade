# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 14:32:22 2024

@author: luizd
"""

import numpy as np

fl = open("arquivos_txt/tabela_ex_6.1.4.txt", "r")

A = np.empty([3,3])

for i, linha in enumerate(fl):
    if (i >= 3):
            A[i-3] = (linha.split(","))
   
fl.close()

print(A)

def determinante(m):
    diagSoma = m[0][0]*m[1][1]*m[2][2] + m[0][1]*m[1][2]*m[2][0] + m[0][2]*m[1][0]*m[2][1]
    #print(diagSoma)
    diagSub = m[0][2]*m[1][1]*m[2][0] + m[1][2]*m[2][1]*m[0][0] + m[0][1]*m[1][0]*m[2][2]
    #print(diagSub)
    return diagSoma - diagSub

print(f'Determinante da matriz A = {determinante(A)}')
