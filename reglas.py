from codif import *

class Tree(object):
    def __init__(self, label, left, right):
        self.left = left
        self.right = right
        self.label = label

def String2Tree(A):
    Pila = []
    for c in A:
        if c in letrasProposicionales:
            Pila.append(Tree(c,None,None))
        elif c=='-':
            FormulaAux = Tree(c,None,Pila[-1])
            del Pila[-1]
            Pila.append(FormulaAux)
        elif c in Conectivos:
            FormulaAux = Tree(c,Pila[-1],Pila[-2])
            del Pila[-1]
            del Pila[-1]
            Pila.append(FormulaAux)
        else:
            print(u"Hay un problema: el símbolo " + str(c)+ " no se reconoce")
    return Pila[-1]

#Victoria Horizontal en O
def regla0():
    inicial = True
    for r in range(3):
        for c in range(3):
            if inicial:
                f1 = P(r,c,1,1)
                inicial = False
            else:
                f1 += P(r,c,1,1) 
    f2 = f1 + P(r,c,1,1) + 'Y' + 'O'
    return f2

#Victoria Horizontal en X
def regla1():
    inicial = True
    for r in range(3):
        for c in range(3):
            if inicial:
                f1 = P(r,c,2,1)
                inicial = False
            else:
                f1 += P(r,c,2,1)
    f2 = f1 + P(r,c,1,1) + 'Y' + 'O'
    return f2

#Victoria Vertical en O
def regla2():
    inicial = True
    for c in range(3):
        for r in range(3):
            if inicial:
                f1 = P(r,c,1,1)
                inicial = False
            else:
                f1 += P(r,c,1,1) 
    f2 = f1 + P(r,c,1,1) + 'Y' + 'O' 
    return f2

#Victoria Vertical en X
def regla3():
    inicial = True
    for c in range(3):
        for r in range(3):
            if inicial:
                f1 = P(r,c,2,1)
                inicial = False
            else:
                f1 += P(r,c,2,1) 
    f2 = f1  + P(r,c,2,1) +')'+ 'Y' + 'O'
    return f2
    
#Victoria Diagonal en O    
def regla4():
    inicial = True
    for r in range(3):
        for c in range(3):
            if r == c:
                if inicial:
                    f1 = P(r,c,1,t)
                    inicial = False
                else:
                    f1 += P(r,c,1,t)
    f2 = f1 + P(r,c,1,t) + 'Y'+'O'
    return f2

#Victoria Diagonal en X
def regla5():
    inicial = True
    for r in range(3):
        for c in range(3):
            if r == c:
                if inicial:
                    f1 = P(r,c,2,1)
                    inicial = False
                else:
                    f1 += P(r,c,2,1) 
    f2 = f1 + P(r,c,1,t) + 'Y'+'O'
    return f2
             
#Regla de Unicidad por Casilla
def regla6():
    inicial = True
    for r in range(3):
        for c in range(3):
            for v in range(3):
                #if inicial:
                    #f1 = P(r,c,v,1)
                    #inicial = False
                #else:
                    #f1 += P(r,c,v,1)

#Regla Tablero Lleno 
def regla7():
    placeholder

#Regla Evitar Victoria
def regla8():
    placeholder
