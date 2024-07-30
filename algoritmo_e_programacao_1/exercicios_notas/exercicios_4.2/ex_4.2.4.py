# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 20:56:05 2024

@author: luizd
"""

a = float(input("Entre com o valor de a: "))
b = float(input("Entre com o valor de b: "))

def raizFuncaoAfim(a,b):
    
    try:
        x = -b/a
    except:
        return print("'a' precisa ser diferente de 0 ")
    return x
    
print(raizFuncaoAfim(a, b))