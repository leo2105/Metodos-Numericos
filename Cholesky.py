import math
import funciones

def metodoCholesky(A,B,n):
	#creamos matriz nula G
	G = [[0.0]*n]*n
	#creamos matriz nula G_T
	for i in range(n):
		suma = A[i][i]
		for k in range(i):
			suma = suma - A[k][i]**2
		if suma < 0: #no es definida positiva
			return ["NULL","NULL"]
		A[i][i] = math.sqrt(suma)
		for j in range(i+1, n):
			suma = A[i][j]
			for k in range(i):
				suma = suma - A[k][i]*A[k][j]
			A[i][j] = suma / A[i][i]

	for j in range(n):
		for i in range(n):
			if(i > j):
				A[i][j] = 0.0
	G = A
	Gt = funciones.transMatriz(G,n)

	print "\n Resolucion por Algoritmo Cholesky "
	print " -------------------------------------------------"
	print "\n Matriz G Triangular Superior"
	funciones.imprimeMatriz(G)
	print "\n Matriz Gt Triangular Inferior"
	funciones.imprimeMatriz(Gt)

	y = funciones.solucionL(Gt,B,n)	#Ly = b  "obtenemos y"
	x = funciones.solucionU(G,y,n)	#Ux = y  "obtenemos x"

	return [y,x]