#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 20:05:53 2024

@author: luizdevjr
"""

n = int(input('entre com o valor de n= '))

s = 1

for i in range(1, n+1):
    s += 1/(i)

print(s)