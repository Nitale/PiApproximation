# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""
import math
import matplotlib.pyplot as plt

def SerieInvCarres(n, parity):
    result = 0
    if not parity:
        for i in range (1, n):
            result += 1/i**2
        return result
    else:
        for i in range (1, n, 2):
            result += 1/i**2
        return result

def MethodeSerieInvCarres(n):
    return math.sqrt(SerieInvCarres(n, 0)*6)

def MethodeSerieInvCarresImparis(n):
    return math.sqrt(SerieInvCarres(n, 1)*8)

def GraphMethodes(begin, end):
    y1=[]
    y2=[]
    x=[]
    for i in range (begin, end):
        x.append(i)
        y1.append(math.pi - MethodeSerieInvCarres(i))
        y2.append(math.pi - MethodeSerieInvCarresImparis(i))
    plt.plot(x, y1, label="Série Inverse Carrés")
    plt.plot(x, y2, label="Série Inverse Carrés Impaires")
    plt.legend()
    plt.xlim(begin, end)
    plt.ylim(0, 0.001)
    plt.show()

def MethodeSerieRamanujan(n):
    result = 0
    for i in range(0,n):
        result += ((math.factorial(4*i))/(math.factorial(i)**4))*((1103+26390*i)/((4*99)**(4*i)))
    return 1/(result*((2*math.sqrt(2))/(9801)))

    