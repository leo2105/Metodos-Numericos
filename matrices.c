#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "matrices.h"

float ** ingreso_matriz(int n){
    float**A;
    int i,j;
    
    A= malloc(n*sizeof(int*));
  
    for(i=0;i<n;i++) A[i]=malloc(n*sizeof(float));
    //insercion de elementos a la matriz
    
    for(i=0;i<n;i++){
        for(j=0;j<n;j++){
            printf("ingrese numero A[%d][%d]:",i+1,j+1);
            scanf("%f",&A[i][j]);
        }
    }
    
    return A;
}

float * ingreso_vector(int n){
    float*b;
    int i; 
   
    b= malloc(n*sizeof(float));

    for(i=0;i<n;i++){
        printf("ingrese numero b[%d]:",i+1);
        scanf("%f",&b[i]);
    }

    return b;
}

void imprimir_matriz(float**A,int n){
    int i,j;
    for(i=0;i<n;i++){
        for(j=0;j<n;j++){
            printf("%.3f ",A[i][j]);
        }
        printf("|\n");
    }
}

void imprimir_matriz_sol(float**A,float*b,int n){
    int i,j;
    for(i=0;i<n;i++){
        for(j=0;j<n;j++){
            printf("%.0f ",A[i][j]);
        }
        printf("| %.0f\n",b[i]);
    }
}

void libera_matriz(float**A,int n){
    int i;
    for(i=0;i<n;i++)
        free(A[i]);
    free(A);
};

void libera_vector(float*b){
    free(b);
};

void eliminacion_gauss(float**A,float*b,int n){
    int k,i,j;
    float m;
    float *x;
    
    x= malloc(n*sizeof(float));
    
    for(k=0;k<n-1;k++){
        for(i=k+1;i<n;i++){
            m=A[i][k]/A[k][k];
            for(j=k+1;j<n;j++){
                A[i][j]=A[i][j] - m*A[k][j];
            }
            b[i] = b[i] - m*b[k];        
        }    
    }
    
    /*sustitucion regresiva*/
    x[n-1]=b[n-1]/A[n-1][n-1];

    for(i=n-2;i>=0;i--){
        x[i]=b[i];
        for(j=i+1;j<n;j++){
            x[i]=x[i] - A[i][j]*x[j];
        }
        x[i]=x[i]/A[i][i];
    }

    printf("el vector solucion es: x[");
    for(j=0;j<n;j++){
        printf("%.1f,",x[j]);
    }
    printf("]\n");

    libera_vector(x);
}
/*
void eliminacion_gauss_jordan(float**A,float*b,int n){
    int i,j,k,l;
    double aux,m,s;
    
    float *x;    
    x= malloc(n*sizeof(float));

    for(i=0;i<=n-2;i++){
        j=i;
        for(k=i+1;k<=n-1;k++){
            if(!(abs(A[j][i])>=abs(A[k][i]))) j = k;
        }
        if(!(j==1)){
            for(l=0;l<=n;l++){
                aux=A[i][l];
                A[i][l] = A[j][l];
                A[j][l] = aux;
            }        
        }
        for(j=i;j<=n-1;j++){
            m = A[j][i]/A[i][i];
            for(l=0;l<=n;i++) A[j][l] = A[j][l] - m*A[i][l];
        }
    }

    x[n-1] = b[n-1]/A[n-1][n-1];
    
    for(i=0;i<=n-2;i++){
        j = n-i-1;
        s = 0;
        for(l=0;l<=i;l++){
            k = j+l+1;
            s += A[j][k] * x[k];
        }
        x[j] = (A[j][n]-s)/A[j][j];
    }
    
    printf("el vector solucion es: x[");
    for(j=0;j<n;j++){
        printf("%.1f,",x[j]);
    }
    printf("]\n");

    libera_vector(x);
}
*/

float suma_LU(float **L, float **U,int i,int j,int x){
    int k;
    double suma = 0.0;
    for(k=0;k<=x-1;k++){
        suma += L[j][k]*U[k][i];
    }
    return suma;
}

