#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 14:48:01 2024

@author: luizdevjr
"""

import numpy as np

n = int(input("n = "))
m = int(input("m = "))
r = np.random.randint(1, n+m,(n,m))

def indmenor(arr):
    ind = 0
    valor = 0
    
    for i in range(len(arr)-1):
        
        for j in range(arr[i].size):
            