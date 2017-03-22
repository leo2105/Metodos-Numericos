import funciones

def gaussJordan(A, b, n):
	a = []
	a = funciones.matrizAumentada(A, b, n)
	filas = n
	columnas = n

	for j in range(columnas):
		r = [0]*filas
		for i in range(j+1, filas+1):		
			#pivoteo
			if i < filas:
				a = funciones.pivot(a, j)
			if i == j+1:			
			#Eliminacion de gauss			
				for m in range(j):
					if a[j][j] == 0:
						return "NULL"
					r[m] = a[m][j] / float(a[j][j])
				for l in range(j):
					for k in range(j, columnas):
						if l < filas:
							a[l][k] = a[l][k] - r[l]*a[j][k]
			if i < filas:
				if a[j][j] == 0:
					return "NULL"
				r[i] = a[i][j] / float(a[j][j])				
				for k in range(j, columnas):
					a[i][k] = a[i][k] - r[i]*a[j][k]				
	#Transforma en Diagonal de unos
	for i in range(filas):
		temp = float(a[i][i])
		for j in range(columnas):
			if temp == 0:
				return "NULL"
			a[i][j] = a[i][j] / temp
	x = []
	for i in range(n):
		x.append(a[i][n])
	print"\n -------------------------------------------------"
	print" Matriz Diagonalizada por Gaus-Jordan"
	print" -------------------------------------------------"
	funciones.imprimeSistema(a,x,n)
	return x