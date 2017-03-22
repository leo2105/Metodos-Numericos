import numpy as np
from scipy import linalg

def ModifiedGramSchmidt(X):
    rowsA,colsA=X.shape
    #Initialize Q, the array of vectors which are the vectors orthogonal to the vectors in X
    Q=np.zeros([rowsA,colsA])
    r=np.zeros([rowsA,colsA])
    for k in range(0,rowsA):
        #Step 1
        #Get the Frobenius or 2-norm of the kth vector in X
        r[k,k] = linalg.norm(X[:,k])
        Q[:,k] = (1.0/r[k,k])*X[:,k]
        #Step 2
        for j in range(k+1,rowsA):
            r[k,j] = np.inner(X[:,j],Q[:,k])
            '''
            Step 3
            Subtract off the projection once the new vector Q[:,k] is found
            '''
            X[:,j] = X[:,j] - r[k,j]*Q[:,k]
    print Q
    
def main():
    X=np.array([[-4.0,2.0,2.0],[3.0,-3.0,6.0],[6.0,6.0,0.0]])
    ModifiedGramSchmidt(X)

if __name__ == '__main__':
    main()
