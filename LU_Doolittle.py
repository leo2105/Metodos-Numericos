import funciones

def metodoDoolittle(A, B, n):

	U = [[0.0]*n for j in range(n)]
	L = [[float(i == j) for j in range(n)] for i in range(n)]
	
	a = funciones.matrizAumentada(A,B,n)
	for j in range(n):
		a = funciones.pivot(a, j)
	A = []
	B = []
	for i in range(n):
		A.append(a[i][0:n])
		B.append(a[i][n])

	for k in range(n):
		for i in range(k+1):
			U[i][k] = A[i][k] - sum(L[i][p]*U[p][k] for p in range(i))
		for i in range(k+1, n):
			if U[k][k] == 0:
				return L,U,["NULL","NULL"]
			L[i][k] = (A[i][k] - sum(L[i][p]*U[p][k] for p in range(k))) / float(U[k][k])
	
	print "\n Resolucion por Algoritmo LU-Doolittle "
	print " -------------------------------------------------"
	print "\n Matriz U Triangular Superior"
	funciones.imprimeMatriz(U)
	print "\n Matriz L Triangular Inferior"
	funciones.imprimeMatriz(L)

	y = funciones.solucionL(L,B,n)	#Ly = b  "obtenemos y"
	x = funciones.solucionU(U,y,n)	#Ux = y  "obtenemos x"

	return [y,x]