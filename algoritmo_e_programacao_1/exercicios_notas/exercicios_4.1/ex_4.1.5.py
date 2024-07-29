# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 20:00:02 2024

@author: luizd
"""

import random

aleatorio = random.randint(0,51)

tentativa = 3

repete = True

while tentativa > 0:
    print(f"Você tem {tentativa} tentativas")
    chute = int(input("Adivinhe um número entre 0 e 51: "))

    if chute == aleatorio:
        print("Parabéns, você acertou!")
        break
    else:
        tentativa -= 1
        
        
if tentativa == 0:
    print(f"\n Você falhou, o número certo era: {aleatorio}")