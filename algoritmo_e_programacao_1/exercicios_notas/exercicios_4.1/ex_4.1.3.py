# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 15:53:44 2024

@author: luizd
"""

import math as m

a = float(input("Entre com o valor de a: "))
b = float(input("Entre com o valor de b: "))
c = float(input("Entre com o valor de c: "))

angA = m.acos((a**2-b**2-c**2)/(-2*b*c))
h = m.sin(angA)*b

print(f"A altura h do triangulo abc é de aproximadamente: {h}")