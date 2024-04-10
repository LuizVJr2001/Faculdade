#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 13:52:34 2024

@author: luizdevjr
"""

# Referente a notas 2.4 de algoritmos e programação do notaspedrok

#Forma de realizar permutação usando buffer (terceira variavel)
x = 1
y = 2
z = y
y = x
x = z

print(f'x= {x}  y = {y}')


# Forma de realizar troca de variáveis em python de forma simples

a = 3
b = 5

[a, b] = [b, a]
print(f'a= {a}  b = {b}')

# Teste de precedencias em cálculo do python

c = 2+8*3/2**2-1

print(c)

import sys
print(sys.getsizeof(10**10))


# Limitação de números floats no computador

print(f'{1.4:.25e}')

# Número complexo no computador (1j)
