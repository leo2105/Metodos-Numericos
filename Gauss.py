import funciones

def gauss(A, b,n):
	a = []
	a = funciones.matrizAumentada(A, b, n)
	n = len(A)
	for j in range(len(a[0])):
		r = [0]*n
		# pivoteo
		if j < n:
			a = funciones.pivot(a, j)

		for i in range(j+1, n):		
			if a[j][j]==0:
				return "NULL"
			#Eliminacion de gauss
			r[i] = a[i][j] / float(a[j][j])

			for k in range(j, len(a[0])):
				a[i][k] = a[i][k] - r[i]*a[j][k]
	B = []
	for i in range(n):
		B.append(a[i][n])
	print " \n Resolucion por Algoritmo de Eliminacion de Gauss "
	print " -------------------------------------------------"
	funciones.imprimeSistema(a,B,n)
	x = funciones.solucionU(a,B,n)
	return x