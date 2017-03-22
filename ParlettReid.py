import funciones

def metodoParlet(aa,bb,nn):
	global A,a,b,n
	a = aa[:]
	b = bb[:]
	n = nn
	A=[]
	for i in range(n):
		A.append([0]*(n+1))
	for i in range(n):
		for j in range(n):
			A[i][j]=a[i][j]
	for i in range(n):
		A[i][n]=b[i]
	I,P,M,L,U,T,G,F,S,PP,W,PPT,b=[],[],[],[],[],[],[],[],[],[],[],[],[]
	for i in range (n):
		I.append([0]*(n))
		PPT.append([0]*(n))
		P.append([0]*(n))
		W.append([0]*(n))
		M.append([0]*(n))
		L.append([0]*(n))
		PP.append([0]*(n))
		U.append([0]*(n+1))
		T.append([0]*(n+1))
		S.append([0]*(n+1))
		G.append(0)
		F.append(0)
		b.append(0)
		P[i][i]=1
		PP[i][i]=1
		I[i][i]=1
		W[i][i]=1


	for i in range(n):
		L[i][i]=1
	for i in range(n):
		for j in range(n+1):
			T[i][j]=A[i][j]
   
   #algoritmo#
	for i in range(n-2):
		P=[]
		for j in range (n):
			P.append([0]*(n))
			P[j][j]=1
		for j in range(n):
			for k in range(n):
				S[j][k] = I[j][k]
		#Pivoteo#
		p = i+1       
		mayor = abs(T[i+1][i])
		for j in range (i+2,n):    
			if mayor < abs(T[j][i]):
				mayor = abs(T[j][i])
				p = j
		P[i+1] = S[p]
		P[p] = S[i+1]       
	#funciones.mulMatriceslicacion PAPT#
		F=T[i+1]
		T[i+1] = T[p]
		T[p] = F        
		for j in range(n):
			for k in range(n+1):
				U[j][k] = T[j][k]       
		for j in range (n):
			for k in range (n):
				suma = 0
				for l in range (n):
					suma = suma + U[j][l]*P[k][l]
				T[j][k] = suma
	#Gauss#
		for j in range (n):
			G[j]=0
			U.append([0]*(n+1))
		for j in range (i+2,n):
			G[j] = U[j][i]*(U[i+1][i]**(-1))        
	#matriz de gaus#
		for j in range (n):
			for l in range (n):
				M[j][l] = S[j][l] - G[j]*I[i+1][l]       
	#funciones.mulMatriceslicacion MPAPTMT#                
		for j in range(n):
			for k in range(n+1):
				U[j][k] = T[j][k]        
		for j in range(n):
			for k in range(n):
				suma = 0
				for l in range(n):
					suma = suma  + M[j][l]*U[l][k]
				T[j][k] = suma
		for j in range(n):
			for k in range(n+1):
				U[j][k] = T[j][k]        
		for j in range(n):
			for k in range(n):
				suma = 0
				for l in range(n):
					suma = suma  + U[j][l]*M[k][l]
				T[j][k] = suma
		
	#EL P TOTAL#
		for j in range(n):
			for k in range(n):
				suma = 0
				for l in range(n):
					suma = suma + P[j][l]*W[l][k]
				PP[j][k] = suma
		for j in range (n):
			for k in range(n):
				W[j][k]=PP[j][k]
	#M2P2M1P1#
		L= funciones.mulMatrices(funciones.mulMatrices(M,P,n),L,n)            
	for j in range(n):
		for k in range(n):
			PPT[j][k]=PP[k][j]
	L=funciones.mulMatrices(L,PPT,n)
	L=funciones.inversa(L,n)
	Q=[]
	for s in range (n+1):
		Q.append(0)
	Lt=[]
	for s in range (n):
		Lt.append([0]*n)    
	z=[]
	for i in range (n):
		z.append(0)
	z[0]=T[0][n]*(L[0][0]**(-1))
	for j in range (1,n):       
		suma=0
		for k in range (j):
			suma+= L[j][k]*z[k]
		z[j]=(T[j][n]-suma)*(L[j][j]**(-1))
	matT=[]
	for i in range(n):
		matT.append([])
		for j in range(n):
			matT[i].append(T[i][j])
	
	for i in range (n):
		j=i+1
		if T[i][i]==0:
			p=i+1
			mayor = T[j][i]
			for j in range (i+2,n):
				if(abs(mayor) < abs(T[j][i])):
					mayor= T[j][i]
					p = j
			
			Q=T[i]
			T[i]=T[p]
			T[p]=Q
			k=z[i]
			z[i]=z[p]
			z[p]=k
		for j in range (i+1,n):
			w = T[j][i]*(T[i][i])**(-1)
			for k in range (i,n+1):
				T[j][k] = T[j][k] - (w*T[i][k])
				T[j][i]=0
			z[j] = z[j] - (w*z[i])


	W=[]
	for i in range (n):
		W.append(0)
	W[n-1]=z[n-1]/T[n-1][n-1]
	for j in range (n-2,-1,-1):
		suma=0
		for k in range (j+1,n):
			suma+= T[j][k]*W[k]
		W[j]=(z[j]-suma)/T[j][j]

	for i in range(n):
		for j in range (n):
			Lt[i][j]= L[j][i]
	y=[]
	for i in range (n):
		y.append(0)
	y[n-1]=W[n-1]/Lt[n-1][n-1]
	for j in range (n-2,-1,-1):
		suma=0
		for k in range (j+1,n):
			suma+= Lt[j][k]*y[k]
		y[j]=(W[j]-suma)*(Lt[j][j]**(-1))

	x=[]
	for i in range (n):
		x.append(0)
	for j in range(n):
		suma = 0
		for l in range(n):
			suma=suma+PPT[j][l]*y[l]
		x[j]=suma
	print "\n Resolucion por Algoritmo de Parlett y Reid "
	print " -------------------------------------------------"
	print " Matriz L"
	funciones.imprimeMatriz(L)
	print " Matriz P"
	funciones.imprimeMatriz(PP)
	print " Matriz T"
	funciones.imprimeMatriz(matT)
	print " Como A.x = b, en P.A.Pt = L.T.Lt:"
	return x