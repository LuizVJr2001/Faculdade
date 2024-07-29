# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 15:45:39 2024

@author: luizd

Desenvolva um código que verifica e informa a existência 
de um triângulo de lados fornecidos por usuária(o).
"""

a = float(input("Entre com o valor de a: "))
b = float(input("Entre com o valor de b: "))
c = float(input("Entre com o valor de c: "))

if abs(b-c) < a < (b+c):
    print("O triangulo existe")
else:
    print("Não há triangulo")    