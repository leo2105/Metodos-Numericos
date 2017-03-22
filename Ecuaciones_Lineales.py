import math
import numpy
from numpy import *
from numpy import dot

def Llenarmatriz(m):
    matriz=[]
    for i in range(m):
        matriz.append([])
        for j in range(m):
            matriz[i].append(0)
    return matriz

def multip(M1,M2,n):
    M=[]
    for i in range (n):
        M.append([0]*(n))
    for i in range (n):
        for j in range (n):
            suma=0
            for k in range (n):
                suma=suma+M1[i][k]*M2[k][j]
            M[i][j]=suma
    return M
  
def Gasi(A,b,n):
    x=[]
    for i in range(n):
        x.append([0]*(n))
    M=[]
    for i in range(n):
        M.append([0]*(n+1))
    for i in range(n):
        for j in range(n):
            M[i][j]=A[i][j]
    for i in range(n):
        M[i][n]=b[i]
    mayor=0
    Q=[]
    for s in range (n+1):
        Q.append([0])
    for i in range (n):
        j=i
        p=i
        mayor = M[j][i]
        for j in range (i+1,n):
            if(abs(mayor) < abs(M[j][i])):
                mayor= M[j][i]
                p = j
        for l in range (i,n+1):
            Q[l]=M[i][l]
            M[i][l]=M[p][l]
            M[p][l]=Q[l]
        for j in range (i+1,n):
            w = M[j][i]*(M[i][i])**(-1)
            for k in range (i,n+1):
                M[j][k] =M[j][k] - (w*M[i][k])
                M[j][i]=0
    x[n-1]=M[n-1][n]/M[n-1][n-1]
    for j in range (n-2,-1,-1):
        suma=0
        for k in range (j+1,n):
            suma=suma + M[j][k]*x[k]
        x[j]=(M[j][n]-suma)/M[j][j]
    return x
def Inversa(M,n):
    B=Llenarmatriz(n)
    I=identity(n)
    for i in range(n):
        B[i]=Gasi(M,I[i],n)
    return B
def Gauss(A,b,n):
    print "Metodo de Gauss"
    print "Resover Gauss mediante:"
    print "1.-Sin pivoteo"
    print "2.-Con pivoteo"
    x=[]
    for i in range(n):
        x.append([0]*(n))  
    h=input("")
    if h==1:
        for k in range(0,n-1):
            for i in range(k+1,n):
                m=(A[i][k]*1.0)/A[k][k]
                for j in range(k,n):
                    A[i][j]=A[i][j]-m*A[k][j]
                b[i]=b[i]-m*b[i-1]
        print "La matriz escalonada reducida es:"
        M=[]
        for i in range(n):
            M.append([0]*(n+1))
        for i in range(n):
            for j in range(n):
                M[i][j]=A[i][j]
        for i in range(n):
            M[i][n]=b[i]
        print numpy.array(M)   
        x[n-1]=(M[n-1][n]*1.0)/M[n-1][n-1]
        for j in range(n-2,-1,-1):
            suma=0
            for k in range(j+1,n):
                suma=suma+M[j][k]*x[k]
            x[j]=(M[j][n]-suma)*1.0/M[j][j]
        print "La solucion es:"
        print x
    else:
        M=[]
        for i in range(n):
            M.append([0]*(n+1))
        for i in range(n):
            for j in range(n):
                M[i][j]=A[i][j]
        for i in range(n):
            M[i][n]=b[i]
        mayor=0
        Q=[]
        for s in range (n+1):
            Q.append([0])
        print " La matriz ampliada es:"
        print numpy.array(M)
        print "La matriz escalonada ampliada es:"
        for i in range (n):
            j=i
            p=i
            mayor = M[j][i]
            for j in range (i+1,n):
                if(abs(mayor) < abs(M[j][i])):
                    mayor= M[j][i]
                    p = j
            for l in range (i,n+1):
                Q[l]=M[i][l]
                M[i][l]=M[p][l]
                M[p][l]=Q[l]
            for j in range (i+1,n):
                w = M[j][i]*(M[i][i])**(-1)
                for k in range (i,n+1):
                    M[j][k] =M[j][k] - (w*M[i][k])
                    M[j][i]=0            
        print numpy.array(M)
        x[n-1]=M[n-1][n]/M[n-1][n-1]
        for j in range (n-2,-1,-1):
            suma=0
            for k in range (j+1,n):
                suma=suma + M[j][k]*x[k]
            x[j]=(M[j][n]-suma)/M[j][j]
        print "La solucion es:"
        print x
