# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 19:18:24 2024

@author: luizd
"""

"""
import matplotlib.pyplot as plt

fig = plt.figure()

ax = fig.add_subplot()

ax.plot([-0.5, 0, 1],[0.5, 0, 1])

plt.show()

"""
"""
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot()

x = np.linspace(-2, -0.5)
ax.plot(x, -(x+1)**2-2)

x = np.linspace(-0.5, 1)
ax.plot(x, np.fabs(x))

x = np.linspace(1, 3)
ax.plot(x, (x-2)**3+2)

plt.show()
"""

#===========================

"""
#Eixos

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot()

x = np.linspace(-2, -0.5)
ax.plot(x, -(x+1)**2-2)

x = np.linspace(-0.5, 1)
ax.plot(x, np.fabs(x))

x = np.linspace(1, 3)
ax.plot(x, (x-2)**3+2)

#Editando eixo-x
ax.set_xlim((-2.1, 3.1)) #Muda o crop horizontal do gráfico
ax. set_xticks([-2, -1, 0, 1, 2, 3]) # define as coordenadas do eixo x
ax.set_xlabel('eixo x') #Define um rótulo do eixo

#Colocando uma malha
ax.grid()

#Salvando as figuras
plt.savefig("figuras/fig_notas_6.2.png", bbox_inches='tight')
plt.savefig("figuras/fig_notas_6.2.pdf", bbox_inches='tight')

plt.show()
"""

#===========================

"""
#Elementos gráficos

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot()


# -2 <= x < -0.5
x = np.linspace(-2, -0.5)
f1= lambda x: -(x+1)**2-2

ax.plot(x, f1(x), color='blue', label = '-(x+1)**2-2')
ax.plot([-0.5], f1(-0.5), ls='', marker='o',
        markerfacecolor = 'white',
        markeredgecolor = 'blue') # Plota o ponto no final da curva


# -0.5 <= x < 1
x = np.linspace(-0.5,1)
f2 = lambda x: np.fabs(x)
ax.plot(x, f2(x), color = 'orange', label = '|x|')
ax.plot([-0.5], f2(-0.5), ls='', marker='o', color='orange') #Plota o ponto no inicio da reta

ax.plot([-0.5, -0.5],[f1(-0.5), f2(-0.5)], ls='--', color='gray', alpha=0.5) #Plota a linha pontilhada entre os dois pontos anteriores


# 1 <= x < 3

x = np.linspace(1,3)
f3 = lambda x: (x-2)**3+2
ax.plot(x, f3(x), color='green', label='(x-2)**3+2')
ax.plot(1., f3(1.), ls='', marker='o', color='green') #Plota o ponto na interseção entre as duas funções
ax.plot(3., f3(3.), ls='', marker='o', mfc='white', mec='green') #Plota o ponto no fim da função verde

#eixo x
ax.set_xlim((-2.1, 3.1))
ax.set_xticks([-2, -1, 0, 1, 2, 3])
ax.set_xlabel('eixo x')

#eixo y
ax.set_ylim(-3.1,3.1)
ax.set_yticks([-3,-2, -1, 0, 1, 2, 3])
ax.set_ylabel('eixo y')

#grid
ax.grid()
ax.legend() #Coloca a legenda das funções no gráfico (Mostra oque foi definido nas Labels)

#Salvando as figuras
plt.savefig("figuras/fig_notas_6.2-melhorado.png", bbox_inches='tight')
plt.savefig("figuras/fig_notas_6.2-melhorado.pdf", bbox_inches='tight')

"""

#===========================

















