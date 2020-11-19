#-*-coding: utf-8-*-
from random import choice
##############################################################################
# Variables globales
##############################################################################

# Crea las letras minúsculas a-z
letrasProposicionales = [chr(x) for x in range(97, 123)]
# inicializa la lista de interpretaciones
listaInterpsVerdaderas = []
# inicializa la lista de hojas
listaHojas = []

##############################################################################
# Definición de objeto tree y funciones de árboles
##############################################################################

class Tree(object):
	def __init__(self, label, left, right):
		self.left = left
		self.right = right
		self.label = label

def Inorder(f):
    # Imprime una formula como cadena dada una formula como arbol
    # Input: tree, que es una formula de logica proposicional
    # Output: string de la formula
	if f.right == None:
		return f.label
	elif f.label == '-':
		return f.label + Inorder(f.right)
	else:
		return "(" + Inorder(f.left) + f.label + Inorder(f.right) + ")"

def String2Tree(A, letrasProposicionales):
	# Crea una formula como tree dada una formula
	# como cadena escrita en notacion polaca inversa
	# Input: A, lista de caracteres con una formula escrita en notacion polaca inversa
	# letrasProposicionales, lista de letras proposicionales
	# Output: formula como tree
	conectivos = ['O', 'Y', '>']
	pila = []
	for c in A:
		if c in letrasProposicionales:
			pila.append(Tree(c, None, None))
		elif c == '-':
			formulaAux = Tree(c, None, pila[-1])
			del pila[-1]
			pila.append(formulaAux)
		elif c in conectivos:
			formulaAux = Tree(c, pila[-1], pila[-2])
			del pila[-1]
			del pila[-1]
			pila.append(formulaAux)
	return pila[-1]

##############################################################################
# Definición de funciones de tableaux
##############################################################################

def imprime_hoja(H):
	if H[0] != None:
		cadena = "{"
		primero = True
		for f in H:
			if primero == True:
				primero = False
			else:
				cadena += ", "
			cadena += Inorder(f)
		print(cadena + "}")
	else:
		cadena = "{"
		primero = True
		for f in H:
			if primero == True:
				primero = False
			else:
				cadena += ", "
			cadena += Inorder(f)
		print(cadena + "}")



def par_complementario(l):
	# Esta función determina si una lista de solo literales
	# contiene un par complementario
	# Input: l, una lista de literales
	# Output: True/False
	lista = []
	for item in l:
		if item.label == '-':
			lista.append('-' + item.right.label)
		else:
			lista.append(item.label)
	for elem in lista:
		if elem[0] == '-':
			complementario = elem[1]
			if complementario in lista:
				return True
			else:
				complementario = '-' + elem[0]
				if complementario in lista:
					return True
	return False

def es_literal(f):
	# Esta función determina si el árbol f es un literal
	# Input: f, una fórmula como árbol
	# Output: True/False
	if(f.label in ['Y','O']):
		return False
	elif(f.label == '-'):
		if(f.right.label not in ['Y','O','-']):
			return True
		else:
			return False
	else:
		return True

def no_literales(l):
	# Esta función determina si una lista de fórmulas contiene
	# solo literales
	# Input: l, una lista de fórmulas como árboles
	# Output: None/f, tal que f no es literal
	for formula in l:
		if (es_literal(formula)):
			continue
		else:
			return formula
	return None

def clasifica(l):
	# Esta función determina el conectivo que contiene la formula
	# Input: l, una lista de fórmulas como árboles
	# Output: La regla que aplica a la formula
	if l.label == '-':
		if l.right.label == '-':
			return "1alfa"
		elif l.right.label == 'Y':
			return "1beta"
		elif l.right.label == '>':
			return "4alfa"
		elif l.right.label == 'O':
			return "3alfa"
		else:
			return "None"

	elif l.label == 'Y':
		return "2alfa"
	elif l.label == 'O':
		return "2beta"
	elif l.label == '>':
		return "3beta"
	else:
		return None

