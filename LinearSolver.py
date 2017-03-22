"""Paquete que muestra la resolucion y factorizacion de un sistema de ecuaciones lineales
	 aplicando diferentes metodos.

   Nota: 
	- La mayoria de las funciones y las variables estan en ingles, y los comentarios en espanol.	
	- Aun falta implementar varios metodos, y mejorar los existentes.

   Definiciones:
   A, M : Matriz original.
   a : Matriz aumentada (A|b)
   b : Vector independiente. 
   L : Matriz triangular inferior unitaria.
   M : Matriz triangular inferior unitaria.
   U : Matriz triangular superior unitaria.
   D : Matriz diagonal.
   P : Matriz de permutacion
   Pr : Matriz de permutacion de filas
   Pc : Matriz de permutacion de columnas
   G : Matriz superior hallada con el metodo de Cholesky.
   Gt : Transpuesta de G.
   A = LU : significa factorizacion sin pivoteo
   PA = LU : significa factorizacion con pivoteo parcial
   PAQ = LU : significa factorizacion con pivoteo total

"""
from math import fabs
from math import sqrt
from sys import exit


def inputMatrix():
	"""Ingreso de datos de la matriz"""

	n = int(input("Ingrese el orden de la matriz: "))
	print "Ingrese los elementos de la matriz A fila por fila con un espacio luego enter"
	A = [[0.0]*n for i in range(n)]
	aux = [[0.0]*n for i in range(n)]
	for i in range(n):
		temp = raw_input()
		A[i] = temp.split()
		for j in range(n):
			A[i][j] = float(A[i][j])
	if A == aux:
		exit('Matriz nula, vuelva a escribir la matriz')
	return A		

def inputVector(M):
	"""Ingreso de datos del vector independiente"""

	n = len(M)
	print 'Ingrese los elementos del vector b'
	b = [0]*n
	#for i in range(n):
	#	b[i] = float(input())

	temp = raw_input();
	b = temp.split()
	for i in range(n):
		b[i] = float(b[i])

	return b	
	
def printMatrixD(M):
	"""Imprime la matriz, version debugger."""

	for i in range(len(M)):
		# print '|',
		for j in range(len(M[i])):
			if(i == 0 and j == 0):
				print " ",
				for x in range(len(M[i])):
					print '{0:8}'.format(x),
				print
				print
			if(j == 0):
				print i,

			if(j == len(M)):
				print '|',
				print '{0:8.4f}'.format(M[i][j]),
			else:
				print '{0:8.4f}'.format(M[i][j]),	
		print '|'
	print

def printMatrix(M):
	"""Imprime la matriz de una forma legible."""

	for i in range(len(M)):
		print '|',
		for j in range(len(M[i])):
			if(j == len(M)):
				print '|',
				print '{0:8.4f}'.format(M[i][j]),
			else:
				print '{0:8.4f}'.format(M[i][j]),	
		print '|'
	print  

def norm1(A):
	"""Calcula la norma 1"""

	summation = 0
	for i in range(len(A)):
		summation += abs(A[i][0])

	for j in range(1, len(A)):
		temp = 0
		for i in range(len(A[i])):
			temp += abs(A[i][j])
		summation = temp if (temp > summation) else summation

	return summation 

def infinityNorm(A):
	"""Calcula la norma infinita"""

	summation = 0
	for j in range(len(A)):
		summation += abs(A[0][j])

	for i in range(1, len(A)):
		temp = 0
		for j in range(len(A[i])):
			temp += abs(A[i][j])
		summation = temp if (temp > summation) else summation
			
	return summation  

def symmetricMatrix(A):
	"""Calcula la matriz simetrica de A"""

	for i in range(len(A)):
		for j in range(i+1,len(A)):
			if A[i][j] != A[j][i]:
				return False
	return True 

def trans(M):
	"""Calcula la matriz transpuesta de M"""

	n = len(M)
	return [[ M[i][j] for i in range(n)] for j in range(n)]

