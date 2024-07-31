# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 19:17:18 2024

@author: luizd
"""

def listaTermosPA(a0, r, n=5):
    lista = []
    
    for i in range(n+1):
        lista.append(a0 + i*r)
    
    return lista


print(listaTermosPA(1, 5))