import funciones

def metodoLU1(A,B,n):
	L = []
	for i in range(n):
		L.append( [0]*n)
	U = []
	for i in range(n):
		U.append( [0]*n)
	#pivot
	a = funciones.matrizAumentada(A,B,n)
	for j in range(n):
		a = funciones.pivot(a, j)
	A = []
	B = []
	for i in range(n):
		A.append(a[i][0:n])
		B.append(a[i][n])
	#LU1
	for j in range(0,n):
		U[j][j] = 1.0
		for i in range(j,n):
			L[i][j] = A[i][j] - funciones.suma(U,L,i,j,j)#ultima j por i
		for i in range(j+1,n):
			if L[j][j] == 0:
				return ["NULL","NULL"]
			U[j][i] = (A[j][i] - funciones.suma(U,L,j,i,j))/L[j][j]
	
	print "\n Resolucion por Algoritmo LU1-Crout "
	print " -------------------------------------------------"
	print "\n Matriz U Triangular Superior"
	funciones.imprimeMatriz(U)
	print "\n Matriz L Triangular Inferior"
	funciones.imprimeMatriz(L)

	y = funciones.solucionL(L,B,n)	#Ly = b  "obtenemos y"
	x = funciones.solucionU(U,y,n)	#Ux = y  "obtenemos x"

	return [y,x]