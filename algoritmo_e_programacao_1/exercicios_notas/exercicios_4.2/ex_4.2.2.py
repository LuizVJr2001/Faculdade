# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 20:20:25 2024

@author: luizd
"""

import math as m

def area(a, b, c):
    p = (a+b+c)/2
    return (p*(p-a)*(p-b)*(p-c))**0.5

a = float(input("Entre com o valor de a: "))
b = float(input("Entre com o valor de b: "))
c = float(input("Entre com o valor de c: "))


print(area(a,b,c))