def LU1(A,b,n):
    print "Metodo LU1"
    x=[]
    y=[]
    for i in range(n):
        y.append([0]*(n))    
        x.append([0]*(n))
    print "Resover LU1 mediante:"
    print "1.-Sin pivoteo"
    print "2.-Con pivoteo"
    h=input("")
    if h==1:
        print "La matriz ampliada es:"
        M=[]
        for i in range(n):
            M.append([0]*(n+1))
        for i in range(n):
            for j in range(n):
                M[i][j]=A[i][j]
        for i in range(n):
            M[i][n]=b[i]
        print numpy.array(M)
        L = []
        U = []
        for i in range (n):
            L.append([0]*(n))
            U.append([0]*(n))
            p = 0
        for i in range (n):
            U[i][i]=float(1)
        for i in range (n):
            for j in range(i,n):
                suma=0
                for p in range (0,i):
                    suma=suma+L[j][p]*U[p][i]
                L[j][i] = M[j][i] - suma
            for j in range(i+1,n):
                suma=0
                for p in range (0,i):
                    suma=suma+L[i][p]*U[p][j]
                U[i][j]=(M[i][j]-suma)*(L[i][i])**(-1)
        print "la matriz L es:"
        print numpy.array(L)
        print "La matriz U es:"
        print numpy.array(U)
        y[0]=M[0][n]*(L[0][0]**(-1))
        for j in range (1,n,1):
            suma=0
            for k in range (j):
                suma+= L[j][k]*y[k]
            y[j]=(M[j][n]-suma)*(L[j][j]**(-1))
        x[n-1]=y[n-1]/U[n-1][n-1]
        for j in range (n-2,-1,-1):
            sum=0
            for k in range (j+1,n):
                suma+= U[j][k]*x[k]
            x[j]=(y[j]-suma)*(U[j][j]**(-1))
        print "La solucion es:"
        print x
    else:
        print "La matriz ampliada es:"
        M=[]
        for i in range(n):
            M.append([0]*(n+1))
        for i in range(n):
            for j in range(n):
                M[i][j]=A[i][j]
        for i in range(n):
            M[i][n]=b[i]
        print numpy.array(M)
        Q = []
        p = 0
        L = []
        U = []
        for i in range (n):
            L.append([0]*(n))
            U.append([0]*(n))
        for i in range (n):
            U[i][i]=float(1)
        for i in range (n+1):
            Q.append(0)
        for i in range (n):
            for j in range(i,n):
                suma=0
                for p in range (0,i):
                    suma=suma+L[j][p]*U[p][i]
                L[j][i]=M[j][i]-suma
            p=i
            mayor=L[i][i]
            for j in range (i+1,n):
                if(abs(mayor) < abs(L[j][i])):
                    mayor=L[j][i]
                    p=j
            for l in range (i,n):
                Q[l]=L[i][l]
                L[i][l]=L[p][l]
                L[p][l]=Q[l]
            for l in range (i,n+1):
                Q[l]=M[i][l]
                M[i][l]=M[p][l]
                M[p][l]=Q[l]
            for j in range(i+1,n):
                suma=0
                for p in range (0,i):
                    suma=suma+L[i][p]*U[p][j]
                U[i][j]=(M[i][j]-suma)*(L[i][i])**(-1)
        print "la matriz L es:"
        print numpy.array(L)
        print "La matriz U es:"
        print numpy.array(U)
        y[0]=M[0][n]*(L[0][0]**(-1))
        for j in range (1,n,1):
            suma=0
            for k in range (j):
                suma+= L[j][k]*y[k]
            y[j]=(M[j][n]-suma)*(L[j][j]**(-1))
        x[n-1]=y[n-1]/U[n-1][n-1]
        for j in range (n-2,-1,-1):
            suma=0
            for k in range (j+1,n):
                suma=suma+ U[j][k]*x[k]
            x[j]=(y[j]-suma)*(U[j][j]**(-1))
        print "La solucion es:"
        print x        
        
