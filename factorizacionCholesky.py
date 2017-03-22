from printMatrixVector import *
from eliminacionGauss import *
from math import *
def factorizacionCholeskyFilas(A,b,n):
	G = []
	Gt = []
	for i in range(n):
		G.append([0]*n)
		Gt.append([0]*n)

	for i in range(n):
		G[i][i] = A[i][i]
		for k in range(0,i):
			G[i][i] = G[i][i] - G[k][i]*G[k][i]
		G[i][i] = sqrt(G[i][i])
		for j in range(i+1,n):
			G[i][j] = A[i][j]
			for k in range(0,i):
				G[i][j] = G[i][j] - G[k][i]*G[k][j]
			G[i][j] = G[i][j]/G[i][i]
	for i in range(n):
		for j in range(n):
			Gt[j][i] = G[i][j]
	printMatrix(G)
	printMatrix(Gt)
	y = eliminacionGaussTriangularInferior(Gt,b,n)
	print "Solucion y:"
	printVector(y)
	x = eliminacionGaussTriangularSuperior(G,y,n)
	print "Solucion x:"
	printVector(x)

def factorizacionCholeskyColumnas(A,b,n):
	G = []
	Gt = []
	for i in range(n):
		G.append([0]*n)
		Gt.append([0]*n)

	for j in range(n):
		for i in range(0,j-1):
			suma = .0
			for k in range(0,i):
				suma = suma + G[k][i]*G[k][j]
			G[i][j] = (A[i][j] - suma)/G[i][i]
		suma = .0
		for k in range(0,j):
			suma = suma + G[k][j]*G[k][j]
		G[j][j] = sqrt(A[j][j] - suma)
	for i in range(n):
		for j in range(n):
			Gt[j][i] = G[i][j]
	printMatrix(G)
	printMatrix(Gt)
	y = eliminacionGaussTriangularInferior(Gt,b,n)
	print "Solucion y:"
	printVector(y)
	x = eliminacionGaussTriangularSuperior(G,y,n)
	print "Solucion x:"
	printVector(x)

if __name__ == '__main__':
	b = [1.0,5,0,14.0,15.0]
	A = [5.0,1.0,-2.0,.0],[1.0,2.0,.0,.0],[-2.0,.0,4.0,1.0],[.0,.0,1.0,3.0]
	n = len(A)
	print "Sistema Lineal Ax = b"
	printMatrixVector(A,b)
	factorizacionCholeskyFilas(A,b,n)
	factorizacionCholeskyColumnas(A,b,n)

	b = [1.0,5,0,14.0,15.0]
	A = [5.0,1.0,-2.0,.0],[1.0,2.0,.0,.0],[-2.0,.0,4.0,1.0],[.0,.0,1.0,3.0]

	x = eliminacionGauss(A,b,n)
	print "Solucion x:"
	printVector(x)