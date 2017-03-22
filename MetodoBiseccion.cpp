#include <iostream>
#include <math.h>
using namespace std;

const double tol = 1e-10;

double f(double x){
	double rpta;
	rpta = pow(x,3);
	return rpta;	
}
int main(){
	double a,b,m;
	a = -20.0, b = 15.0;
	while((b-a)/2.0 > tol){
		m = a + (b-a)/2;

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