def clasifica_y_extiende(f,h):
	# clasifica una fórmula como alfa o beta y extiende listaHojas
	# de acuerdo a la regla respectiva
	# Input: f, una fórmula como árbol
	# Output: no tiene output, pues modifica la variable global listaHojas
	global listaHojas

	print("Formula:", Inorder(f))
	print("Hoja:", imprime_hoja(h))

	assert(f in h), "La formula no esta en la lista!"

	clase = clasifica(f)
	print("Clasificada como:", clase)
	assert(clase != None), "Formula incorrecta " + imprime_hoja(h)

	if clase == '1alfa': #LISTO
		aux = [x for x in h]
		listaHojas.remove(h)
		aux.remove(f)
		aux += [f.right.right]
		listaHojas.append(aux)
	elif clase == '2alfa': #LISTO
		aux = [x for x in h]
		listaHojas.remove(h)
		aux.remove(f)
		aux += [f.right]
		aux += [f.left]
		listaHojas.append(aux)
	elif clase == '3alfa': #LISTO
		aux = [x for x in h]
		listaHojas.remove(h)
		aux.remove(f)
		aux += [Tree('-',None,f.right.right)]
		aux += [Tree('-',None,f.right.left)]
		listaHojas.append(aux)
	elif clase == '4alfa': #LISTO
		aux = [x for x in h]
		listaHojas.remove(h)
		aux.remove(f)
		aux += [Tree('-',None,f.right.right)]
		aux += [f.right.left]
		listaHojas.append(aux)
	elif clase == '1beta': #LISTO
		aux1 = [x for x in h]
		aux2 = [x for x in h]
		listaHojas.remove(h)
		aux1.remove(f)
		aux2.remove(f)
		aux1 += [Tree('-', None, f.right.right)]
		listaHojas.append(aux1)
		aux2 += [Tree('-',None,f.right.left)]
		listaHojas.append(aux2)
	elif clase == '2beta': #LISTO
		aux1 = [x for x in h]
		aux2 = [x for x in h]
		listaHojas.remove(h)
		aux1.remove(f)
		aux2.remove(f)
		aux1.append(f.right)
		listaHojas.append(aux1)
		aux2.append(f.left)
		listaHojas.append(aux2)
	elif clase == '3beta': #LISTO
		aux1 = [x for x in h]
		aux2 = [x for x in h]
		listaHojas.remove(h)
		aux1.remove(f)
		aux2.remove(f)
		aux1.append(f.right)
		listaHojas.append(aux1)
		aux2.append(Tree('-',None,f.left))
		listaHojas.append(aux2)


def Tableaux(f):

	# Algoritmo de creacion de tableau a partir de lista_hojas
	# Imput: - f, una fórmula como string en notación polaca inversa
	# Output: interpretaciones: lista de listas de literales que hacen
	#		 verdadera a f

	global listaHojas
	global listaInterpsVerdaderas

	A = String2Tree(f,let)
	print(u'La fórmula introducida es:\n', Inorder(A))

	listaHojas = [[A]]

	while (len(listaHojas) > 0):
		h = choice(listaHojas)
		print("Trabajando con hoja:\n", imprime_hoja(h))
		x = no_literales(h)
		if x == None:
			if par_complementario(h):
				listaHojas.remove(h)
			else:
				listaInterpsVerdaderas.append(h)
				listaHojas.remove(h)
		else:
			clasifica_y_extiende(x, h)

	return listaInterpsVerdaderas




let=['r','s','p','q']
# # f = String2Tree('prsYO-',let)
# #
# # h = [f, String2Tree('q',let), String2Tree('p',let)]
# #
# # listaHojas = [h]
# #
# # clasifica_y_extiende(f, h)
# #
# # imprime_hoja(listaHojas[0])
#
#
# f = String2Tree('qp>',let)
#
# h = [f, String2Tree('s-',let)]
#
# listaHojas = [h]
#
# clasifica_y_extiende(f, h)
#
# imprime_hoja(listaHojas[0])
# imprime_hoja(listaHojas[1])