# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 19:53:57 2024

@author: luizd
"""

#Deve ser resolvido por pitágoras
    
def inDisk(*pts, a=0, b=0, r=1): #Oque o '*' faz?
  for pt in pts:
    if ((pt[0]-a)**2 + (pt[1]-b)**2 <= r**2):
      print(f'({pt[0]}, {pt[1]}) pertence ao disco.')
    else:
      print(f'({pt[0]}, {pt[1]}) não pertence ao disco.')    

lista = [1/2,1/2]

      
print(inDisk(lista))