def reverseSub(a):
	"""Se usa para resolver la matriz superior de gauss/gauss-Jordan"""

	n = len(a)
	x = [0]*n
	for j in range(n-1, -1, -1):
		x[j] = (a[j][n] - sum(a[j][k]*x[k] for k in range(j+1, n)))/float(a[j][j])
	return x	

def solMatrixSup(M, b):
	"""Resuelve la matriz superior con el metodo inverso"""	

	x = []
	for i in range(len(M)-1,-1,-1):
		x.append((1.0/(M[i][i]))*(b[i]-sum(M[i][len(M)-j-1]*x[j] for j in range(len(x)))))
	x.reverse()
	
	return x

def solMatrixInf(M, b):
	"""Resuelve la matriz inferior con el metodo inverso"""

	x = []
	for i in range(len(M)):
		x.append((1.0/(M[i][i]))*(b[i]-sum(M[i][j]*x[j] for j in range(len(x)))))
	return x
	
def augmentedMatrix(M, b):
	"""Retorna la matriz aumentada"""
	
	a = M
	for i in range(len(M)):
		a[i].append(b[i])

	return a	

def maxColum(M, c):
	"""Devuelve la fila del mayor valor debajo de la diagonal en la columna c"""

	r = c #fila
	maximum = M[c][c]
	for i in range(c+1,len(M)):
		if(fabs(maximum) < fabs(M[i][c])):
			maximum = M[i][c]
			r = i
	return r

def maxSubMatrix(M, c):
	"""Retorna el mayor elemento de la submatriz A[c]"""

	row = c
	colum = c
	n = len(M)
	maximum = M[c][c]
		
	for j in range(c, n):
		for k in range(c, n):
			maxTemp = M[k][j]
			if(fabs(maximum) < fabs(maxTemp)):
				maximum = maxTemp
				colum = j
				row = k

	return row, colum			

def exchangeRows(M, r1, r2):
	"""Intercambia las filas r1 y r2 de M"""

	M[r1], M[r2] = M[r2], M[r1]
	return M

def exchangeCols(M, c1, c2):
	"""Intercambia las columnas c1 y c2 de M"""

	for k in range(len(M)):
		M[k][c1] , M[k][c2] = M[k][c2], M[k][c1]
	return M	

def pivot(a, P, Q, colum, piv=0):
	"""Se encarga del pivoteo en cualquier metodo."""

	if piv > 2 or piv < 0:
		exit('Valores invalidos para el parametro pivoteo, valores validos: 0, 1, 2.')
	n = len(a)
		
	temp = a[colum][colum]
	if(temp == 0.0 and piv == 0):
		row_maxColumn = maxColum(a, colum)
		a = pivotP(a, row_maxColumn, colum)
		P = exchangeRows(P, row_maxColumn, colum)
		print 'P(%d,%d)' % (row_maxColumn, colum)
		printMatrix(Pr(n, row_maxColumn, colum))
		
	elif piv == 1:
		row_maxColumn = maxColum(a, colum)
		if row_maxColumn != colum:
			a = pivotP(a, row_maxColumn, colum)
			P = exchangeRows(P, row_maxColumn, colum)
			print 'P(%d,%d)' % (row_maxColumn, colum)
			printMatrix(Pr(n, row_maxColumn, colum))
			
	elif piv == 2:
		row, c = maxSubMatrix(a, colum)	
		if (row != colum) or (c != colum) :
			a = pivotT(a, colum)
			P = exchangeCols(P, row, colum)
			Q = exchangeCols(Q, colum, c)
			print 'P(%d,%d):' % (colum, row)
			printMatrix(Pr(n, row, colum))
			print 'Q(%d,%d):' % (colum, c)
			printMatrix(Pr(n, c, colum))
	
	#retorna la matriz, la matriz de permutacion de filas y la de columnas.	
	return 	a, P, Q		

def pivotP(M, r1, r2):
	"""Permuta la fila r1 con la fila r2 de la matriz M"""

	return exchangeRows(M, r1, r2)