def LDLt(A,b,n):
    print "Factorizacion LDLt"
    B=Llenarmatriz(n)
    z=[]
    v=[]
    for i in range(n):
        v.append([0]*(n))
        z.append([0]*(n))
    for i in range(n):
        for j in range(n):
            B[i][j]=A[j][i]
    if numpy.array_equal(A,B):
        print "La matriz es simetrica"
        print "La matriz ampliada es:"
        print numpy.array(A)
        L = Llenarmatriz(n)
        D = Llenarmatriz(n)
        Lt = Llenarmatriz(n)
        DLt = Llenarmatriz(n)
        for i in range(n):
            L[i][i]=1
        for k in range (n):
            suma = 0
            for p in range(k):
                suma = suma + (L[k][p]**2)*D[p][p]
            D[k][k] = A[k][k] - suma
            if D[k][k]!=0:
                for i in range(k+1,n):
                    suma = 0
                    for p in range (k):
                        suma = suma + L[i][p]*L[k][p]*(D[p][p])
                    L[i][k] = (A[i][k] - suma)*(D[k][k]**(-1))
            else:
                break
        for i in range(n):
            for j in range (n):
                Lt[i][j]= L[j][i]
        for i in range (n):
            for j in range (n):
                for k in range (n):
                    DLt[i][j] = DLt[i][j] + D[i][k]*Lt[k][j]
        print "La matriz L es:"
        print numpy.array(L)
        print "La matriz D es:"
        print numpy.array(D)
        v=Gasi(L,b,n)
        z=Gasi(DLT,v,n)
        print z
     
    else:
        print "La matriz de representacion no es simetrica"
        C=Llenarmatriz(n)
        d=Llenarmatriz(n)
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    C[i][j]=C[i][j]+B[i][k]*A[k][j]
        print "Convirtiendola a simetrica:"
        print numpy.array(C)
        L = []
        D = []
        Lt = []
        DLt = []
        for i in range(n):
            L.append([0]*(n))
            D.append([0]*(n))
            Lt.append([0]*(n))
            DLt.append([0]*(n))
        for i in range(n):
            L[i][i]=1
        for k in range (n):
            suma = 0
            for p in range(k):
                suma = suma + (L[k][p]**2)*D[p][p]
            D[k][k] = C[k][k] - suma
            if D[k][k]!=0:
                for i in range(k+1,n):
                    suma = 0
                    for p in range (k):
                        suma = suma + L[i][p]*L[k][p]*(D[p][p])
                    L[i][k] = (C[i][k] - suma)*(D[k][k]**(-1))
            else:
                break
        for i in range(n):
            for j in range (n):
                Lt[i][j]= L[j][i]
        for i in range (n):
            for j in range (n):
                for k in range (n):
                    DLt[i][j] = DLt[i][j] + D[i][k]*Lt[k][j]
        print "La matriz L es:"
        print numpy.array(L)
        print "La matriz D es:"
        print numpy.array(D)
        d=dot(B,b)
        M=[]
        for i in range(n):
            M.append([0]*(n+1))
        for i in range(n):
            for j in range(n):
                M[i][j]=C[i][j]
        for i in range(n):
            M[i][n]=d[i]
        X=[]
        for s in range (n):
            X.append(0)
        Z=[]
        for s in range (n):
            Z.append(0)
        Z[0]=M[0][n]*(L[0][0]**(-1))
        for j in range (1,n,1):
            suma=0
            for k in range (j):
                suma=suma +  L[j][k]*Z[k]
            Z[j]=(M[j][n]-suma)*(L[j][j]**(-1))
        X[n-1]=Z[n-1]/DLt[n-1][n-1]
        for j in range (n-2,-1,-1):
            suma=0
            for k in range (j+1,n):
                suma=suma+ DLt[j][k]*X[k]
            X[j]=(Z[j]-suma)*(DLt[j][j]**(-1))
        print "La solucion al sistema de ecuaciones es:"
        print X
        
