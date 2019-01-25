# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""
import math
import matplotlib.pyplot as plt

    # return the result of the 1/n**2 sum from 1 to n
        # parity (boolean : 0 -> false ; 1 -> true) : Take only pair elements of the sum if true
def SerieInvCarres(n, parity):
    result = 0
    if not parity:
        for i in range (1, n+1):
            result += 1/i**2
        return result
    else:
        for i in range (1, n+1, 2):
            result += 1/i**2
        return result

def MethodeSerieInvCarres(n):
    return math.sqrt(SerieInvCarres(n, 0)*6)

def MethodeSerieInvCarresImparis(n):
    return math.sqrt(SerieInvCarres(n, 1)*8)

    # Shows the precision for the estimation of the 2 series
        # Shows the graph from begin to end (first value from last value)
def GraphMethodes(begin, end):
    y1=[]
    y2=[]
    x=[]
    for i in range (begin, end + 1):
        x.append(i)
        y1.append(math.pi - MethodeSerieInvCarres(i))
        y2.append(math.pi - MethodeSerieInvCarresImparis(i))
    plt.plot(x, y1, label="Série Inverse Carrés")
    plt.plot(x, y2, label="Série Inverse Carrés Impaires")
    plt.legend()
    plt.xlim(begin, end)
    plt.ylim(0, 0.05)
    plt.show()
    
    # Estimating Pi by Ramanujan's method
def MethodeSerieRamanujan(n):
    result = 0
    for i in range(0,n+1):
        result += ((math.factorial(4*i))/(math.factorial(i)**4))*((1103+26390*i)/((4*99)**(4*i)))
    return 1/(result*((2*math.sqrt(2))/(9801)))

    # Determine how many elecments you need to reach eps
        # eps (Epsilonn) : The precision that you need to reach
def PrecisionSerieInvCarres(eps):
    n = 1
    while (math.pi - MethodeSerieInvCarres(n) > eps):
        n += 1
    return n

    # Determine how many elecments you need to reach eps
        # eps (Epsilonn) : The precision that you need to reach
def PrecisionSerieInvCarresImparis(eps):
    n = 1
    while (math.pi - MethodeSerieInvCarresImparis(n) > eps):
        n += 1
    return n
        

    