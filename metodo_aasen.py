#!usr/bin/python
from math import fabs

def imprimir_matriz(A):    
    for i in range(len(A)):
        print '|',
        for j in range(len(A[i])):
            if(j==len(A)):
                print '{0:8.4f}'.format(A[i][j]),
            else:
                print '{0:8.4f}'.format(A[i][j]),
        print '|'
    print

"""DESCOMPOSICION LTL' MEDIANTE EL METODO DE AASEN"""
def cambiar(a,b):
    temF=a
    a=b
    b=temF
    return a,b
def assen(A,n):
    """CREAMOS MATRIZ L,T"""
    """T"""    
    t=[]
    for i in range(n):
        t.append([])
        for j in range(n):
            t[i].append(0)
        
    """L"""    
    l=[]
    for i in range(n):
        l.append([])
        for j in range(n):
            l[i].append(0)
    """CREAMOS VECTORES ALFA,BETA,H,V,L0,IPVT"""
    """ALFA"""
    alfa = []
    for i in range(n):
        alfa = [0]*n    
    """BETA"""
    beta = []
    for i in range(n):
        beta = [0]*n    
    """H"""
    h = []
    for i in range(n):
        h = [0]*n
    """V"""
    v = []
    for i in range(n):
        v = [0]*n
    """L0"""
    l0 = []
    for i in range(n):
        l0 = [0]*n
    """IPVT"""
    ipvt = []
    for i in range(n):
        ipvt = [0]*n

    """valores iniciales de L"""
    for i in range(n):
        for j in range(n):
            if i<j:  l[i][j]=0
            if i==j:  l[i][j]=1
    """LLENAMOS IPVT"""    
    for i in range(n):
        ipvt[i]=i
    """FACTORIZACION"""    
    for j in range(n):
        if (j==0): h[0] = A[0][0]
        elif (j == 1):
            h[0] = beta[0]
            h[1] = A[1][1]
        else:
            l0[0] = 0
            for k in range(1,j):
                l0[k] = l[j][k]
            l0[j] = 1
            h[j] = A[j][j]
            h[0] = beta[0]*l0[1]
            for k in range(1,j):
                h[k] = beta[k-1]*l0[k-1] + alfa[k]*l0[k] + beta[k]*l0[k+1]
                h[j] -= l0[k]*h[k]
        if (j==0 or j == 1):
            alfa[j] = h[j]
        else:
            alfa[j] = h[j] - beta[j-1]*l[j][j-1]
        if (j < n-1):
            smax=0
            iq=j
            for k in range(j+1,n):
                suma=0
                for k1 in range(0,j+1):
                    suma -= l[k][k1]*h[k1]
                v[k] = A[k][j] + suma
                if (abs(v[k]) > smax):
                    smax = abs(v[k])
                    iq = k
            v[j+1],v[iq] = cambiar(v[j+1],v[iq])
            ipvt[j],ipvt[iq] = cambiar(ipvt[j],ipvt[iq])
            for k in range(1,j+1): l[j+1][k],l[iq][k] = cambiar(l[j+1][k],l[iq][k])
            for k in range(j+1,n): A[j+1][k],A[iq][k] = cambiar(A[j+1][k],A[iq][k])
            for k in range(j+1,n): A[k][j+1],A[k][iq] = cambiar(A[k][j+1],A[k][iq])
            beta[j] = v[j+1]
        if (j < n-2):
            for k in range(j+2,n): l[k][j+1] = v[k]
            if (v[j+1]):
                for k in range(j+2,n): l[k][j+1] /= v[j+1]
    print 'ALFA:'
    for j in range(n): print '{0:9.4f}'.format(alfa[j]),
    print
    print 'BETA:'
    for j in range(n): print '{0:9.4f}'.format(beta[j]),
    print
    for i in range(n):
        for j in range(n):
            if (i == j): t[i][j] = alfa[i]
            elif (abs(i-j)==1): 
                if(i < j): t[i][j] = beta[i]
                else: t[i][j] = beta[j]
            else: t[i][j] = 0
    print 'MATRIZ TRIDIAGONAL T:'
    for i in range(n):
        for j in range(n):
            print '{0:9.4f}'.format(t[i][j]),
        print
    print 'MATRIZ L:'
    for i in range(n):
        for j in range(n): print '{0:9.4f}'.format(l[i][j]),
        print
    #for j in range(n): print ipvt[j]+1
    return (alfa,beta)

def iterativo(alfa,beta,a_inicial,a_final,n):
    """P"""
    p = []
    for i in range(n):
        p = [0]*n
    a = 1.0
    while(abs(a-a_inicial)>0.5):
        p[0] = 1.0
        p[1] = alfa[0] - a_inicial
        for k in range(2,n,1):
            p[k] = (alfa[k-1] - a_inicial)*p[k-1] - (beta[k-2]**2)*p[k-2]
        contador = 0
        for i in range(n): print '{0:9.4f},'.format(p[i])
        for i in range(0,n-1,1):
            if (p[i]/p[i+1] < 0): contador += 1
        a = (a_final - a_inicial)/2  
        print 'De [',a_inicial,' a ',a,']','hay ',contador,' valores propios'
    
def metodo_biseccion(A,n):
    """ALFA"""
    alfa = []
    for i in range(n):
        alfa = [0]*n    
    """BETA"""
    beta = []
    for i in range(n):
        beta = [0]*n 
    """ALMACENAMOS LOS VALORES DE LA TRIDIAGONAL DE LA MATRIZ A"""    
    (alfa,beta) = assen(A,n)    
    a_inicial = 0
    a_final = 20    
    print 'polinomios:'
    iterativo(alfa,beta,a_inicial,a_final,n)
n=5
A=[[6.0,0.0,-1.0,0.0,0.0],[-3.0,3.0,0.0,0.0,0.0],[0.0,-1.0,9.0,0.0,0.0],[0.0,-1.0,-8.0,11.0,-2.0],[-3.0,-1.0,0.0,0.0,4.0]]
imprimir_matriz(A)
#metodo_biseccion(A,n)
assen(A,n)
