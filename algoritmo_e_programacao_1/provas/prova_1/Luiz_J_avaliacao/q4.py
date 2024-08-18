# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 13:53:06 2024

@author: F115
"""

n = float(input("entre com n"))
k = float(input("entre com k"))

if n <= 0 or k > n:
    print("n precisa ser maior que 0 e K menor ou igual a n")

else:
    
    print( (n*(n-1)*(n-k+1))/(k*(k-1)*1) )

'''
Avaliação - Nota: 0.5
'''