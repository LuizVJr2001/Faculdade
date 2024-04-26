#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 14:40:10 2024

@author: luizdevjr
"""

#Testar se o ponto pertence a reta, ou se está acima ou abaixo da reta

# Y = AX+B
print('y = ax + b')

a = float(input('a = '))
b = float(input('b = '))


print('A = (a1, a2)')
a1 = float(input('a1 = '))
a2 = float(input('a2 = '))

#verificando
lhs = a*a1 + b

if(lhs == a2):
    print('A na reta')

elif (lhs > a2):
    print('A abaixo da reta')
    
else:
    print('A acima da reta')