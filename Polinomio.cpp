#include <iostream>
#define N 100
using namespace std;

double x[N] , _x;

double solve( int n ){
	if ( n == -1) return 0;
	return solve (n-1) * _x + x[n];
}
int main(){
	int degree;
	cout << "Ingresar el grado del polinomio : " << endl;
	cin >> degree;
	cout << "Ingresar los coeficientes : " << endl;
	for(int i = 0; i <= degree ; i++) cin >> x[i];
	cout << "Ingresar el punto a evaluar : ";
	cin >> _x;
	cout << solve(degree) << endl;
	return 0;	
}

