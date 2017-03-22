import funciones

def metodoL1U(A,b,n):
	L = []
	for i in range(n):
		L.append( [0]*n)
	U = []
	for i in range(n):
		U.append( [0]*n)
	#pivot
	a = funciones.matrizAumentada(A,b,n)
	for j in range(n):
		a = funciones.pivot(a, j)
	A = []
	b = []
	for i in range(n):
		A.append(a[i][0:n])
		b.append(a[i][n])
	#L1U
	for j in range(0,n):
		L[j][j] = 1.0
		for i in range(j,n):
			U[j][i] = A[j][i] - funciones.suma(U,L,j,i,j)
		for i in range(j+1,n):
			if U[j][j]==0:
				return ["NULL","NULL"]
			L[i][j] = (A[i][j] - funciones.suma(U,L,i,j,j))/U[j][j]

	print "\n Resolucion por Algoritmo L1U-Crout "
	print " -------------------------------------------------"
	print "\n Matriz U Triangular Superior"
	funciones.imprimeMatriz(U)
	print "\n Matriz L Triangular Inferior"
	funciones.imprimeMatriz(L)

	y = funciones.solucionL(L,b,n)	#Ly = b  "obtenemos y"
	x = funciones.solucionU(U,y,n)	#Ux = y  "obtenemos x"
	return [y,x]