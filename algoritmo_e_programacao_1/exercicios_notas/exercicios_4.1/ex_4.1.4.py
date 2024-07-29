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

if theta == 90:
    print(f"Sen(theta) = {m.sin(thetaRad)}")
    print("Cos(theta) = 0")
    
elif theta == 180:
    print("Sen(theta) = 0")
    print(f"Cos(theta) = {m.cos(thetaRad)}")
    
elif theta == 270:
    print("Sen(theta) = {m.sin(thetaRad)}")
    print(f"Cos(theta) = {m.cos(thetaRad)}")    
    
    
    
    

"""
print(f"Sen(theta) = {m.sin(thetaRad)}")
print(f"Cos(theta) = {m.cos(thetaRad)}")
"""