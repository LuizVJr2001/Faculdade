#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 14:09:46 2024

@author: luizdevjr
"""
import numpy as np

def ordenaIndDec(u):
    n = len(u)
    ind = np.arange(n)
    for k in range(n-1):
        noUpdated = True
        for i in range(n-k-1):
            if (u[ind[i]] < u[ind[i+1]]):
                ind[i], ind[i+1] = ind[i+1], ind[i]
                noUpdated = False
        if (noUpdated):
            break
    return ind

n = int(input("Entre com o valor de n natural: "))
while n <= 0:
    n = int(input("Entre com o valor de n natural: "))
    
u = np.random.rand(n)


print(u)


uOrden = ordenaIndDec(u)
print(uOrden)


def ordenaDec(u, index):
    array = []

    for i in index:    
        array.append(u[i])
        
    return array




listaOrdenada = ordenaDec(u, uOrden)
        
print(listaOrdenada)
        


fl = open('lista_dados_Q1.txt','a')

fl.write('\n Nova entrada de dados\n \n')

for i in range(len(listaOrdenada)):
    fl.write(f'{listaOrdenada[i]} \n')
    
fl.close()
        
print("Os dados foram adicionados no arquivo 'lista_dados_Q1.txt'")
        
        
        
        
    