# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 19:25:58 2024

@author: luizd
"""

def EhPrimo(x):
    Ehprimo = True
    if x == 1:
        return False
    
    for i in range(2,x):
        if x%i == 0:
            return False
    else:
        return True 

def Primos(n=1,m=29):
    if m < n:
        return print("m precisa ser maior ou igual a n")
    primos = []
    for i in range(n,m+1):
        if EhPrimo(i):
            primos.append(i)
    return primos

        


print(Primos(10, 50))