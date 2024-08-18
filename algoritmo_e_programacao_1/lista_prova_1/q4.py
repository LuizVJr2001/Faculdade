# -*- coding: utf-8 -*-
"""
Created on Wed May  1 16:02:34 2024

@author: luizd
"""

n = int(input('Informe o número de termos: '))
x = float(input('Informe o fator: '))

repete = not(n > 0)

if repete:
    n = int(input('Informe o número de termos(precisa ser um valor inteiro maior que 0): '))

prod = 1

for i in range(n):
    prod *= (x + i + 1)
    print(prod)
    
print(f'produtorio = {prod}')