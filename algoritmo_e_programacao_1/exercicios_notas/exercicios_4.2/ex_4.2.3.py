# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 20:39:28 2024

@author: luizd
"""
import random


def imparAleat():
    repete = True
    while repete:
        x = random.randint(0, 51)

        if x%2 == 0:
            repete = True
        else:
            return x

print(imparAleat())