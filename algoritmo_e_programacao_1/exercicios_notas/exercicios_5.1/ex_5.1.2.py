#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 12:24:52 2024

@author: luizdevjr
"""

import numpy as np

v = np.array([4, -1, 1, -2, 3])

a = v[1]
b = v[1:4]
c = v[:3]
d = v[1:]
e = v[1:4:2]
f = v[-2:-5:-1]
g = v[::-2] # não especifíca onde começa o array, apenas passa que os passos será de 2 em 2 no sentido negativo. Portanto, ele começa no final do array até chegar no inicio


print(f" a = {a} ")
print(f" b = {b} ")
print(f" c = {c} ")
print(f" d = {d} ")
print(f" e = {e} ")
print(f" f = {f} ")
print(f" g = {g} ")