# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 14:13:36 2024

@author: F115
"""

import numpy as np

a = np.array([[1,2,3],[4,5,6]]) #deve retornar [[1,4],[2,5],[3,6]]

b = np.array([[1,2,3,9],[4,5,6,8]])

def transposta(arr):
    transp = []
    
    for i in range(len(arr)):
        for j in range(arr[i].size):
            try:
                x = [arr[i][j],arr[i+1][j]]
                transp.append(x)
            except:
                0
                
    return transp
    

#Funcionou apenas para array 2xn

print(transposta(b))

'''
Avaliação - Nota: 1,25
'''