void factorizacion_LU_Doolitle(float **A,int n){
    int i,j,k;
    float **L,**U;
    
    L = malloc(n*sizeof(float*));
    U = malloc(n*sizeof(float*));

    for(i=0;i<n;i++) L[i]=malloc(n*sizeof(float));
    for(i=0;i<n;i++) U[i]=malloc(n*sizeof(float));
    /*
     for(i=0;i<n;i++){
        for(j=0;j<n;j++){
            if(i==j)L[i][j]=1.0;
        }    
    }*/
    
    for(k=0;k<n;k++){
        for(j=0;j<n;j++){
            if(j<=k){ 
                U[j][k] = A[j][k];
                for(i=0;i<j-1;i++){            
                    U[j][k] = U[j][k] - L[j][i]*U[i][k];
                }
            }
            if(k<=j){
                L[j][k] = A[j][k];
                for(i=0;i<k-1;i++){
                    L[j][k] = L[j][k] - L[j][i]*U[i][k];
                }
                L[j][k] = L[j][k]/U[k][k];
            }            
        }
    }  
    

    printf("matriz L:\n");
    imprimir_matriz(L,n);
    printf("matriz U:\n");
    imprimir_matriz(U,n);
    
    libera_matriz(L,n);
    libera_matriz(U,n);
}

float suma(float **L,float **U, int i, int j,int x){
    int k;
    float suma=0.0;
    for(k=0;k<=x-1;k++){
        suma = suma + L[i][k]*U[k][j];
    }
    return suma;
}

void factorizacion_LU_Crout(float **A,int n){
    int i,j;
    float **L,**U;
    
    L = malloc(n*sizeof(float*));
    U = malloc(n*sizeof(float*));

    for(i=0;i<n;i++) L[i]=malloc(n*sizeof(float));
    for(i=0;i<n;i++) U[i]=malloc(n*sizeof(float));

    for(i=0;i<n;i++){
        for(j=0;j<n;j++){
            if(i==j)U[i][j]=1.0;
        }    
    }
    
    for(j=0;j<n;j++){
        for(i=j;i<n;i++){
            L[i][j] = A[i][j] - suma(L,U,i,j,j);
        }
        for(i=j+1;i<n;i++){
            U[j][i] = (A[j][i] - suma(L,U,j,i,j))/L[j][j];
        }
    }
    printf("matriz L:\n");
    imprimir_matriz(L,n);
    printf("matriz U:\n");
    imprimir_matriz(U,n);
    
    libera_matriz(L,n);
    libera_matriz(U,n);
}

void factorizacion_LU_Crout_recurrencia(float **A,int n){
    int i,j,k;
    float **L,**U;
    
    L = malloc(n*sizeof(float*));
    U = malloc(n*sizeof(float*));

    for(i=0;i<n;i++) L[i]=malloc(n*sizeof(float));
    for(i=0;i<n;i++) U[i]=malloc(n*sizeof(float));

    for(i=0;i<n;i++){
        for(j=0;j<n;j++){
            if(i==j)U[i][j]=1.0;
        }    
    }
    
    for(k=0;k<n;k++){
        for(j=k;j<n;j++){
            U[k][j] = A[k][j] - suma(L,U,k,j,k);
        }
        for(i=k+1;i<n;i++){
            L[i][k] = (A[i][k] - suma(L,U,i,k,k))/U[k][k];
        }
    }
    printf("matriz L:\n");
    imprimir_matriz(L,n);
    printf("matriz U:\n");
    imprimir_matriz(U,n);
    
    libera_matriz(L,n);
    libera_matriz(U,n);
}

int maximo(float **A,int n,int i){
    int p,j;
    float max = 0.0;
    for(j=0;j<n;j++){
         if(max<abs(A[j][i])){
            max=abs(A[j][i]);
            p=j;
         }
    }    
    return p;     
}

float **intercambiar(float **A,int p,int k,int n){
    int i;    
    float *X;
    X=malloc(n*sizeof(float));
    
    for(i=0;i<n;i++){
         X[i]=A[p][i];
         A[p][i]=A[k][i];
         A[k][i]=X[i];
    }      
    
    return A;
}

void factorizacion_LU_1(float **A,int n){
    int k,i,p;
    float **L,**U;
    
    L = malloc(n*sizeof(float*));
    U = malloc(n*sizeof(float*));

    for(i=0;i<n;i++) L[i]=malloc(n*sizeof(float));
    for(i=0;i<n;i++) U[i]=malloc(n*sizeof(float));

    for(k=0;k<n;k++){
        for(i=k;i<n;i++){
            L[i][k] = A[i][k] - suma(L,U,i,k,k);
        }

        //determinar indice p pertenece {k,k+1,...,n}
        p=maximo(A,n,k);
        //intercambiar filas p y k
        A=intercambiar(A,p,k,n);

        for(i=k+1;i<n;i++){
            U[k][i] = (A[k][i] - suma(L,U,k,i,k))/L[k][k];
        }
    }
        
    printf("matriz L:\n");
    imprimir_matriz(L,n);
    printf("matriz U:\n");
    imprimir_matriz(U,n);
    
    libera_matriz(L,n);
    libera_matriz(U,n);
}

