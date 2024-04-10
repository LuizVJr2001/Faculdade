#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 11:14:34 2024

@author: luizdevjr
"""


a = bool(int(input("Entre com o valor de a: 1 para True e 0 para False ")))

b = bool(int(input("Entre com o valor de b: 1 para True e 0 para False ")))

xor = not(a and b) and (a or b)

print(f"xor = {xor}")