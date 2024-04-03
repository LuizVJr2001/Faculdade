#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 19:44:58 2024

@author: luizdevjr
"""
import math as m

a = float(input("Entre com o valor de a: "))
b = float(input("Entre com o valor de b: "))
c = float(input("Entre com o valor de c: "))

delta = (b*b)-4*a*c


x1 = (-b+(m.sqrt(delta)))/(2*a)
x2 = (-b-(m.sqrt(delta)))/(2*a)

print(f'Raiz x1 = {x1}')
print(f'Raiz x2 = {x2}')