def pivotT(M, i):
	"""Busca el mayor elemento de la submatriz A[i] y permuta filas y columnas"""

	r, c = maxSubMatrix(M, i)
	M = pivotP(M, i, r)		

	return exchangeCols(M, c, i)

def L(n, ri, c):
	"""Calcula las matrices Li.

		ri: a[i][c] / a[c][c]
		c : columna c-esima 
	"""
	#Matriz identidad
	L = [[float(i == j) for j in range(n)] for i in range(n)]
	for k in range(c+1, n):
		L[k][c] = -ri[k]
			
	return L

def matrixMulti(A, B):
	"""Multiplica dos matrices, C = A*B """

	rowsA, colsA = len(A), len(A[0])
	rowsB, colsB = len(B), len(B[0])

	if colsA != rowsB:
		exit('Dimensiones incorrectas')

	C = [[0 for row in range(colsB)] for col in range(rowsA)]

	for i in range(rowsA):
		for j in range(colsB):
			for k in range(colsA):
				C[i][j] += A[i][k]*B[k][j]
	return C

def T(n, ri, c):
	"""Calcula las matrices Ti (Para el metodo Gauss-Jordan)

		ri: a[i][c] / a[c][c]
		c : columna c-esima 
	"""
	T = [[float(i == j) for j in range(n)] for i in range(n)]
	for k in range(n):
		T[k][c] = -ri[k]

	return T

def Pr(n, r1, r2):
	"""Calcula la matriz de permutacion de fila"""

	#Matriz identidad
	I = [[float(i == j) for j in range(n)] for i in range(n)]
	return exchangeRows(I, r1, r2)

def Pc(n, c1, c2):
	"""Calcula la matriz de permutacion de columna"""

	#Matriz identidad
	I = [[float(i == j) for j in range(n)] for i in range(n)]
	return exchangeCols(I, c1, c2)	

def multi(A,x):
	"""Multiplica una matriz con un vector"""

	c=[]
	for i in range(len(A)):
		c.append(sum(A[i][j]*x[j] for j in range(len(A))))
	return c

def invLU(A):
	P, L, U = croutLU1(A)
	for x in range(1,10):
		pass
		
def gauss(A, b, piv=0):
	"""Metodo de Gauss

		A: Matriz
		b: vector independiente
		piv: pivoteo, piv=0 sin pivoteo, piv=1 con pivoteo parcial
			 piv=2 con pivoteo total

	"""
	a = augmentedMatrix(A, b)
	n = len(A)
	P = [[float(i == j) for j in range(n)] for i in range(n)]
	Q = [[float(i == j) for j in range(n)] for i in range(n)]
	for j in range(len(a[0])):
		r = [0]*n
		# pivoteo
		if j < n:
			a, P, Q = pivot(a, P, Q, j, piv)

		for i in range(j+1, n):		
			
			#Eliminacion de gauss
			r[i] = a[i][j] / float(a[j][j])

			for k in range(j, len(a[0])):
				a[i][k] = a[i][k] - r[i]*a[j][k]
					
		if j < n:
			temp = [0]*n
			if (temp != r):
				print 'L%d' % (j+1)
				printMatrix(L(n, r, j))			

	print 'A|b:'			
	printMatrix(a)

	if piv == 2:
		return multi(Q, reverseSub(a))	

	return reverseSub(a)			

