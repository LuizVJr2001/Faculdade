#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 13:46:26 2024

@author: luizdevjr
"""

#LENDO UM ARQUIVO

fl = open('./exemploArq.txt', 'r')  #Abre o arquivo no modo read

texto = fl.read()  #guarda a leitura na variavel texto

#for linha in fl:   # É possível printar linha por linha o arquivo de texto
 #   print(linha)

fl.close()  #fecha a abertura do arquivo


#ESCREVENDO NO ARQUIVO

import math as m

fl = open('exemploArq.txt', 'w') # abre em modo write
x = 3.
y = m.log(x)

fl.write(f'4, 3, {x:.1f}, {y:.4f}') #Isso sobreescreve o arquivo

fl.close()


#ADICIONANDO ESCRITA NO ARQUIVO

import math as m

fl = open('exemploArq2.txt', 'a') # abre em modo append
x = 3.
y = m.log(x)

fl.write(f'\n5, 3, {x:.1f}, {y:.4f}\n') #Isso sobreescreve o arquivo

fl.close()