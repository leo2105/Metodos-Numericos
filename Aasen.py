import string
import funciones

def metodoAasen(aa,bb,nn):
	global aux,P,T,I,P_aux,b_aux,pvt,L,Lt,Pt,A,b,n
	A = aa[:]
	b = bb[:]
	n = nn
	aux=0.0	
	P= [ [ 0 for i in range(n) ] for j in range(n) ]
	T,I,P_aux,b_aux,pvt,L,Lt,Pt = [],[],[],[],[],[],[],[]
	for i in range(n+1):
		if i!=n:       
			T.append([])
		I.append([])
		pvt.append(i)
		L.append([])
		Lt.append([])
		Pt.append([])
		b_aux.append(0.0)
		P_aux.append(0.0)
		for j in range(n+1):
			if i!=n and j !=n:
				T[i].append(0.0)
			Lt[i].append(0.0)
			Pt[i].append(0.0)
			if i==j:               
				I[i].append(1.0)
				L[i].append(1.0)
			else:
				I[i].append(0.0)
				L[i].append(0.0)

	a=[ [ 0 for i in range(n+1) ] for j in range(n+1) ]
	a=funciones.paso(A,n)
	#PIVOTACION
	alfa,beta,h,l,v = [],[],[],[],[]
	smax=0.0
	iq=0
	iaux=0
	suma=0.0
	aux=0.0 
	a=[ [ 0 for i in range(n+1) ] for j in range(n+1) ]
	a=funciones.paso(A,n)
	for i in range (n+1):
		alfa.append(0.0)
		beta.append(0.0)
		h.append(0.0)
	for i in range (n+2):
		l.append(0.0)        
		v.append(0.0)

	### EMPIEZA  ################
	for j in range(1,n+1):
		if j == 1:
			h[j]=a[1][1]
		elif j==2:
			h[1]= beta[1]
			h[2]= a[2][2]
		else :
			l[0]=0.0
			l[1]=0.0
			for k in range(2,j):
				l[k]=L[j][k]
			l[j]=1.0
			h[j]=a[j][j]
			for k in range(1,j):
				h[k]=beta[k-1]*l[k-1] + alfa[k]*l[k] + beta[k]*l[k+1]
				h[j] = h[j] - l[k]*h[k]
		if j==1 or j==2:
			alfa[j]=h[j]
		else:
			alfa[j]=h[j] - beta[j-1]*L[j][j-1]

		if j<=n-1:
			smax=0.0
			iq = j
			for k in range (j+1,n+1):
				suma=0.0
				for e in range (1,j+1):
					suma -= L[k][e]*h[e]
				v[k]=a[k][j] +suma
				if (abs(v[k])>=smax):###posible >=
					smax=abs(v[k])
					iq=k
			aux=v[j+1]
			v[j+1]=v[iq]
			v[iq]=aux

			for k in range (2,j+1):
				aux= L[j+1][k]
				L[j+1][k]=L[iq][k]
				L[iq][k]=aux

			iaux = pvt[j+1]
			pvt[j+1] = pvt[iq]  
			pvt[iq] = iaux
			for k in range(j+1,n+1):
				aux=a[j+1][k]
				a[j+1][k]=a[iq][k]
				a[iq][k]=aux
			for k in range(j+1,n+1):
				aux=a[k][j+1]
				a[k][j+1]=a[k][iq]
				a[k][iq]=aux
			beta[j]=v[j+1]

		if j<=n-2:
			for k in range(j+2,n+1):
				L[k][j+1]=v[k]
			if (v[j+1]!= 0.0):
				for k in range (j+2,n+1):
					L[k][j+1]= L[k][j+1]/v[j+1]

	for j in range (n-1):
		T[j][j]=alfa[j+1]
		T[j+1][j]=beta[j+1]
		T[j][j+1]=beta[j+1]

	T[n-1][n-1]=alfa[n]

	for i in range (1,n+1):
		P_aux[i]=I[pvt[i]]

	for i in range (n):
		for j in range (n):
			P[i][j]= P_aux[i+1][j+1]
	#FIN PIVOTE
	for i in range(n):
		b_aux[i]=b[pvt[i+1]-1]   

	#LZ = b_aux
	j = 0
	z = []
	for i in range(n):
		z.append(0.0)
	while j < n:
		res = b_aux[j]
		for k in range (j):
			res -= L[j+1][k+1] *z[k]
		res /= float(L[j+1][j+1])
		z[j]=res
		j+=1

	# GAUS Tw =Z
	a = []
	for i in range(n):
		a.append([])
		for j in range(n):
			a[i].append(float(T[i][j]))

	for i in range(n):
		a[i].append(z[i])

	maxi = 0
	pos_maxi=-1
	P1 = []
	h1=0.0
	for i in range(n):
		P1.append(i)
	for i in range(n-1):
		maxi = 0
		pos_maxi=-1
		for p in range(i,n):
			if maxi< abs(a[p][i]):
				maxi = abs(a[p][i])
				pos_maxi = p
		a[i], a[pos_maxi] = a[pos_maxi], a[i]
		P1[i], P1[pos_maxi] = P1[pos_maxi], P1[i]
		for j in range(i+1, n):
			h1 = a[j][i]/float(a[i][i])
			for k in range(i, n+1):
				a[j][k] -= float((h1)*(a[i][k]))
	w = []
	for i in range(n):
		w.append(0.0)

	j = n-1
	while j>=0:
		res = a[j][n]
		for k in range (j+1, n):
			res -= a[j][k] *w[k]
		res /= float(a[j][j])

		w[j] = res
		j-=1
	#LY = w
	for i in range(n):
		for j in range(n):
			Lt[i][j]=L[j+1][i+1]

	j = n-1
	y = []

	for i in range(n):
		y.append(0.0)

	while j >=0:
		res2 = 0.0
		for k in range (j+1,n):
			res2 += Lt[j][k]*y[k]
		y[j] = float(w[j]-res2)/Lt[j][j]
		j-=1
	#X = P(t)y
	x = []
	for i in range(n):
		x.append(0.0)

	for i in range(n):
		for j in range(n):
			Pt[i][j]=P[j][i]

	for i in range(n):
		aux=0.0
		for j in range(n):
			aux+= Pt[i][j]*y[j]
		x[i]=aux
	print "\n Resolucion por Algoritmo de Aasen "
	print " -------------------------------------------------"
	print " Matriz P"
	funciones.imprimeMatriz(P)
	print " Matriz L"
	funciones.imprimeMatriz(funciones.transMatriz(Lt,n))
	print " Matriz T"
	funciones.imprimeMatriz(T)
	print " Como A.x = b, en P.A.Pt = L.T.Lt:"
	return x