import funciones

def LDMt(A, B, n):
	L = []
	for i in range(n):
		L.append( [0]*n)
	Mt = []
	for i in range(n):
		Mt.append( [0]*n)
	#pivot
	a = funciones.matrizAumentada(A,B,n)
	for j in range(n):
		a = funciones.pivot(a, j)
	A = []
	B = []
	for i in range(n):
		A.append(a[i][0:n])
		B.append(a[i][n])
	for j in range(0,n):
		Mt[j][j] = 1.0
		for i in range(j,n):
			L[i][j] = A[i][j] - funciones.suma(Mt,L,i,j,j)#ultima j por i
		for i in range(j+1,n):
			if L[j][j] == 0:
				return ["NULL","NULL","NULL"]
			Mt[j][i] = (A[j][i] - funciones.suma(Mt,L,j,i,j))/L[j][j]

	D = [[float(i == j) for j in range(n)] for i in range(n)]
	for i in range(n):
		D[i][i] = float(L[i][i])
		for j in range(i+1):
			L[i][j] = L[i][j]/D[j][j]
	print "\n Resolucion por Algoritmo LDMt "
	print " -------------------------------------------------"
	print " Matriz L Triangular Inferior"
	funciones.imprimeMatriz(L)
	print " Matriz D Diagonal"
	funciones.imprimeMatriz(D)
	print " Matriz Mt Triangular Superior"
	funciones.imprimeMatriz(Mt)
	print "Para hallar el resultado de LDMt.x=b requerimos 3 ecuaciones:"
	z = funciones.solucionL(L,B,n) 		#Lz = b   "obtenemos z"
	y = funciones.solucionL(D,z,n)		#Dy = z   "obtenemos y"
	x = funciones.solucionU(Mt,y,n)		#Mtx = y  "obtenemos x"
	return z,y,x