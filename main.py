# -*- coding: utf-8 -*-

# Implementación de los tableros semánticos (tableaux)
# Input: cadena de la formula en notacion inorder
# Output: lista de listas de literales

# Importando la libreria tableaux
import tableaux as T

# Fórmula (en notación polaca inversa)
# para obtener uno de sus tableaux
formula = "pq>-rO"

# Se crea el tableau
ta = T.Tableaux(formula)

# Imprime el resultado en consola
if len(ta) == 0:
    print('La fórmula es insatisfacible')
else:
    print('La fórmula es satisfacible.')
    print('Las hojas abiertas del tableaux son:')
    for l in ta:
        print(T.imprime_hoja(l))


A = [T.Tree('b',None,None), T.Tree('-',None,T.Tree('a',None,None)), T.Tree('-',None,T.Tree('c',None,None)), T.Tree('a',None,None), T.Tree('d',None,None)]
#print(T.par_complementario(A))

B = [T.Tree('-',None,T.Tree('Z1',None,None)), T.Tree('S1',None,None), T.Tree('-',None,T.Tree('S10',None,None)), T.Tree('Z10',None,None)]
#print(T.par_complementario(B))

C = [T.Tree('-',None,T.Tree('q',None,None)), T.Tree('-',None,T.Tree('p',None,None)), T.Tree('q',None,None), T.Tree('-',None,T.Tree('r',None,None))]
#print(T.par_complementario(C))

D = [T.Tree('1',None,None), T.Tree('2',None,None), T.Tree('-',None,T.Tree('3',None,None)), T.Tree('1',None,None)]
#print(T.par_complementario(D))

E = T.Tree('-',None,T.Tree('p',None,None))
#print(T.es_literal(E))

F = T.Tree('p',None,None)
#print(T.es_literal(F))

G = T.Tree('-',None,T.Tree('Y',T.Tree('p',None,None),T.Tree('q',None,None)))
#print(T.es_literal(G))

H = T.Tree('O',T.Tree('k',None,None),T.Tree('Y',T.Tree('i',None,None),T.Tree('j',None,None)))
#print(T.es_literal(H))

I = [T.Tree('-',None,T.Tree('p',None,None)),T.Tree('p',None,None),T.Tree('-',None,T.Tree('q',None,None)),T.Tree('q',None,None)]
#print(T.no_literales(I))

J = [T.Tree('q',None,None),T.Tree('-',None,T.Tree('p',None,None)),T.Tree('-',None,T.Tree('-',None,T.Tree('p',None,None))),T.Tree('-',None,T.Tree('q',None,None))]
#print(T.no_literales(J))

K = [T.Tree('-',None,T.Tree('p',None,None)),T.Tree('q',None,None),T.Tree('-',None,T.Tree('p',None,None)),T.Tree('r',None,None),T.Tree('-',None,T.Tree('q',None,None)),T.Tree('p',None,None)]
#print(T.no_literales(K))

L = [T.Tree('p',None,None),T.Tree('q',None,None),T.Tree('O',T.Tree('p',None,None),T.Tree('q',None,None)),T.Tree('-',None,T.Tree('q',None,None)),T.Tree('-',None,T.Tree('p',None,None))]
#print(T.no_literales(L))



