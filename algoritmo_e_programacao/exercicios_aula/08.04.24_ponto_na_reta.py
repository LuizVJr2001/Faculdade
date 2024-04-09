#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 14:06:42 2024

@author: luizdevjr
"""

# 1) entrar com o valor de a
# 2) entrar com o valor de b
# 3) entrar com o valor de x
# 4) entrar com o valor de y
# 5) verificar se o ponto está na reta (a*x+b=y)
# 6) imprimir se o ponto etá na reta
# 7) verificar se o ponto está acima da reta (se o y da reta é menor que o y do ponto)
# 8) verificar se o ponto está abaixo da reta ( se o y da reta é maior que o y do ponto)


a = float(input("Entre com o valor de a: "))
b = float(input("Entre com o valor de b: "))

x = float(input("Entre com o valor de x: "))
y = float(input("Entre com o valor de y: "))

yReta = (a*x+b)
resp = (yReta == y)


print('(x,y) está na reta:?')
print(resp)

if resp:
    print('O ponto pertence a reta')
    
else:
    if yReta < y:
        print('O ponto está acima da reta')
        
    else:
        print('O ponto está abaixo da reta')