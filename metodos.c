#include <stdio.h>
#include "matrices.h"

void menu(){
    printf("Eliga una opcion:\n");
    printf("1) Metodo de gauss.\n2) Factorizacion LU Crout.\n3) Factorizacion LU Doolitle.\n4)Pivotacion parcial.\n5)Factorizacion Matriz simetrica.\n6)Cholesky.\n7)Salir.\n");
}
//programa principal

int main(){
    int n,opcion;
    float**A;
    float *b;
    
    do{
    menu();    
    scanf("%d",&opcion);
    }while(opcion<0 || opcion>7);

    switch(opcion){
    
        case 1:    
                printf("ingrese orden:");
                scanf("%d",&n);

                A=ingreso_matriz(n);
                b=ingreso_vector(n);
    
                imprimir_matriz_sol(A,b,n);
                printf("solucion:\n");   
                eliminacion_gauss(A,b,n);

                libera_matriz(A,n);
                libera_vector(b);
                break;
        case 2:
                printf("ingrese orden:");
                scanf("%d",&n);

                A=ingreso_matriz(n);
                printf("matriz A:\n");                  
                imprimir_matriz(A,n);
                factorizacion_LU_Crout(A,n);
                
                libera_matriz(A,n);
                break; 
        case 3:
                printf("ingrese orden:");
                scanf("%d",&n);

                A=ingreso_matriz(n);
                printf("matriz A:\n");                  
                imprimir_matriz(A,n);
                factorizacion_LU_Doolitle(A,n);

                libera_matriz(A,n);
                break;
        case 4:
                printf("ingrese orden:");
                scanf("%d",&n);

                A=ingreso_matriz(n);
                b=ingreso_vector(n);
    
                imprimir_matriz_sol(A,b,n);
                printf("solucion:\n");   
                factorizacion_PivPar(A,b,n);

                libera_matriz(A,n);
                libera_vector(b);
                break;
        case 5:
                printf("ingrese orden de matriz simetrica:");
                scanf("%d",&n);

                A=ingreso_matriz(n);
    
                printf("solucion:\n");

                factorizacion_LDLT(A,n);
                libera_matriz(A,n);
                break;
        case 6:
                printf("ingrese orden de matriz simetrica:");
                scanf("%d",&n);

                A=ingreso_matriz(n);
    
                printf("solucion:\n");

                cholesky(A,n);
                libera_matriz(A,n);
                break;        
        case 7:
                break;
        default:
                menu();break;
                
     }
return 0;
}
