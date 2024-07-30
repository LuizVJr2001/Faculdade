# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 21:08:22 2024

@author: luizd
"""

def intercepta_y(a, b, c):
    
    
    return [0,c]


def raizes(a,b,c):
    x1 = (-b+(b**2-4*a*c)**0.5)/2*a
    x2 = (-b-(b**2-4*a*c)**0.5)/2*a
    
    return [0,x2], [0,x1]

def vertice(a,b,c):
    x0 = -b/(2*a)
    
    y0 = a*(x0**2)+b*x0+c
    
    
    return [x0,y0]


a = float(input("Entre com o valor de a: "))
b = float(input("Entre com o valor de b: "))
c = float(input("Entre com o valor de c: "))


print(f"Intercepta o eixo y em x={intercepta_y(a, b, c)}\n")

print(f"As raizes são {raizes(a, b, c)}\n")

print(f"O vertice fica em {vertice(a, b, c)}\n")