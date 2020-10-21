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

def StringtoTree(A):
    # Crea una formula como tree dada una formula como cadena escrita en notacion polaca inversa
    # Input: A, lista de caracteres con una formula escrita en notacion polaca inversa
             # letrasProposicionales, lista de letras proposicionales
    # Output: formula como tree

	# OJO: DEBE INCLUIR SU CÓDIGO DE STRING2TREE EN ESTA PARTE!!!!!

	p = letrasProposicionales[0] # ELIMINE ESTA LINEA LUEGO DE INCLUIR EL CODIGO DE STRING2TREE
	return Tree(p, None, None) # ELIMINE ESTA LINEA LUEGO DE INCLUIR EL CODIGO DE STRING2TREE

##############################################################################
# Definición de funciones de tableaux
##############################################################################

def imprime_hoja(H):
	cadena = "{"
	primero = True
	for f in H:
		if primero == True:
			primero = False
		else:
			cadena += ", "
		cadena += Inorder(f)
	return cadena + "}"

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
	return False

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

def clasifica_y_extiende(f):
	# clasifica una fórmula como alfa o beta y extiende listaHojas
	# de acuerdo a la regla respectiva
	# Input: f, una fórmula como árbol
	# Output: no tiene output, pues modifica la variable global listaHojas
	global listaHojas

def Tableaux(f):

	# Algoritmo de creacion de tableau a partir de lista_hojas
	# Imput: - f, una fórmula como string en notación polaca inversa
	# Output: interpretaciones: lista de listas de literales que hacen
	#		 verdadera a f
	global listaHojas
	global listaInterpsVerdaderas

	A = string2Tree(f)
	listaHojas = [[A]]

	return listaInterpsVerdaderas
