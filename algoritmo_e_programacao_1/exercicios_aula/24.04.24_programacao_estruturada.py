#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 13:35:22 2024

@author: luizdevjr
"""

"""
Programação estruturada

- Sequencial
- Ramificação
- Repetição
"""

a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))

delta = b**2-4*a*c

#Ramificação
if (delta > 0.):

    x1 = (-b-delta**0.5)/(2*a)
    x2 = (-b+delta**0.5)/(2*a)

    print(f'x1 = {x1:.2e}')
    print(f'x2 = {x2:.2e}')

elif (delta == 0):
    #real dupla
    x = -b/(2*a)
    print(f'x = {x:.2e}')
    
else:
    #raizes complexas
    rea = -b/(2*a)
    img = (-delta)**0.5/(2*a)
    print(f'x1 = {rea:.2e} - {img:.2e}')
    print(f'x2 = {rea:.2e} + {img:.2e}')
    
print('fim')