# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 20:15:20 2024

@author: luizd
"""

a = float(input("Entre com o valor de a: "))
b = float(input("Entre com o valor de b: "))

def hip(a,b):
    return (a**2+b**2)**0.5


print(f"A hipotenusa c do triangulo retangulo abc é: {hip(a,b)}")