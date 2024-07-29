# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 15:39:23 2024

@author: luizd

Desenvolva um código que computa e imprime a hipotenusa h 
de um triângulo retângulo com catetos a e b fornecidos por usuária(o).
"""

a = float(input("Entre com o valor do cateto a: "))
b = float(input("Entre com o valor do cateto b: "))

h = (a**2 + b**2)**0.5

print(f"O valor da hipotenusa h é: {h}")