def Cholesky(A,b,n):
    print "Factorizacion de Cholesky: GGt."
    B=Llenarmatriz(n)
    for i in range(n):
        for j in range(n):
            B[i][j]=A[j][i]
    print "Factorizar con el metodo de Cholesky:"
    print "1.-Sin pivoteo."
    print "2.-Con pivoteo"
    r=input("")
    if r==1:
        if A[0][0]>0:
            if numpy.array_equal(A,B):
                Chol1(A,b,n)
            else:
                C=Llenarmatriz(n)
                for i in range(n):
                    for j in range(n):
                        for k in range(n):
                            C[i][j]=C[i][j]+B[i][k]*A[k][j]
                p=numpy.array(b)
                q=numpy.array(B)
                s=dot(q,p)
                print "Convirtiendola a simetrica:"
                print numpy.array(C)
                Chol1(C,s,n)
    else:
        if A[0][0]>0:
            if numpy.array_equal(A,B):
                Cholcp1(A,b,n)
            else:
                D=Llenarmatriz(n)
                for i in range(n):
                    for j in range(n):
                        for k in range(n):
                            D[i][j]=D[i][j]+B[i][k]*A[k][j]
                p=numpy.array(b)
                q=numpy.array(B)
                s=dot(q,p)
                print "Convirtiendola a simetrica:"
                print numpy.array(D)
                Cholcp1(D,s,n)
def Chol1(A,b,n):
    G=Llenarmatriz(n)
    Gt=Llenarmatriz(n)
    for k in range(n):
        suma=0
        for p in range(k):
            suma=suma+((G[k][p])**2)
        G[k][k]=sqrt(A[k][k]-suma)
        for i in range(k+1,n):
            suma=0
            for p in range(k):
                suma=suma+(G[i][p]*G[k][p])
            G[i][k]=(A[i][k]-suma)*((G[k][k])**-1)
    print "La matriz G es:"
    print numpy.array(G)
    M=[]
    print "La matriz ampliada es:"
    for i in range(n):
        M.append([0]*(n+1))
    for i in range(n):
        for j in range(n):
            M[i][j]=A[i][j]
    for i in range(n):
        M[i][n]=b[i]
    print numpy.array(M)
    x=[]
    y=[]
    for s in range (n):
        x.append([0])
        y.append([0])
    for i in range(n):
        for j in range(n):
            Gt[i][j]=G[j][i]
    y=Gasi(G,b,n)
    x=Gasi(Gt,y,n)
    print "La solucion es:"
    print x
    
def Cholcp1(A,b,n):
    G=Llenarmatriz(n)
    Gt=Llenarmatriz(n)
    P=Llenarmatriz(n)
    mayor=abs(A[0][0])
    for k in range(1,n):
        if mayor<abs(A[k][k]):
            mayor=abs(A[k][k])
        else:
            mayor =mayor
    for i in range(n):
        if mayor!=A[i][i]:
            continue
        else:
            break
    I=identity(n)
    N=identity(n)
    I[0]=I[i]
    I[i]=N[0]
    for i in range(n):
        for j in range(n):
            P[i][j]=I[j][i]
    C=dot(I,A)
    C=dot(C,P)
    for k in range(n):
        suma=0
        for p in range(k):
            suma=suma+((G[k][p])**2)
        G[k][k]=sqrt(C[k][k]-suma)
        for i in range(k+1,n):
            suma=0
            for p in range(k):
                suma=suma+(G[i][p]*G[k][p])
            G[i][k]=(C[i][k]-suma)/(G[k][k])
    print "La matriz G es:"
    print numpy.array(G)
    M=[]
    print "La matriz ampliada es:"
    for i in range(n):
        M.append([0]*(n+1))
    for i in range(n):
        for j in range(n):
            M[i][j]=A[i][j]
    for i in range(n):
        M[i][n]=b[i]
    print numpy.array(M)                                
    x=[]
    y=[]
    for s in range(n):
        x.append([0])
        y.append([0])
    for i in range(n):
        for j in range(n):
            Gt[i][j]=G[j][i]
    y=Gasi(G,b,n)
    x=Gasi(Gt,y,n)
    print "La solucion es:"
    print x                                    
                                    
def Aasen(A,b,n):
    print "Factorizacion mediante el metodo de Aasen"
    print "Factorizando:"
    print "1.-Sin pivoteo."
    print "2.-Con pivoteo."
    w=input("")
    if w==1:
        Aasensp(A,b,n)
    else:
        Aasencp(A,b,n)