def gaussJordan(A, b, piv=0):
	"""Metodo de Gauss-Jordan
		A: Matriz
		b: vector independiente
		piv: pivoteo, piv=0 sin pivoteo, piv=1 con pivoteo parcial
			 piv=2 con pivoteo total  	
	"""
	a = augmentedMatrix(A, b)
	n_rows = len(a)
	n_cols = len(a[0])
	P = [[float(i == j) for j in range(n_rows)] for i in range(n_rows)]
	Q = [[float(i == j) for j in range(n_rows)] for i in range(n_rows)]
	for j in range(n_cols): #0, 1, 2, 3, 4
		r = [0]*n_rows
		for i in range(j+1, n_rows+1):		
			#pivoteo
			if i < n_rows:
				a, P, Q = pivot(a, P, Q, j, piv)

			if i == j+1:			
			#Eliminacion de gauss			
				for m in range(j):
					r[m] = a[m][j] / float(a[j][j])

				for l in range(j):
					for k in range(j, n_cols):
						if l < n_rows:
							a[l][k] = a[l][k] - r[l]*a[j][k]

			if i < n_rows:		
				r[i] = a[i][j] / float(a[j][j])				
				for k in range(j, n_cols):
					a[i][k] = a[i][k] - r[i]*a[j][k]				

		if j < n_rows:
			temp = [0]*n_rows
			if (temp != r):
				print 'T%d' % (j+1)
				printMatrix(T(n_rows, r, j))			

	#para convertir la diagonal en 1's.
	for i in range(n_rows):
		temp = float(a[i][i])
		for j in range(n_cols):
			a[i][j] = a[i][j] / temp

	print 'A|b:'			
	printMatrix(a)
	if piv == 2:
		return multi(Q, reverseSub(a))	

	return reverseSub(a)	

def croutLU1(A, piv=0):
	"""Calcula el metodo LU1"""

	n = len(A)
	L = [[0.0]*n for j in range(n)];
	U = [[float(i == j) for j in range(n)] for i in range(n)]
	P = [[float(i == j) for j in range(n)] for i in range(n)]
	Q = [[float(i == j) for j in range(n)] for i in range(n)]

	#pivot
	if piv:
		for j in range(len(A)):
			A, P, Q = pivot(A, P, Q, j, piv)

	for k in range(n):
		for i in range(k, n):
			L[i][k] = A[i][k] - sum(L[i][p]*U[p][k] for p in range(k))
		for i in range(k+1, n):
			if L[k][k] == 0:
				exit('Debe usarse pivoteo parcial')
			U[k][i] = (A[k][i] - sum(L[k][p]*U[p][i] for p in range(k))) / float(L[k][k])	

	if piv == 2:
		return P, Q, L, U	
	return P, L, U

def croutL1U(A, piv=0):
	"""Calcula el metodo L1U"""

	n = len(A)
	U = [[0.0]*n for j in range(n)];
	L = [[float(i == j) for j in range(n)] for i in range(n)]
	P = [[float(i == j) for j in range(n)] for i in range(n)]
	Q = [[float(i == j) for j in range(n)] for i in range(n)]

	#pivot
	if piv:
		for j in range(len(A)):
			A, P, Q = pivot(A, P, Q, j, piv)

	for k in range(n):
		for i in range(k, n):
			U[k][i] = A[k][i] - sum(L[k][p]*U[p][i] for p in range(k))
		for i in range(k+1, n):
			if U[k][k] == 0:
				exit('Debe usarse pivoteo parcial')
			L[i][k] = (A[i][k] - sum(L[i][p]*U[p][k] for p in range(k))) / float(U[k][k])	
	
	if piv == 2:
		return P, Q, L, U

	return P, L, U

def Doolittle(A, piv=0):

	n = len(A)
	U = [[0.0]*n for j in range(n)]
	L = [[float(i == j) for j in range(n)] for i in range(n)]
	P = [[float(i == j) for j in range(n)] for i in range(n)]
	Q = [[float(i == j) for j in range(n)] for i in range(n)]

	#pivot
	if piv:
		for j in range(len(A)):
			A, P, Q = pivot(A, P, Q, j, piv)

	for k in range(n):
		for i in range(n):
			U[k][i] = A[k][i] - sum(L[k][p]*U[p][i] for p in range(k))
		for i in range(k, n):
			if U[k][k] == 0:
				exit('Debe usarse pivoteo parcial')
			L[i][k] = (A[i][k] - sum(L[i][p]*U[p][k] for p in range(k))) / float(U[k][k])	

	if piv == 2:
		return P, Q, L, U
	return P, L, U

