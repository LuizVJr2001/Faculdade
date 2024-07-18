# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 13:43:00 2024

@author: F115
"""


x = float(input("Entre com a coordenada x"))
y = float(input("Entre com a coordenada y"))

curvaY = (x-1)**3
curvaX = 1+(curvaY**(1/3))

retaY = x-1
retaX = retaY+1

dentroX = False
dentroY = False


if x >= 1 and y >= 0:
    if x <= curvaX and x >= retaX:
        dentroX = True
        if y <= retaY and y >= curvaY:
            dentroY = True
            print("O ponto está entro da área")
            
elif x < 1 and y < 0:
    if y >= retaY and y <= curvaY:
        dentroY = True
        if x <= retaX and x >= curvaX:
            dentroX = True



if not(dentroX and dentroY):
    print("Fora da área")
    
'''
Avaliação - Nota: 1.0
'''