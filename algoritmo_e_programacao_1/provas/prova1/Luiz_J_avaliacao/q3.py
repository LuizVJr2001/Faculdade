# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 13:46:11 2024

@author: F115
"""

n = int(input("Entre com o valor de n: "))

soma = 0

for i in range(1,n+1):
    soma += 1/(i*(i+1))
    
print(f"O resultado do somatório é {soma}")    

'''
Avaliação  Nota: 2.5
'''