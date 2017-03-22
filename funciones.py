import math
import os
import csv

def menu():
	print "\n Elija el metodo a Realizar:"
	print " ---------------------------"
	print "  1. Metodo de Gauss "
	print "  2. Metodo de Gauss Jordan"
	print "  3. Metodo L1U-Crout"
	print "  4. Metodo LU1-Crout"
	print "  5. Metodo LU-Doolittle"
	print "  6. Metodo de LDMt "
	print "  7. Metodo de LDLt "
	print "  8. Metodo de Cholesky "
	print "  9. Metodo de Parlett y Reid "	
	print " 10. Metodo de Aasen "
	print " 11. Metodo de Gram-Schmidt "
	print " 12. Salir "
	try:
		opcion=int(raw_input("\n Ingrese Opcion: "))
		return opcion
	except:
		limpiaPantalla()
		print "\n\n Opcion no valida!, Usted no ingreso un numero\n"
		return menu()

def leerMat(texto):
	mat = []
	with open(texto, "rb") as f:
		reader = csv.reader(f)
		for i in reader:
			v = (i[0].split(';'))
			mat.append(v)
	f.close()
	for i in range(len(mat)):
		for j in range(len(mat[0])):
			mat[i][j] = float(mat[i][j])
	return mat

def leerVect(texto):
	mat = []
	new = []
	with open(texto, "rb") as f:
		reader = csv.reader(f)
		for i in reader:
			v = (i[0].split(';'))
			mat.append(v)
	f.close()
	for i in range(len(mat[0])):
		new.append( float(mat[0][i]))
	return new

def epsilonMaq():
	eps = 1.0
	while eps + 1.0 > 1.0:
		epsilon = eps
		eps = 0.5*eps
	return epsilon

def limpiaPantalla():
	if str(os.getcwd())[0] in ('C','D','E','F','G','H','I'):
		os.system('cls')
	else:
		os.system('clear')

def pivot(a, colum):
	fil_maxcol = colum #fila
	maximo = a[colum][colum]
	for i in range(colum+1,len(a)):
		if(math.fabs(maximo) < math.fabs(a[i][colum])):
			maximo = a[i][colum]
			fil_maxcol = i
	if fil_maxcol != colum:
		a[fil_maxcol], a[colum] = a[colum], a[fil_maxcol]
	return 	a

def imprimeMatriz(A):
	for i in range(len(A)):
		text = " |"
		for j in range(len(A[i])):
			if(j==len(A)):
				text = text +str("%8.3f"%A[i][j])
			else:
				 text = text +str("%8.3f"%A[i][j])
		print text+"| "
	print

def imprimeSistema(A,b,n):
	x = []
	text = " |"
	for i in range(n):
		for j in range(n):
			varA = str("%8.2f"%A[i][j])
			text = text + varA + " "
		varB = str("%8.2f"%b[i])
		print text + "| " + varB
		text =" |"

def matrizAumentada(M, b, n):
	"""Retorna la matriz aumentada"""
	a = []
	for i in range(n):
		a.append([])
		for j in range(n):
			a[i].append(M[i][j])
	for i in range(n):
		a[i].append(b[i])
	return a

def suma(U,L,i,j,x):
	suma = 0.0
	for k in range(0,x):
		suma += L[i][k]*U[k][j]
	return suma

def solucionL(A,B,n):
	x = []
	for i in range(n):
		if A[i][i] == 0:
			return "NULL"
		x.append((1.0/A[i][i])*(B[i] - sum(A[i][j]*x[j] for j in range(len(x)))))
	return x

def solucionU(A,B,n):
	x = []
	for i in range(n-1,-1,-1):
		if A[i][i] == 0:
			return "NULL"
		x.append((1.0/A[i][i])*(B[i] - sum(A[i][n-j-1]*x[j] for j in range(len(x)))))
	x.reverse()	
	return x

def mulMatrices(A, B, n):
	M = [[0 for f in range(n)] for c in range(n)]
	for i in range(n):
		for j in range(n):
			for k in range(n):
				M[i][j] += A[i][k]*B[k][j]
	return M

def mulVector(A,b,n):
	v=[]
	for i in range(n):
		v.append(sum(A[i][j]*b[j] for j in range(n)))
	return v

def transMatriz(M,n):
	return [[ M[i][j] for i in range(n)] for j in range(n)]
	return M

def esSimetrica(A,n):
	for i in range(n):
		for j in range(i+1,n):
			if A[i][j] != A[j][i]:
				return False
	return True 

def simetSistema(A,b,n):
	print "\n La matriz A no es simetrica, para probar este algoritmo"
	print " multiplicaremos At por izquierda a nuestro sistema"
	print " Tendremos ara un nuevo sitema: A'x=b' donde A'=At.A y b' = At.b\n"
	print " Matriz A"
	print " --------"
	imprimeMatriz(A)
	At = transMatriz(A,n)
	print " Matriz At"
	print " ---------"
	imprimeMatriz(At)
	C = mulMatrices(At,A,n)
	d = mulVector(At,b,n)
	print " Matriz At.A"
	print " -----------"
	imprimeMatriz(C)
	print " Vector At.b: "+str(d)
	return C,d

