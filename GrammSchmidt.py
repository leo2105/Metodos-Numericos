import math
import funciones

def metodoGramm(A,b,n):
	#La matriz A es mxn por tanto la matriz E sera de orden mxn y U nxn
	#Creamos matriz E
	E = []
	for i in range(n):
		E.append([0]*n)
	#Creamos matriz U
	U = []
	for i in range(n):
		U.append([0]*n)
	
	#Algoritmo
	for j in range(n):
		for k in range(n):
			E[k][j] = A[k][j]
		for i in range(j):
			U[i][j] = funciones.productoGramm(E,n,i,j)
			for k in range(n):
				E[k][j] = E[k][j] - U[i][j]*E[k][i]
		U[j][j] = math.sqrt(funciones.sumaGramm(E,n,j))
		for k in range(n):
			E[k][j] = E[k][j]/U[j][j]
	y = funciones.solGramm(E,b,n)
	x = funciones.solGramm(U,y,n)
	print "\n Resolucion por Algoritmo de Gramm Schmidt "
	print " -------------------------------------------------"
	print " Matriz E(Q):"
	funciones.imprimeMatriz(E)
	print " Matriz U(R):"
	funciones.imprimeMatriz(U)
	return y,x
