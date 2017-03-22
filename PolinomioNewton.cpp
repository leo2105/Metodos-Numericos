#include <iostream>
#define N 5
using namespace std;

double x[N] , f_x[N] , dp[N][N] ;

double productoria( double _x, int n ){
	double rpta = 1.0;
	for ( int j = 0 ; j <= n ; j++ )
		rpta *= ( _x - x[j] );
	return rpta;
}

double P ( int n , double _x ){
	if( n == -1 ) return 0;
	return ( P( n - 1 , _x ) + dp[n][n] * productoria( _x , n-1) ); 
}

void MatrizA(){
	for ( int i = 0 ; i < N ; i++ )
		for ( int j = 0 ; j <= i ; j++ )
			if ( j == 0) dp[i][j] = f_x[i];
			else dp[i][j] = (dp[i][j-1] - dp[i-1][j-1]) / (x[i]-x[i-j]);
}

int main(){	
	double _x;
	cout << "Ingresar los puntos : ";
	for ( int i = 0 ; i < N ; i++ ) cin >> x[i];
	cout << "Ingresar los f(x) : ";
	for ( int i = 0 ; i < N ; i++ ) cin >> f_x[i];
	cout << "Ingresar el punto a evaluar: ";
	cin >> _x;

	MatrizA();
	
	cout << endl << "La respuesta es : " << P( N , _x) << endl;
	return 0;
}	
