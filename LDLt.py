import math
import funciones

def LDLt(A,B,n):
	Lt = [[0.0]*n]*n
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
	Lt = A
	L = funciones.transMatriz(Lt,n)
	D = [[float(i == j) for j in range(n)] for i in range(n)]
	for i in range(n):
		D[i][i] = float(L[i][i])
		for j in range(i+1):
			L[i][j] = L[i][j]/D[j][j]
	for i in range(n):
		for j in range(i,n):
			Lt[i][j] = Lt[i][j]/D[i][i]
	for i in range(n):
		D[i][i] = D[i][i]**2

	print "\n Resolucion por Algoritmo LDLt "
	print " -------------------------------------------------"
	print " Matriz L Triangular Inferior"
	funciones.imprimeMatriz(L)
	print " Matriz D Diagonal"
	funciones.imprimeMatriz(D)
	print " Matriz Lt Triangular Superior"
	funciones.imprimeMatriz(Lt)
	print "Para hallar el resultado de LDLt.x=b requerimos 3 ecuaciones:"
	z = funciones.solucionL(L,B,n) 		#Lz = b   "obtenemos z"
	y = funciones.solucionL(D,z,n)		#Dy = z   "obtenemos y"
	x = funciones.solucionU(Lt,y,n)		#Ltx = y  "obtenemos x"
	return z,y,x