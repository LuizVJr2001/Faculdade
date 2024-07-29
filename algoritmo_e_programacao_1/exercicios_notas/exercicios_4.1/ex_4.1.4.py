# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 16:03:53 2024

@author: luizd
"""
import math as m

def graupRad(x):
    return x*(m.pi/180)


theta = float(input("Entre com o valor do angulo theta: "))

thetaRad = graupRad(theta)



print(f"Sen(theta) = {m.sin(thetaRad)}")
print(f"Cos(theta) = {m.cos(thetaRad)}")

print("\n Para valores múltiplos de (pi ou 90°), os valores de sen ou cos que deveriam ser igual a 0, estarão errados!")
