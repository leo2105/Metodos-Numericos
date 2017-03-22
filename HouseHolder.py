from  math import *
#Transformacion de Matriz A, columnas 1 a n
class HouseHolder:
    def __init__(self,A,m,n,b):
        self.A = A
        self.m = m
        self.n = n
        self.b = b
        self.X = [0]*self.m

    def all(self):
        self.out = 'HouseHolder\n\n'
        self.houseHolder()
        m = self.m 
        n = self.n
        A = self.A[:]
        b = self.b[:]

        self.solHouseHolder()
        X = self.X
        
        self.out += str(X) + '\n'

        return self.out

    def houseHolder(self):
        m = self.m
        n = self.n
        A = self.A
        b = self.b
        w = [0]*m
        for j in range (n):
            #sacamos maximo de columnas
                MaxCol = A[j][j]
                for k in range(j+1,m):
                    MaxCol = max(MaxCol, A[k][j])
                if MaxCol==0:
                    return -1
                psum = 0
                for k in range (j,m):
                    psum = psum + A[k][j]*A[k][j]
                ssign = copysign(1,A[j][j])
                sigma = sqrt(psum)*ssign
                for k in range (j,m):
                    w[k] = A[k][j]
                w[j] = w[j]+sigma
                betha = 0
                psum = 0
                for k in range(j,m):
                    psum = psum+ w[k]*w[k]
                betha = float(2/psum)
                A[j][j] = -sigma
                for l in range(j+1,n):
                    s = 0
                    for k in range(j,m):
                        s = s+w[k]*A[k][l]
                    for k in range(j,m):
                        A[k][l] = A[k][l]-w[k]*s*betha
                #Transformar vector B
                s = 0
                for k in range(j,m):
                    s = s+w[k]*b[k]
                for k in range(j,m):
                    b[k] = b[k] - w[k]*s*betha

        #limpiar Matriz A
        for x in range(n):
            for y in range(n):
                if x>y:
                    A[x][y]=0
        for x in range(n,m):
            b[x]=0
            for y in range(n):
                A[x][y]=0
        self.A = A
        self.b = b

    def solHouseHolder(self):
        n = self.n
        A = self.A
        b = self.b
        X = self.X
        j = n-1
        while j>=0:
            psum = 0
            for k in range(j+1,n):
                psum = psum + A[j][k]*X[k]
            X[j] = float((b[j]-psum)/A[j][j])
            j=j-1
        self.A = A
        self.b = b
        self.X = X

    def residuosCuadrado(self):
        b = self.b
        res = 0
        for k in range(self.n, self.m):
            res = res + b[k]*b[k]
        return str(res)