def LDMt(A, piv=0):
	""""""
	if piv == 2:
		P, I, L, U = croutLU1(A, piv)
	else:
		P, L, U = croutLU1(A, piv)

	D, M = diagonalDMt(U)
	return L, D, M

def diagonalDMt(U):

	n = len(U)
	D = [[float(i == j) for j in range(n)] for i in range(n)]
	for i in range(n):
		D[i][i] = float(U[i][i])
	for i in range(n):
		for j in range(n):
			U[i][j] /= (D[i][i])
	return D, U

def cholesky(A):
	if not symmetricMatrix(A):
		exit('La matriz no es simetrica')
	n = len(A)
	G = [[0.0]*n for j in range(n)]
	for i in range(n):
		suma = A[i][i]
		for k in range(i):
			suma -= A[k][i]**2
		if suma < 0:
			exit('No es definida positiva')	
		A[i][i] = sqrt(suma)
		for j in range(i+1, n):
			suma = A[i][j]
			for k in range(i):
				suma -= A[k][i]*A[k][j]
			A[i][j] = suma / A[i][i]

	for j in range(n):
		for i in range(n):
			if(i > j):
				A[i][j] = 0.0
	return A	

def norm(x):
    """Norma euclideana del vector x, ie, ||x||2"""

    return sqrt(sum([x_i**2 for x_i in x]))

def Q_i(Q_min, i, j, k):
    """Rellenando elementos de la matrix Q_t"""

    if i < k or j < k:
        return float(i == j)
    else:
        return Q_min[i-k][j-k]

def Householder(A):
	""" Transformacion por Householder, donde Hn...H2*H1*A = R, Q_t*A = R
		Q = H1*H2 ... Hn, Q es ortogonal (Q * Qt = I)
		Retorna Q y R, donde A = Q*R 
	"""

	n = len(A)

	R = A
	Q = [[0.0] * n for i in range(n)]

	for k in range(n-1):                                                                    
		I = [[float(i == j) for i in range(n)] for j in range(n)]

		# Se crea los vectores x, e y un escalar alpha
		x = [row[k] for row in R[k:]]
		e = [row[k] for row in I[k:]]
		#La funcion cmp(a, b) retorna -1 si a<b, 1 si a>b, 0 si a==b
		alpha = -cmp(x[0],0) * norm(x) 

		#Se crea los vectores u, v
		u = map(lambda p,q: p + alpha * q, x, e)
		norm_u = norm(u)
		v = map(lambda p: p/norm_u, u)

		#Se crea la matriz menor Q_t
		Q_min = [ [float(i==j) - 2.0 * v[i] * v[j] for i in range(n-k)] for j in range(n-k) ]

		#Se rellena la matriz menor Q (Q_min)
		Q_t = [[ Q_i(Q_min,i,j,k) for i in range(n)] for j in range(n)]

		#Si esta en la primera ejecutada, entonces se calcula Q_t*A = R
		#Sino, Q_tn .. Q_t1*A = R
		if k == 0:
			Q = Q_t
			R = matrixMulti(Q_t,A)
		else:
			Q = matrixMulti(Q_t,Q)
			R = matrixMulti(Q_t,R)

	#Se retorna la transpuesta de los Q_t, ie, trans(Q_tn* ... *Q_t1) = Q
	return trans(Q), R

def givens(A):
	"""	Gn* ... G2*G1*A = R
		Q_t = Gn* ... G2*G1
		A = Q*R, de la propiedad Q_t * Q = I
	"""
	n = len(A)

	An = A	
	Gn = [[float(i == j) for j in range(n)] for i in range(n)]
	Q_t = [[float(i == j) for j in range(n)] for i in range(n)]

	a = An[0][n-2]
	b = An[0][n-1]
	index = 1
	for i in range(n):
		for j in range(n-1, i, -1):
			a = An[j-1][i]
			b = An[j][i]
			if a*a + b*b == 0:
				continue

			cosX = a / (sqrt(a*a + b*b)) 
			sinX = -b / (sqrt(a*a + b*b))

			Gn[j][j] = cosX
			Gn[j][j-1] = sinX
			Gn[j-1][j] = -sinX
			Gn[j-1][j-1] = cosX

			print 'G' +str(index) + ':'
			printMatrix(Gn)

			An = matrixMulti(Gn, An)

			print 'A' +str(index) + ':'
			printMatrix(An)

			Q_t = matrixMulti(Gn, Q_t)
			#Volviendo la matriz Gn a la identidad
			Gn = [[float(k == l) for l in range(n)] for k in range(n)]
			index += 1
	return trans(Q_t), An

