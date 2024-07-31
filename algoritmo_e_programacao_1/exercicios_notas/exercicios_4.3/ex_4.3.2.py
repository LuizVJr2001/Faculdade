# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 18:40:04 2024

@author: luizd
"""

def fun(x):
    global x
    x = x-1
    
    
"""
o Nome "x" é tanto parametro da função fun, quanto 
uma variavel global (sendo acessada de dentro da função)

"""