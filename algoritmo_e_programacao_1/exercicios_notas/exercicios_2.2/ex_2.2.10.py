#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 20:11:39 2024

@author: luizdevjr
"""

n = int(input('entre com o valor de n= '))

fat = 1

for i in range(1, n+1):
    fat = fat*i
    
print(fat)

#corrigir