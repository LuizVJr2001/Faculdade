#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 17:49:09 2024

@author: luizdevjr
"""

import math as m

h = float(input('Entre com o valor da hipotenusa do triangulo retangulo: '))
l = float(input('Entre com o valor do lado l: '))

h2 = h**2
l2 = l**2

b = m.sqrt(h2 - l2)
a= m.floor((b*l)/2)

print(f'O valor da Área do Triangulo Retangulo é = {a}')