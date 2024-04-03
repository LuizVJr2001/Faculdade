#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 13:52:34 2024

@author: luizdevjr
"""

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