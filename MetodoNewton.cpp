#include <iostream>
#include <cmath>

using namespace std;

const double error = 1e-5;

// funcion f
double f(double x){
	return (x*x-40.0*x+256);
}	

// f derivada
double _f(double x){
	return (2.0*x-40);
}
int main(){
	double x_k,x_k1;

	x_k1 = 10.0;
	do{
		x_k = x_k1;
		x_k1 = x_k - (f(x_k)/_f(x_k));
		cout << x_k1 << endl;
	}while(fabs(x_k1 - x_k) > error);
	cout<<"La respuesta es: "<<x_k1<<endl;	
	return 0;
}
