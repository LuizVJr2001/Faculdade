# -*- coding: utf-8 -*-
"""
Created on Wed May  1 15:39:55 2024

@author: luizd
"""

n = int(input('Informe o número de termos: '))
a = float(input('Informe o fator: '))

repete = not(n > 0) or (a == 1)

if repete:
    n = int(input('Informe o número de termos(precisa ser um valor inteiro maior que 0): '))
    a = float(input('Informe o fator(precisa ser um valor diferente de 1): '))

soma = 0

for i in range(n):
    soma += i*a**i
    
    
print(f'somatorio = {soma}')