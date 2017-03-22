#include <iostream>
#define N 10
using namespace std;

double  _x , x[N] , f[N];
double L (int n, int k){
	double rpta1 = 1.0, rpta2 = 1.0; 
	for (int i = 0 ; i <= n ; i++ )
		if ( i != k ) rpta1 *= ( _x - x[i] ), rpta2 *= ( x[k] - x[i] );
	return rpta1 / rpta2;
}

double P ( int n ){
	double rpta = 0.0;
	for ( int k = 0 ; k <= n ; k++ )
		rpta +=  ( f[k] * L( n , k ));
	return rpta;
}
int main(){
	int puntos;
	cout << "Ingresar la cantidad de puntos : " << endl;
	cin >> puntos;
	cout << "Ingresar los puntos : " << endl;
	for ( int i = 0 ; i < puntos ; i++ ) cin >> x[i];
	cout << "Ingresar los f(x) : " << endl;
	for ( int i = 0 ; i < puntos ; i++ ) cin >> f[i];
	cout << "Ingresar el punto a evaluar : " << endl;
	cin >> _x;
	
	cout << endl << "La respuesta es : " << P(2) << endl; 
	
	
	return 0;
}
