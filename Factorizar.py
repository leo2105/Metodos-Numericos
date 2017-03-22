import sys
from Tkinter import *
import tkMessageBox
import string
import math

class Factorizar:
    def __init__(self,A,dim,sym,b):
        self.A = A[:]
        self.b = b[:]
        self.n = dim
        self.can = sym
        
    def croutUTrivial(self):
        n = self.n
        a = []
        L = []
        U = []
        for i in range(n):
                a.append([])
                for j in range(n):
                        a[i].append(self.A[i][j])
        for i in range(n):
                L.append([])
                U.append([])
                for j in range(n):
                        L[i].append(0.0)
                        U[i].append(0.0)
        
        cont = 0

        correct = 1
 
        for k in range (n):
                for i in range(k,n):
                        res = 0.0
                        for p in range(k):
                                res += L[i][p]*U[p][k]
                                cont+=2
                        L[i][k] = a[i][k]-res
                        cont+=1
                for i in range (k,n):
                        res = 0.0
                        for p in range(k):
                                res += L[k][p]*U[p][i]
                                cont+=2
                        if L[k][k] == 0:
                            correct = 0
                            break
                        U[k][i] = (a[k][i]-res)/L[k][k]
                        cont+=2
                if correct == 0:
                    break
         
        return L,U,correct

    def croutUParcial(self):
        n = self.n
        a = []
        bb = self.b[:]
        L = []
        U = []
        for i in range(n):
                a.append([])
                for j in range(n):
                        a[i].append(self.A[i][j])
        for i in range(n):
                L.append([])
                U.append([])
                for j in range(n):
                        L[i].append(0.0)
                        U[i].append(0.0)
        
        correct = 1
        
        cont = 0
        P = []
        for i in range (n):
            P.append(i)
        for k in range (n):
                pos = -1
                maxi = -1000
                for i in range(k,n):   
                        if maxi < abs(a[i][k]):
                                pos = i
                                maxi = abs(a[i][k])
                a[pos], a[k] = a[k], a[pos]
                bb[pos], bb[k] = bb[k], bb[pos]

                P[k], P[pos] = P[pos], P[k]
         
                maxi = 0.0     
                for i in range(k,n):
                        res = 0.0
                        for p in range(k):
                                res += L[i][p]*U[p][k]
                                cont+=2
                        L[i][k] = a[i][k]-res
                        cont+=1
               
                for i in range (k,n):
                        res = 0.0
                        for p in range(k):
                                res += L[k][p]*U[p][i]
                                cont+=2
                        if L[k][k] == 0:
                            correct = 0
                            break
                        U[k][i] = (a[k][i]-res)/L[k][k]
                        cont+=2
                if correct == 0:
                    break
        return L,U,correct,bb
        
    def croutLTrivial(self):
        n = self.n
        a = []
        L = []
        U = []
        for i in range(n):
                a.append([])
                for j in range(n):
                        a[i].append(self.A[i][j])
        for i in range(n):
                L.append([])
                U.append([])
                for j in range(n):
                        L[i].append(0.0)
                        U[i].append(0.0)
        
        cont = 0
        correct = 1
 
        for k in range (n):
                for j in range(k,n):
                        res = 0.0
                        for p in range(k):
                                res += L[k][p]*U[p][j]
                                cont+=2
                        U[k][j] = a[k][j]-res
                        cont+=1
                for i in range (k,n):
                        res = 0.0
                        for p in range(k):
                                res += L[i][p]*U[p][k]
                                cont+=2
                        if U[k][k] == 0:
                            correct = 0
                            break
                        L[i][k] = (a[i][k]-res)/U[k][k]
                        cont+=2
                if correct == 0:
                    break
        return L,U,correct
        
    def croutLParcial(self):
        n = self.n
        a = []
        bb = self.b[:]
        L = []
        U = []
        for i in range(n):
                a.append([])
                for j in range(n):
                        a[i].append(self.A[i][j])
        for i in range(n):
                L.append([])
                U.append([])
                for j in range(n):
                        L[i].append(0.0)
                        U[i].append(0.0)
        
        cont = 0
        correct = 1
        P = []
        for i in range (n):
            P.append(i)
        for k in range (n):
                pos = -1
                maxi = 0.0
                for i in range(k,n):
                        if maxi < abs(a[i][k]):
                                pos = i
                                maxi = abs(a[i][k])
                a[pos], a[k] = a[k], a[pos]
                bb[pos], bb[k] = bb[k], bb[pos]

                P[pos], P[k] = P[k], P[pos]
               
         
                for j in range(k,n):
                        res = 0.0
                        for p in range(k):
                                res += L[k][p]*U[p][j]
                                cont+=2
                        U[k][j] = a[k][j]-res
                        cont+=1
                for i in range (k,n):
                        res = 0.0
                        for p in range(k):
                                res += L[i][p]*U[p][k]
                                cont+=2
                        if U[k][k] == 0:
                            correct = 0
                            break
                        L[i][k] = (a[i][k]-res)/U[k][k]
                        cont+=2
                if correct == 0:
                    break
        return L,U,correct,bb

    def choleskyFilas(self):
        if not self.can:
            tkMessageBox.showinfo('AVISO!', 'La matriz no es simetrica!')
            return
        n = self.n
        a = []
        GT = []
        G = []
        
        for i in range(n):
                a.append([])
                for j in range(n):
                        a[i].append(self.A[i][j])
         
        for i in range(n):
                GT.append([])
                G.append([])
                for j in range(n):
                        G[i].append(0.0)
                        GT[i].append(0.0)
        cont = 0         
        correct = 1
        for i in range (n):
                res = 0.0
                for k in range(i):
                        res += GT[k][i]*GT[k][i]
                        cont+=2
                if(a[i][i]-res) < 0:
                    correct = 0
                    break

                GT[i][i] = math.sqrt(a[i][i]-res)
                cont+=1
                for j in range (i,n):
                        res = 0.0
                        for k in range(i):
                                res += GT[k][i]*GT[k][j]
                                cont+=2
                        if GT[i][i] == 0:
                            correct = 0
                            break
                        GT[i][j] = (a[i][j]-res)/GT[i][i]
                        cont+=2
                if correct == 0:
                    break
        for i in range(n):
                for j in range(n):
                        G[i][j] = GT[j][i]
        return G,GT,correct
        
    def choleskyColumnas(self):
        if not self.can:
            tkMessageBox.showinfo('AVISO!', 'La matriz no es simetrica!')
            return
        n = self.n
        a = []
        GT = []
        G = []
        for i in range(n):
                a.append([])
                GT.append([])
                for j in range(n):
                        if j>=i:
                                a[i].append(self.A[i][j])
                                GT[i].append(self.A[i][j])
                        else:
                                GT[i].append(0.0)
                                a[i].append(self.A[i][j])
        for i in range(n):
                G.append([])
                for j in range(n):
                        G[i].append(0.0)
        cont = 0
        correct = 1
        info = 1
        for j in range (n):
                for i in range(j):
                        res = 0.0
                        for k in range(i):
                                res += GT[k][i]*GT[k][j]
                                cont+=2
                        if GT[i][i] == 0:
                            correct = 0
                            break
                        GT[i][j] = (GT[i][j]-res)/GT[i][i]
                        cont+=2
                        #print i, j, a[i][j]
                       
                if correct == 0:
                    break
                res = 0.0
                for k in range (j):
                        res += GT[k][j]*GT[k][j]
                        cont+=2
                #print j               
                temp = GT[j][j]-res
                if temp<=0:
                        info = 0
                        correct = 0
                        break
                GT[j][j] = math.sqrt(temp)
                #GT[j][j] = math.sqrt(a[j][j]-res)
                cont+=2
                #print j, a[j][j]
        info = 1
        for i in range(n):
                for j in range(n):
                        G[i][j] = GT[j][i]
        return G,GT,correct