void factorizacion_PivPar(float **A,float *b,int n){
    int k,i,j,p,m;
    float *x;
    
    x= malloc(n*sizeof(float));

    for(k=0;k<n-1;k++){
        //determinar indice p pertenece {k,k+1,...,n}
        p=maximo(A,n,k);
        //intercambiar filas p y k
        A=intercambiar(A,p,k,n);
        if(A[k][k]==0)printf("La matriz es singular.\n");
        
        else{
            for(i=k+1;i<n;i++){
                m=A[i][k]/A[k][k];
                for(j=k+1;j<n;j++){
                    A[i][j]=A[i][j] - m*A[k][j];
                }
                b[i]=b[i] - m*b[k];  
            }
        }
    }
            
    /*sustitucion regresiva*/
    x[n-1]=b[n-1]/A[n-1][n-1];

    for(i=n-2;i>=0;i--){
        x[i]=b[i];
        for(j=i+1;j<n;j++){
            x[i]=x[i] - A[i][j]*x[j];
        }
        x[i]=x[i]/A[i][i];
    }

    printf("el vector solucion es: x[");
    for(j=0;j<n;j++){
        printf("%.3f,",x[j]);
    }
    printf("]\n");

    libera_vector(x);
}

float suma_D(float **L,float *D,int k){
    int i;    
    float suma=0.0;
    for(i=0;i<=k-1;i++){
        suma = suma + L[k][i]*L[k][i]*D[i];
    }
    return suma;
}

float suma_D_1(float **L,float *D,int i,int k){
    int p;    
    float suma=0.0;
    for(p=0;p<=k-1;p++){
        suma = suma + L[i][p]*L[k][p]*D[p];
    }
    return suma;
}

void imprimir_vector(float *D,int n){
    int i;
    printf("[");    
    for(i=0;i<n;i++){
        printf("%.3f,",D[i]);
    }
    printf("]\n");
}
 
void factorizacion_LDLT(float **A,int n){
    int k,i;
    float **L;
    float *D;
    
    D = malloc(n*sizeof(float));
    L = malloc(n*sizeof(float*));
    for(i=0;i<n;i++) L[i]=malloc(n*sizeof(float));

    for(k=0;k<n;k++){
        L[i][i]=1.0;
        D[k]=A[k][k] - suma_D(L,D,k);
        if(D[k]==0.0)printf("no cumple.\n");break;
        for(i=k+1;i<n;i++){
            L[k][i] = 0.0;
            L[i][k] = (A[i][k] - suma_D_1(L,D,i,k))/D[k];
        }        
    }
    
    printf("matriz L:\n");
    imprimir_matriz(L,n);
    printf("diagonal D:\n");
    imprimir_vector(D,n);

    libera_matriz(L,n);
    libera_vector(D);
}

float suma_1(float **G,int j){
    int p;
    float suma=0.0;
   for(p=0;p<=j-1;p++) suma = suma + G[j][p]*G[j][p];

    return suma;
}

float suma_2(float **G,int i,int j){
   int p;
   float suma=0.0;
   for(p=0;p<=j-1;p++) suma = suma + G[i][p]*G[j][p];
   return suma;
}

void cholesky(float **A,int n){
    int i,j;
    float **G;
    
    G = malloc(n*sizeof(float*));
    for(i=0;i<n;i++) G[i] = malloc(n*sizeof(float));    
    
    //G[0][0]=sqrt(A[0][0]);
    
    //for(i=1;i<n;i++){G[i][0]= A[i][0]/G[0][0];}
    
    for(j=0;j<n;j++){
        G[j][j]=sqrt(A[j][j] - suma_1(G,j));
        for(i=j+1;i<n;i++){
            G[i][j] = (A[i][j] - suma_2(G,i,j))/G[j][j];
        }
    }
    
    //G[n-1][n-1] = sqrt(A[n-1][n-1] - suma_1(G,n));

    printf("matriz G:\n");
    imprimir_matriz(G,n);

    libera_matriz(G,n);
}
