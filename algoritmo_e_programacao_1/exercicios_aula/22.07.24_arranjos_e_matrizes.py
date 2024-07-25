#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 13:48:52 2024

@author: luizdevjr
"""

v = [1, -3, 5]  #Lista
w = [2, -1, 4]  #Lista

#Lista não serve para soma simples de vetores
#Existe um pacote para computação matricial, chamado numpy, nele existe o método array.

import numpy as np

v = np.array([1, -3, 5])
w = np.array([2, -1, 4])
u = np.array([0 , np.pi/6, np.pi/4, np.pi/3, np.pi/2]) #A biblioteca math não permite cálculos trigonométricos com arrays com mais de dois itens

print(v+w)

print(2*v)

print(v*w)

print(v/w)

print(w**2)

print(np.sin(u))

#métodos da biblioteca numpy

a = np.zeros(5)
b = np.empty(5)
c = np.linspace(0., 1., 5) # usado bastante para criar malhas uniformes
d = np.arange(0., 1.1, 0.25)

print(a)
print(b)
print(c)
print(d)

# v.size retorna o tamanho sem fazer operação para pegar o tamanho.

def bolha(v):
    for i in range(v.size-1):
        alterado = False
        for j in range(v.size-i-1):
            if (v[j] > v[j+1]):
                v[j+1], v[j] = v[j], v[j+1]
                alterado = True
        if not(alterado):
            break
    return v


print(bolha(w))

#ou

print(np.sort(w)) #O método já existe na biblioteca numpy


#Produto interno e Produto Vetorial

def prodIn(v,w):
    d = 0.
    
    for i in range(v.size):
        d+= v[i]*w[i]
    return d

v = np.array([1., 0, -2])
w = np.array([2., -1, 3])


print(prodIn(v, w))
#ou
print(np.dot(v,w))

#Norma

def norma(u):
    return np.sqrt(prodIn(u,u))

print(norma(v))    

#sub modo da biblioteca numpy

import numpy.linalg as npla

print(npla.norm(v))


#Produto vetorial (com matrizes)


