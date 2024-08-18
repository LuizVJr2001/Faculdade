# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 14:09:25 2024

@author: luizd
"""
import pickle

dicionario = {}

#Pegando lista do exercicio anterior

fl = open("arquivos_txt/tabela_ex_6.1.2.txt", 'r')

for i, linha in enumerate(fl):
    dicionario[i] = [linha]
    
fl.close()

#Criando arquivo binário

flb = open("arquivos_txt/tabela_ex_6.1.3.bin", "wb")

pickle.dump(dicionario, flb)

flb.close()


#Lendo arquivo binário

flb2 = open("arquivos_txt/tabela_ex_6.1.3.bin", "rb")

data = pickle.load(flb2)

flb2.close()

print(data)