#include <iostream>
#include <math.h>
using namespace std;

const double tol = 1e-5;

double f(double x){
	double rpta;
	rpta = pow(x,3);
	return rpta;	
}
int main(){
	double a,b,m;
	a = -10.0, b = 20.0;
	m = a;
	while( fabs(f(m)) > tol){
		m = (a*f(b) - b*f(a))/(f(b)-f(a));

		if(f(m) == 0.0){
			a = m, b = m;
		}
		
		if( f(a) * f(m) > 0 )
			a = m;
		else
			b = m;
	}
	cout<<"La respues es: ";
	cout<<m<<endl;
	return 0;
}	
