# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 12:34:28 2024

@author: luizd
"""
import numpy as np

fl = open('arquivos_txt/tabela_ex_6.1.2.txt', 'w')

xx = np.array([np.pi/6, np.pi/4, np.pi/3])

fl.write("theta, sin(theta), cos(theta) \n")
fl.write("0, 0, 1 \n")

for i, x in enumerate(xx):
    fl.write(f'{x} , {np.sin(x)} , {np.cos(x)} \n')

fl.write(f"{np.pi/2}, 1, 0 \n")


fl.close()