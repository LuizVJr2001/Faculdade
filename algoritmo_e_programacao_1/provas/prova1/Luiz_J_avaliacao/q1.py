# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 13:35:06 2024

@author: F115
"""

u = [-1, 1, -1]
v = [2, 1, -2]


prodInterno = u[0]*v[0] + u[1]*v[1] + u[2]*v[2]

norma = (v[0]**2 + v[1]**2 + v[2]**2)**0.5

vetorProjecaoEscalar = prodInterno/(norma**2)

projecaoDeUemV = [v[0]*vetorProjecaoEscalar, v[1]*vetorProjecaoEscalar, v[2]*vetorProjecaoEscalar]

'''
Avaliação - Nota: 2.4
'''