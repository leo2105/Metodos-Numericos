import numpy as np
def potencia(A,X,eps,max_iter):
    l=0
    num_iter=0
    err=1
    continuar=True
    while (num_iter<=max_iter) and continuar:
        Y = A.dot(X)
        m = np.max(np.abs(Y))
        c1=m
        dc=np.abs(l-c1)
        Y=(1/c1)*Y
        dv=np.linalg.norm(X-Y)
        err=np.max([dc,dv])
        X=Y
        l = c1
        if err<=eps:
            continuar = False
        else:
            num_iter+=1
        pass
	print(X)
    V=X
    print("No. Iter. = {0:d}".format(num_iter))
    return(l,V,err)

A= np.array([[0.65,0.15],[0.35,0.85]],dtype='f')
X0= np.array([1,1],dtype='f').T
eps =1E-9
max_iter=100
(l,V,e)=potencia(A,X0,eps,max_iter)
print(l,V,e)