def Aasensp(A,b,n):
    print "La matriz ampliada es:"
    M=[]
    for i in range(n):
        M.append([0]*(n+1))
    for i in range(n):
        for j in range(n):
            M[i][j]=A[i][j]
    for i in range(n):
        M[i][n]=b[i]
    print numpy.array(M)
    L = []
    T = []
    h = []
    l = []
    v = []
    mayor=0
    Q=[]
    for i in range (n):
        L.append([0]*(n))
        T.append([0]*(n+1))
    for i in range (n):
        h.append(0)
        v.append(0)
        l.append(0)
    for s in range (n+1):
        Q.append(0)
    for i in range (n):
        L[i][i]=1
    for j in range (n):
        if j==0:
            h[0]=M[0][0]
        else:
            if j==1:
                h[0]=T[1][0]
                h[1]=M[1][1]
            else:
                l[0]=0
                for k in range (1,j):
                    l[k]=L[j][k]
                l[j]=1
                h[j]=M[j][j]
                h[0]=T[0][0]*l[0]+T[1][0]*l[1]
                h[j]=h[j]-l[0]*h[0]
                for k in range (1,j):
                    h[k]= T[k][k-1]*l[k-1]+T[k][k]*l[k]+T[k+1][k]*l[k+1]
                    h[j]=h[j]-l[k]*h[k]
        if j==0 or j==1:
            T[j][j]=h[j]
        else:
            T[j][j]=h[j]-T[j][j-1]*L[j][j-1]
        if j <(n-1):
            for r in range (j+1,n):
                suma=0
                for k in range (0,j+1):
                    suma=suma+L[r][k]*h[k]
                v[r]=M[r][j]-suma
            T[j+1][j]=T[j][j+1]=v[j+1]
        if j<(n-2):
            for k in range (j+2,n):
                L[k][j+1]=v[k]*(v[j+1]**(-1))
    print "la matriz L es:"
    for i in range (n):
        print L[i]
    print "La matriz T es:"
    for i in range (n):
        print T[i][0:n]
    z=[]
    for i in range (n):
        z.append(0)
    z[0]=M[0][n]*(L[0][0]**(-1))
    for j in range (1,n):       
        suma=0
        for k in range (j):
            suma+= L[j][k]*z[k]
        z[j]=(M[j][n]-suma)*(L[j][j]**(-1))
    for i in range(n):
        T[i][n]=z[i]
    p=0
    for i in range (n):
        j=i+1
        if T[i][i]==0:
            p=i+1
            mayor = T[j][i]
            for j in range (i+2,n):
                if(abs(mayor) < abs(T[j][i])):
                    mayor= T[j][i]
                    p = j
            for l in range (i,n+1):
                Q[l]=T[i][l]
                T[i][l]=T[p][l]
                T[p][l]=Q[l]  
        for j in range (i+1,n):
            w = T[j][i]*(T[i][i])**(-1)
            for k in range (i,n+1):
                T[j][k] = T[j][k] - (w*T[i][k])
                T[j][i]=0
    W=[]
    for i in range (n):
        W.append(0)
    W[n-1]=T[n-1][n]/T[n-1][n-1]
    for j in range (n-2,-1,-1):
        suma=0
        for k in range (j+1,n):
            suma+= T[j][k]*W[k]
        W[j]=(T[j][n]-suma)/T[j][j]
    for i in range(n):
        for j in range (n):
            Lt[i][j]= L[j][i]
    x=[]
    for i in range (n):
        x.append(0)
    x[n-1]=W[n-1]/Lt[n-1][n-1]
    for j in range (n-2,-1,-1):
        suma=0
        for k in range (j+1,n):
            suma+= Lt[j][k]*x[k]
        x[j]=(W[j]-suma)*(Lt[j][j]**(-1))
    print "La solucion es:"
    print x
    
