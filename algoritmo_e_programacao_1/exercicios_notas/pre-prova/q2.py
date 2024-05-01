# -*- coding: utf-8 -*-
"""
Created on Wed May  1 15:26:29 2024

@author: luizd
"""
print('Informa a posição do ponto A=(a1,a2) em relação à função quadrática p(x) = x² + x - 2')

a1 = float(input("Entre com o valor de a1: "))
a2 = float(input("Entre com o valor de a2: "))

p = a1**2 + a1 - 2

# testa se o ponto está acima do grafico
acima = (a2 > p)

# testa se o ponto está abaixo do grafico
abaixo = (a2 < p)

if acima:
    print(f'O ponto A está acima do gráfico y= x² + x - 2, no ponto x = {a1}')
    
elif abaixo:
    print(f'O ponto A está abaixo do gráfico y= x² + x - 2, no ponto x = {a1}')
    
else: 
    print(f'O ponto A pertence ao gráfico y= x² + x - 2, no ponto x = {a1}')