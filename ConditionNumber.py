import numpy as np
import numpy.linalg as LA
from Tkinter import *
import tkMessageBox


class ConditionNumber:
    def __init__(self,A,dim):
        self.A = A
        self.n = dim
        self.graphics()
        
    def graphics(self):
        self.mGui = Toplevel()
        self.mGui.geometry('400x140+450+300')
        self.mGui.title('Numero de Condicion de una Matriz')
            
        mbotonTrivial = Button(self.mGui, text = 'K_1(A)', 
                command = self.cond_1).place(x=20, y = 20)
        mbotonParcial = Button(self.mGui, text = 'K_2(A)', 
                command = self.cond_2).place(x=20, y = 60)
        mbotonParcial = Button(self.mGui, text = 'K_inf(A)', 
                command = self.cond_inf).place(x=20, y = 100)

    def norm_1(self,A):
        n = self.n
        ret = -np.inf
        for j in range(n):
            tmp = 0
            for i in range(n):
                tmp += abs(A[i][j])
            if(tmp > ret):
                ret = tmp
        return ret

    def norm_2(self,A):
        ret = LA.norm(A,2)
        return ret

    def norm_inf(self,A):
        n = self.n
        ret = -np.inf
        for i in range(n):
            tmp = 0
            for j in range(n):
                tmp += abs(A[i][j])
            if(tmp > ret):
                ret = tmp
        return ret

    def cond_1(self):
        ret = 0
        out = 'Numero de Condicion\n\n'     
        if(np.isfinite(LA.cond(self.A))):
            Ainv = LA.inv(self.A)
            ret = self.norm_1(self.A)*self.norm_1(Ainv)
            out += 'K(A) = ' + str(ret) + '\n'
        else:
            out += 'Matriz Singular'

        text = Text(self.mGui)
        text.insert(INSERT, out)
        text.insert(END, '...')
        text.place(x=100,y=20)
        return ret

    def cond_2(self):
        ret = 0
        out = 'Numero de Condicion\n\n'     
        if(np.isfinite(LA.cond(self.A))):
            Ainv = LA.inv(self.A)
            A = self.A
            ret = self.norm_2(self.A)*self.norm_2(Ainv)
            out += 'K(A) = ' + str(ret) + '\n'
        else:
            out += 'Matriz Singular'
        text = Text(self.mGui)
        text.insert(INSERT, out)
        text.insert(END, '...')
        text.place(x=100,y=20)
        return ret

    def cond_inf(self):
        ret = 0
        out = 'Numero de Condicion\n\n'     
        if(np.isfinite(LA.cond(self.A))):
            Ainv = LA.inv(self.A)
            ret = self.norm_inf(self.A)*self.norm_inf(Ainv)
            out += 'K(A) = ' + str(ret) + '\n'
        else:
            out += 'Matriz Singular'
        text = Text(self.mGui)
        text.insert(INSERT, out)
        text.insert(END, '...')
        text.place(x=100,y=20)
        return ret