def Aasencp(A,b,n):
    print "La matriz ampliada es:"
    M=[]
    for i in range(n):
        M.append([0]*(n+1))
    for i in range(n):
        for j in range(n):
            M[i][j]=A[i][j]
    for i in range(n):
        M[i][n]=b[i]
    print numpy.array(M)
    L = []
    T = []
    h = []
    l = []
    v = []


    for i in range (n):
        L.append([0]*(n))
        T.append([0]*(n+1))

    for i in range (n):
        h.append(0)
        v.append(0)
        l.append(0)
    mayor=0
    Q=[]
    for s in range (n+1):
        Q.append(0)
    Q1=[]
    for s in range (n):
        Q.append(0)
    for i in range (n):
        L[i][i]=1
    I=[]
    for i in range (n):
        I.append([0]*(n))
    for i in range (n):
        I[i][i]=1
    for j in range (n):
        P=[]
        for k in range (n):
            P.append([0]*(n))
        for k in range (n):
            P[k][k]=1
        if j==0:
            h[0]=M[0][0]
        else:
            if j==1:
                h[0]=T[1][0]
                h[1]=M[1][1]
            else:
                l[0]=0
                for k in range (1,j):
                    l[k]=L[j][k]
                l[j]=1
                h[j]=M[j][j]
                h[0]=T[0][0]*l[0]+T[1][0]*l[1]
                h[j]=h[j]-l[0]*h[0]
                for k in range (1,j):
                    h[k]= T[k][k-1]*l[k-1]+T[k][k]*l[k]+T[k+1][k]*l[k+1]
                    h[j]=h[j]-l[k]*h[k]
        if j==0 or j==1:
            T[j][j]=h[j]
        else:
            T[j][j]=h[j]-T[j][j-1]*L[j][j-1]
            
        if j <(n-1):
            p=j+1
            for r in range (j+1,n):
                suma=0
                for k in range (0,j+1):
                    suma=suma+L[r][k]*h[k]
                v[r]=M[r][j]-suma
            mayor =v[j+1]
            for k in range (j+2,n):
                if mayor < abs(v[k]):
                    p=k
            q=v[p]
            v[p]=v[j+1]
            v[j+1]=q
            Q1=P[p]
            P[p]=P[j+1]
            P[j+1]=Q1
            for k in range (2,j+1):
                q=L[j+1][k]
                L[j+1][k]=L[p][k]
                L[p][k]=q

            for k in range (j+1,n):
                q=M[j+1][k]
                M[j+1][k]=M[p][k]
                M[p][k]=q
            for k in range (j+1,n):
                q=M[k][j+1]
                M[k][j+1]=M[k][p]
                M[k][p]=q
            T[j+1][j]=T[j][j+1]=v[j+1]
        if j<(n-2):
            for k in range (j+2,n):
                L[k][j+1]=v[k]
            if v[j+1]!=0:
                for k in range (j+2,n):
                    L[k][j+1]=L[k][j+1]*(v[j+1]**(-1))
            print 'L:',L
        I=multip(P,I,n)
    print "la matriz L es:"
    for i in range (n):
        print L[i][0:n]
    print "La matriz T es:"
    for i in range (n):
        print T[i][0:n]
    print 'La matriz P es:'
    for i in range (n):
        print I[i]
    IT=[]
    for i in range (n):
        IT.append([0]*(n))
    for i in range (n):
        for j in range (n):
            IT[i][j]=I[j][i]
    Q=[]
    for s in range (n+1):
        Q.append(0)
    Lt=[]
    for s in range (n):
        Lt.append([0]*n)    
    z=[]
    for i in range (n):
        z.append(0)
    B=[]
    for i in range(n):
        B.append(0)
    for i in range (n):
        suma=0
        for j in range (n):
            suma=suma+I[i][j]*M[j][n]
        B[i]=suma
    z[0]=B[0]*(L[0][0]**(-1))
    for j in range (1,n):       
        suma=0
        for k in range (j):
            suma+= L[j][k]*z[k]
        z[j]=(B[j]-suma)*(L[j][j]**(-1))
    
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
            suma=suma+IT[l][j]*y[l]
        x[j]=suma
    print "La solucion del sistema es:"
    print x
    
