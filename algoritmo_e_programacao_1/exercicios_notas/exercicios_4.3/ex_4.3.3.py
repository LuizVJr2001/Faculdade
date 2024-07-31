# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 18:41:39 2024

@author: luizd
"""

y = 1
def fun(x=y):
    y = 2
    print(x)
    
fun()

"""
A resposta seria 1, pois no parametro da função definimos x=y
porém como ainda não entramos no escopo da função a variavel y=1 ainda é acessível
portanto ao mandar printar x dentro da função estamos acessando a variavel y global, e não a variavel y interna da função


"""