def normaInfVector(L):
	""" Calcula la norma infinita de un vector:
		||x|| = max {|xi|}, i = 0, 1, ... n.
	"""

	maximum = fabs(L[0])
	for i in range(1, len(L)):
		maximum = max(maximum, fabs(L[i]))
	return maximum	

def jacobi(A, b, prec=1e-7):
	"""Metodo que calcula la solucion Ax = b, usando tecnicas iterativas"""
	
	n = len(A)
	Xk = [0.0]*n
	sumation = 0.0
	for i in range(n):
		if A[i][i] == 0:
			exit('Los elementos A[i][i] deben ser diferentes de 0')

	Xk1 = [b[i]/float(A[i][i]) for i in range(n)]
	minus = lambda x, y: [x[i]-y[i] for i in range(n)]

	for j in range(n):
		dominancia = 0.0
		for i in range(j+1, n):
			if j != i:
				dominancia += fabs(A[i][j])
		if A[i][i] < dominancia:
			exit('La matriz no converge')

	while (normaInfVector(minus(Xk1,Xk)) / float(normaInfVector(Xk1))) > prec:
		Xk[:] = Xk1[:]
		for i in range(n):
			sumation = sum(A[i][j]*Xk1[j] if i!=j else 0 for j in range(n))
			Xk1[i] = (1.0/A[i][i])*(b[i] - sumation)

		print Xk1
	return Xk1			

def gaussSeidel(A, b, prec=1e-7):
	"""Metodo que calcula la solucion Ax = b, usando tecnicas iterativas"""

	n = len(A)
	Xk = [0.0]*n
	sumation = 0.0
	for i in range(n):
		if A[i][i] == 0:
			exit('Los elementos A[i][i] deben ser diferentes de 0')
	Xk1 = [b[i]/float(A[i][i]) for i in range(n)]
	minus = lambda x, y: [x[i]-y[i] for i in range(n)]

	for j in range(n):
		dominancia = 0.0
		for i in range(j+1, n):
			if j != i:
				dominancia += fabs(A[i][j])
		if A[i][i] < dominancia:
			exit('La matriz no converge')

	while (normaInfVector(minus(Xk1,Xk)) / float(normaInfVector(Xk1))) > prec:
		Xk[:] = Xk1[:]
		for i in range(n):
			sumation1 = sum(A[i][j]*Xk1[j] for j in range(i))
			sumation2 = sum(A[i][j]*Xk1[j] for j in range(i+1, n))

			Xk1[i] = (1.0/A[i][i])*(b[i] - sumation1 - sumation2)

		print Xk1
	return Xk1

def sor(A, b, prec=1e-7, w=1.5):
	""" Metodo SOR, calcula la solucion de un sistema de ecuaciones
		usando el parametro de relajacion w, que necesariamente varia
		de <0, 2> solo en el caso que la matriz converja.
	"""
	n = len(A)
	Xk = [0.0]*n
	sumation = 0.0
	#Garantizar que los elementos de la diagonal principal sean distintos de cero
	for i in range(n):
		if A[i][i] == 0:
			exit('Los elementos A[i][i] deben ser diferentes de 0')

	Xk1 = [b[i]/float(A[i][i]) for i in range(n)]
	minus = lambda x, y: [x[i]-y[i] for i in range(n)]

	# for j in range(n):
	# 	dominancia = 0.0
	# 	for i in range(n):
	# 		if j != i:
	# 			dominancia += fabs(A[i][j])
	# 	if A[i][i] < dominancia:
	# 		exit('La matriz no converge')

	while (normaInfVector(minus(Xk1,Xk)) / float(normaInfVector(Xk1))) > prec:
		Xk[:] = Xk1[:]
		for i in range(n):
			sumation1 = sum(A[i][j]*Xk1[j] for j in range(i))
			sumation2 = sum(A[i][j]*Xk1[j] for j in range(i+1, n))

			Xk1[i] = (float(w)/A[i][i])*(b[i] - sumation1 - sumation2) + (1-w)*Xk[i]

		print Xk1
	return Xk1