def Par_Reid(A,d,n):
    I=[]
    P=[]
    M=[]
    L=[]
    Z=[]
    N=[]
    U=[]
    T=[]
    G=[]
    F=[]
    S=[]
    PP=[]
    W=[]
    PPT=[]
    b=[]
    for i in range (n):
        I.append([0]*(n))
        PPT.append([0]*(n))
        P.append([0]*(n))
        W.append([0]*(n))
        M.append([0]*(n))
        L.append([0]*(n))
        Z.append([0]*(n))
        N.append([0]*(n+1))
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
        for j in range(n):
            N[i][j]=A[i][j]
    for i in range(n):
        N[i][n]=d[i]
    for i in range(n):
        for j in range(n+1):
            T[i][j]=N[i][j]
    print 'METODO PARLET-REID'
    print " La matriz ampliada es:"
    for i in range(n):
        print T[i]
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
    #multiplicacion PAPT#
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
    #multiplicacion MPAPTMT#                
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
        L= multip(multip(M,P,n),L,n)            
    for j in range(n):
        for k in range(n):
            PPT[j][k]=PP[k][j]
    L=multip(L,PPT,n)
    Z=Inversa(L,n)

    print 'La matriz L es:'
    for i in range (n):
        print Z[i]
    print 'La matriz tridiagonal T es:'
    for i in range (n):
        print T[i][0:n]
    print 'La matriz P es:'
    for i in range (n):
        print PP[i]
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
    print "La solucion del sistema es:"
    print x
    
def L1U(A,b,n):
    print "Factorizacion L1U:"
    print "La matriz ampliada es:"
    M=[]
    for i in range(n):
        M.append([0]*(n+1))
    for i in range(n):
        for j in range(n):
            M[i][j]=A[i][j]
    for i in range(n):
        M[i][n]=b[i]
    print numpy.array(M)
    L=Llenarmatriz(n)
    U=Llenarmatriz(n)
    for i in range(n):
        L[i][i]=float(1)
    for k in range(n):
        for j in range(k,n):
            suma=0
            for i in range(k):
                suma=suma+(L[k][i]*U[i][j])
            U[k][j]=A[k][j]-suma
        for i in range(k+1,n):
            suma=0
            for j in range(k):
                suma=suma+L[i][j]*U[j][k]
            L[i][k]=(A[i][k]-suma)*((U[k][k])**-1)
    print "La matriz L1 es:"
    print numpy.array(L)
    print "La matriz U es:"
    print numpy.array(U)
    x=[]
    for s in range (n):
        x.append(0)
    y=[]
    for s in range (n):
        y.append(0)
    y[0]=M[0][n]*(L[0][0]**(-1))
    for j in range (1,n,1):       
        suma=0
        for k in range (j):
            suma+= L[j][k]*y[k]
        y[j]=(M[j][n]-suma)*(L[j][j]**(-1))
    x[n-1]=y[n-1]/U[n-1][n-1]
    for j in range (n-2,-1,-1):
        suma=0
        for k in range (j+1,n):
            suma+= U[j][k]*x[k]
        x[j]=(y[j]-suma)*(U[j][j]**(-1))
    print "La solucion es:"
    print x
    
#Funcion principal
def SEL():
    print "Metodos para la resolucion de Sistemas de Ecuaciones Lineales y Factorizacion de Matrices:"
    print "Ingrese la cantidad de variables a resolver:"
    n=input("")
    A=Llenarmatriz(n)
    b=[]
    x=[]
    for i in range(n):    
        b.append([0]*(n))
    for i in range(n):
        print "Ingrese los %d elementos de la fila %d" %(n,i+1)
        for j in range(n):
            A[i][j]=input("")
    print "Ingrese los terminos independientes:"
    for i in range(n):
        print "Ingrese el %d termino:" %(i+1)
        b[i]=input("")
    print "Indique el metodo que desea usar:"
    print "1.-Eliminacion de Gauss."
    print "2.-Metodo de LU1."
    print "3.-Metodo de L1U."
    print "4.-Factorizacion LDLt."
    print "5.-Factorizacion de Cholesky."
    print "6.-Metodo de Aasen."
    print "7.-Metodo de Parlett-Reid."
    a=input("")
    if a==1:
        Gauss(A,b,n)
    else:
        if a==2:
            LU1(A,b,n)
        else:
            if a==3:
                L1U(A,b,n)
            else:
                if a==4:
                    LDLt(A,b,n)
                else:
                    if a==5:
                        Cholesky(A,b,n)
                    else:
                        if a==6:
                            Aasen(A,b,n)
                        else:
                            if a==7:
                                Par_Reid(A,b,n)
if __name__ == '__main__':
	SEL()
