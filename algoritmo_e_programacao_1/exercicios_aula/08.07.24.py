#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 13:36:32 2024

@author: luizdevjr
"""

def fatores(n):
    L = []
    for i in range(2,n):
        edivisivel = True
        while edivisivel:
            if n%i == 0:
                L.append(i)
                n/=i
            else:
                edivisivel= False
    
    return L
    
def mmc(x, y):
    if x > y:
        x,y = y,x
    xL = fatores(x)
    yL = fatores(y)
    produto = 1
    for i in xL:
        if i in yL:
            pass
        else:
            yL.append(i)
    for i in yL:
        produto *= i
    return produto


def mdc(x,y):
    xL = fatores(x)
    yL = fatores(y)
    
    if x > y:
        maior, menor = x, y
    
    

#print(mmc(30,6))
#print(fatores(20))
#print(fatores(6))