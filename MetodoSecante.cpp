#include <iostream>
#include <math.h>

using namespace std;

const double error = 1e-5;

double f(double x){
	return (x*x*x);
}

int main() {
	double x0,x1,x2,Ea;
	x0 = -20, x1 = -15;
	Ea=error+1;
	while( Ea > error ){
		x2 = ( x1 - ( (x0-x1) / ( f(x0) - f(x1) ) * f(x1) ) );
		Ea = ( fabs( x1 - x2 ));
		x0 = x1;
		x1 = x2;
	}
 	
	cout<< "La respues es: ";
 	cout<< x2 << endl;
 return 0;
}

