def mostrar(A,b,n):
	for i in range(0,n):
		print A[i]
	print 'b:'
	print b
	print '-----------'

def sumD(n,A,t,x):
	s = 0
	for i in range(0,n):
		s=s+A[t][i]*x[i]
	return s
def sumI(j,n,A,t,x):
	s = 0
	if j>=n :
		return 0
	for i in range(j,n):
		s=s+A[i][t]*x[i]
	return s

def sum1(i,j,A):
	s = 0
	if i==0:
		return 0
	for k in range(0,i):
		s=s+A[j][k]*A[i][k]
	return s

###########################################
# Usaremos el algoritmo de Cholesky  ######
# para desarrollar sistemas de ############
# de ecuaciones Lineales ##################
###########################################
n = int(raw_input('Ingrese orden: '))
A=[]
L=[]
b=[]
y=[]
x=[]
m = 0
band = True
###########################################
## Inicializamos A y le anadimos valores ##
## via teclado ############################
###########################################
for i in range(n):
	A.append([])
	L.append([])
	x.append(0)
	y.append(0)
	b.append(0)
	for j in range(n):
		A[i].append(0)
		L[i].append(0)

for i in range(n):
	for j in range(n):
		A[i][j] = float(raw_input('a(%d,%d): '%(i+1,j+1)))
for i in range(n):
	b[i] = float(raw_input('b[%d]: '%(i+1)))
print 'Matriz A:'
mostrar(A,b,n)

############################################
## Factorizacion A = (L)(L*) ###############
############################################
for i in range(0,n):
	if A[i][i] == 0:
		band = False
		break

if band:
	for j in range(n):
		for i in range(j,n):
			if i==j:
				L[i][i]=(A[i][i] - sum1(i,j,L))**0.5
			else:
				L[i][j]=(A[i][j] - sum1(i,j,L))/L[j][j]
	print 'Matriz L:'
	mostrar(L,b,n)

	######################################
	## sustitucion Directa Ly = b ########
	######################################
	for i in range(0,n):
		y[i] = (b[i]-sumD(i,L,i,y))/L[i][i]
	print y
	######################################
	## sustitucion Directa (Lt)x = y #####
	######################################

	for i in range(0,n):
		x[n-1-i] = (y[n-1-i]-sumI(n-i,n,L,n-1-i,x))/L[n-1-i][n-1-i]
	print x
