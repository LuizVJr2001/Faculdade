# -*- coding: utf-8 -*-
"""
Created on Wed May  1 15:24:01 2024

@author: luizd
"""

u = [1, -1, 0]
v = [1, 0, 2]
w = [1, -1, 1]

prodmisto = (u[0]*v[1]*w[2] + u[1]*v[2]*w[0] + u[2]*v[0]*w[1] - u[2]*v[1]*w[0] - u[1]*v[0]*w[2] - u[0]*v[2]*w[1])

print(f"produto misto = {prodmisto}")