def inversa(M,n):
	I = []
	for i in range (n):
		I.append([0]*(n))
	for i in range (n):
		I[i][i] = 1
	mayor = 0
	Q = []
	Q1 = []
	for s in range (n):
		Q.append(0)
		Q1.append(0)
	for i in range (n):
		j = i+1
		if M[i][i] == 0:
			p = i+1
			mayor = M[j][i]
			for j in range (i+2,n):
				if(abs(mayor) < abs(M[j][i])):
					mayor= M[j][i]
					p = j
			Q=M[i]
			M[i]=M[p]
			M[p]=Q
			Q1=I[i]
			I[i]=I[p]
			I[p]=Q1
		for j in range (0,i):
			w = M[j][i]*(M[i][i])**(-1)
			for k in range (i,n):
				M[j][k] =M[j][k] - (w*M[i][k])
				M[j][i]=0
			for k in range (n):
				I[j][k] =I[j][k] - (w*I[i][k])
		for j in range (i+1,n):
			w = M[j][i]*(M[i][i])**(-1)
			for k in range (i,n):
				M[j][k] =M[j][k] - (w*M[i][k])
				M[j][i]=0
			for k in range (n):
				I[j][k] =I[j][k] - (w*I[i][k])
	for i in range (n):
		I[i][i]=I[i][i]*(M[i][i])**(-1)
	return I

def paso(A,n):
	a=[ [ 0 for i in range(n+1) ] for j in range(n+1) ] 
	for i in range (n):
		for j in range(n):
			a[i+1][j+1]=A[i][j]
	return a

def solGramm(A,b,n):
	a = matrizAumentada(A, b, n)
	n = len(A)
	for j in range(len(a[0])):
		r = [0]*n
		if j < n:
			a = pivot(a, j)

		for i in range(j+1, n):		
			if a[j][j]==0:
				return "NULL"
			r[i] = a[i][j] / float(a[j][j])
			for k in range(j, len(a[0])):
				a[i][k] = a[i][k] - r[i]*a[j][k]
	B = []
	for i in range(n):
		B.append(a[i][n])
	return solucionU(a,B,n)

def sumaGramm(A,m,x):
	suma = 0.0
	for k in range(m):
		suma = suma + A[k][x]*A[k][x]
	return suma

def productoGramm(A,m,x,y):
	producto = 0.0
	for k in range(m):
		producto = producto + (A[k][x]*A[k][y])
	return producto

def suma_1(G,j):
	suma = 0.0
	for p in range(0,j):
		suma += G[j][p]*G[j][p]
	return suma

def suma_2(G,i,j):
	suma = 0.0
	for p in range(0,j):
		suma += G[i][p]*G[j][p]
	return suma

"""
n = 4
A =[[ 2, 1,  0, 4],
	[-4,-2,  3,-7],
	[ 4, 1, -2, 8],
	[ 0,-3,-12,-1]
	]
b = [ 2,-9, 2, 2]

print
x = gauss(A,b)
print "solucion:" +str(x)
#"sol = 3,4,-1,-2"


n = 4
A =[[ 1,-4, 1, 1],
	[ 1, 0, 1, 3],
	[-2, 0,-1, 0],
	[ 0, 0, 1, 0]
	]
b = [ 2,-9, 2, 2]

print
U,L,t = metodoLU1(A,b,n)
print "solucion y:" +str(t[0])
print "solucion x:" +str(t[1])


n = 4
A =[[ 5, 1,-2, 0],
	[ 1, 2, 0, 0],
	[-2, 0, 4, 1],
	[ 0, 0, 1, 3]
	]
b = [ 1, 5, 14, 15]
t = LDLt(A,b,n)
print t[0]
print t[1]
print t[2]

A =[[ 0, 1, 2, 3],
	[ 1, 2, 2, 2],
	[ 2, 2, 3, 3],
	[ 3, 2, 3, 4]
	]


	m=n=7
A=[17.0,-2.0,3.0,-1.0,-2.0,3.0,-1.0],[3.0,27.0,-2.0,-4.0,7.0,0.0,0.0],[-5.0,5.0,26.0,-3.0,-2.0,1.0,-4.0],[1.5,-0.8,-7.0,19.0,-3.0,2.0,-1.0],[0.0,2.0,-0.4375,-1.0,13.0,-4.0,-2.0],[-4.0,0.0,0.0,-2.0,-1.0,19.0,-1.0],[0.0,2.0,-1.0,0.0,-0.25,-0.16,19.0]
b=[1000.0,800.0,300.0,750.0,1100.00,600.00,200.00]
"""
