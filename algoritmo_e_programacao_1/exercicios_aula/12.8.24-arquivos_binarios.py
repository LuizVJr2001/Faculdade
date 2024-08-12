#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 14:33:31 2024

@author: luizdevjr
"""

#CRIANDO O ARQUIVO BINARIO

import numpy as np

x = np.linspace(0.1, 5, 10)

#print(f'{x[2]:.15f}')


#np.save('x.npy', x)  #Guarda os arranjo em um arquivo em formato binario

#LENDO O ARQUIVO BINARIO

x2 = np.load('x.npy')
print(x2)