def menu():
	print "\t\t\t  Bienvenidos al Programa de"
	print "\t\t\tResolucion de Ecuaciones Lineales"
	opc = 1
	while(opc):
		print "Elija el metodo a usar:\n"
		print """
			0.  Definiciones
			1.  Gauss
			2.  Gauss-Jordan
			3.  Crout LU1
			4.  Crout L1U
			5.  Doolittle
			6.  LDMt
			7.  Cholesky
			8.  Parlett y Reid (falta)
			9.  Aasen (falta)
			10. Householder
			11. Givens
			12. Jacobi
			13. Gauss-Seidel
			14. SOR
			15. Condicionamiento (incompleto)
			16. Salir
			  """
		opc = input('Ingrese opcion\n')
		if type(opc) != type(1):
			exit('Debe ingresar un valor entero, vuela a intentarlo')
		if opc == 16:
			exit('Gracias por usar el programa')
		if opc < 0 or opc > 16:
			print 'Opcion incorrecta'
			continue
		#Ver la documentacion	
		if opc == 0:
			print __doc__
			opc = 1
			continue

		Matrix = inputMatrix()		 		
		#Matrix = [
		#		[1, -4, 2, 1],
		 #		[2, -6, 1, 4],
		 #		[-1, 2, 3, 4],
		 #		[0, -1, 1, 1]
		 #		]		 		
		#El condicionamiento no necesita el vector b
		if opc != 15:
			
			b = inputVector(Matrix)
	 	 
			#b = [-4, 1, 12, 0]	 	 
			restric = [7, 10, 11, 12, 13, 14]
			if opc not in restric:
				print "Elija el pivoteo a usar:\n"
				print """
					0.  Sin pivoteo
					1.  Pivoteo parcial
					2.  Pivoteo total
						
					  """
				piv = int(raw_input('Ingrese opcion\n'))
		#Gauss
		if opc == 1:
			x = gauss(Matrix, b, piv)
			print 'x:'
			print x

		#Gauss-Jordan	
		elif opc == 2:
			x = gaussJordan(Matrix, b, piv)
			print 'x:'
			print x

		#croutLU1, croutL1U, Doolittle
		elif opc == 3 or opc == 4 or opc == 5:
			#croutLU1
			if opc == 3:
				if piv == 2:
					P, Q, L, U = croutLU1(Matrix, piv)
				else:		
					P, L, U = croutLU1(Matrix, piv)
			#croutL1U		
			elif opc == 4:
				if piv == 2:
					P, Q, L, U = croutL1U(Matrix, piv)
				else:		
					P, L, U = croutL1U(Matrix, piv)
			#Doolittle		
			elif opc == 5:
				if piv == 2:
					P, Q, L, U = Doolittle(Matrix, piv)
				else:		
					P, L, U = Doolittle(Matrix, piv)			

			#Imprimir las matrices	
			print 'P:'
			printMatrix(P)
			if piv == 2:
				print 'Q:'
				printMatrix(Q)		
			print 'L:'
			printMatrix(L)
			print 'U:'
			printMatrix(U)
		
			#calcula las soluciones de Lz=b y Ux=z	
			if piv == 2:
				z = solMatrixInf(L, b)
				y = solMatrixSup(U,z)
				x = multi(P, y)
			else:
				z = solMatrixInf(L, b)
				x = solMatrixSup(U,z) 	

			#imprime las soluciones
			print "z:"
			print z
			print "x:"
			print x

		#LDMt
		elif opc == 6:
			L,D,M = LDMt(Matrix, piv)
			print 'L:'
			printMatrix(L)		
			print "D:"
			printMatrix(D)
			print "M:"
			printMatrix(M)

			#calcula las soluciones
			y = solMatrixInf(L, b)
			z = solMatrixInf(D, y)
			x = solMatrixSup(M, z)
			
			#imprime las soluciones
			print "y:"
			print y
			print "z:"
			print z
			print "x:"
			print x

		#Cholesky
		elif opc == 7:
			G = cholesky(Matrix)
			Gt = trans(G) 
			print "G:"
			printMatrix(G)
			print "Gt:"
			printMatrix(Gt)

			#calcula las soluciones
			z = solMatrixInf(Gt, b)
			x = solMatrixSup(G, z)
			
			#imprime las soluciones
			print "z:"
			print z
			print "x:"
			print x

		#Parlett y Reid	
		elif opc == 8:
			print 'Falta implementar'	
		
		#Aasen	
		elif opc == 9:
			print 'Falta implementar'

		#Householder y Givens	
		elif opc == 10 or opc == 11:
			#Householder
			if opc == 10:	
				Q, R = Householder(Matrix)
			#Givens
			elif opc == 11:
				Q, R = givens(Matrix)

			print 'Q:'
			printMatrix(Q)			  

			print 'R:'
			printMatrix(R)			  
			#Comprobar la igualdad
			print 'A = Q*R :'
			printMatrix(matrixMulti(Q, R))

			b_prima = multi(trans(Q), b)
			print 'b\':'
			print b_prima

			x = solMatrixSup(R, b_prima)
			print 'x:'
			print x

			print 'Ax = b :'
			print multi(Matrix, x)
		
		#Jacobi
		elif opc == 12:
			prec = float(raw_input('Ingrese la precision, ejemplo : 0.001  '))
			x = jacobi(Matrix, b, prec)
			print 'x:'
			print x

			print 'Ax = b :'
			print multi(Matrix, x)

		#Gauss-Seidel	
		elif opc == 13:
			prec = float(raw_input('Ingrese la precision, ejemplo : 0.001  '))
			x = gaussSeidel(Matrix, b, prec)
			print 'x:'
			print x
		
		#SOR (Successive Over relaxation)
		elif opc == 14:
			prec = float(raw_input('Ingrese la precision, ejemplo: 0.001 : '))
			w = float(raw_input('Ingrese el parametro de relajacion <0, 2>, ejemplo 0.5 : '))
			x = sor(Matrix, b, prec, w)
			print 'x:'
			print x
		
		#Condicionamiento	
		elif opc == 15:
			
			while 1:
				print "Elija el tipo de condicionamiento:\n"
				print """
					1.  Norma 1
					2.  Norma 2
					3.  Norma infinita
					4.  Condicionamiento con norma 1
					5.  Condicionamiento con norma 2
					6.  Condicionamiento con norma infinita
					7.  Salir
						
					  """
				nor = int(raw_input('Ingrese Opcion\n'))
				#Norma 1
				if nor == 1:
					print 'norm1(M):'
					print norm1(Matrix)
				
				#Norma 2	
				elif nor == 2:
					print 'Falta implementar'
					# print norma2(Matrix)	
				
				#Norma infinita	
				elif nor == 3:
					print 'infinityNorm(M):'
					print infinityNorm(Matrix)	

				#Condicionamiento de la matriz usando norma 1	
				elif nor == 4:
					print 'Falta implementar'	

				#Condicionamiento de la matriz usando norma 2	
				elif nor == 5:
					print 'Falta implementar'	

				#Condicionamiento de la matriz usando norma infinita	
				elif nor == 6:
					print 'Falta implementar'	

				#Salir del menu	
				elif nor == 7:
					exit('Gracias por usar el programa')
				else:
					print 'Opcion incorrecta'
					continue
				print 'Resultado obtenido con exito'		 		

	print 'Resultado obtenido con exito'	

#menu()
