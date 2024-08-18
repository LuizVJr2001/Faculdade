# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 00:09:31 2024

@author: luizd
"""

doc = open("arquivos_txt/ex_6.1.1-foo.txt","r")

saida = open("arquivos_txt/ex_6.1.1-novo.txt", "w")


for i, linha in enumerate(doc):
    if (i != 8):
        saida.write(linha)

saida.close()
doc.close()