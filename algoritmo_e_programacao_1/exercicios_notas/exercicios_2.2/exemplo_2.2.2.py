#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 17:17:46 2024

@author: luizdevjr
"""

x = float(input('entre com o valor de x:'))
if (x >= 0):
    s = x/2
    for i in range(4):
        s = (s + x/s)/2
    print(f'Raiz aprox. de  x = {s}')
else:
    print(f'Não existe!')