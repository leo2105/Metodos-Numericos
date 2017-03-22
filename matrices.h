extern float** ingreso_matriz(int n);
extern float* ingreso_vector(int n);
extern void imprimir_matriz(float **A,int n);
extern void imprimir_matriz_sol(float**A,float*b,int n);
extern void libera_matriz(float**A,int n);
extern void libera_vector(float*b);
extern void eliminacion_gauss(float**A,float*b,int n);
extern float suma(float **L,float **U, int i, int j,int x);
extern void factorizacion_LU_Crout(float **A,int n);
extern void factorizacion_LU_Crout_recurrencia(float **A,int n);
extern void factorizacion_LU_1(float **A,int n);
extern void factorizacion_PivPar(float **A,float *b,int n);
