#include <stdio.h>
#include <math.h>

int factorial(int n){
	setvbuf(stdout, NULL, _IONBF, 0);
	int factorial = 1;
	for(int i = n; i > 1; i--){
		factorial *= i;
	}
	return factorial;
}

int main(){
	double x;
	scanf("%lf", &x);
	printf("%lf", x-pow(x,3)/factorial(3)+pow(x,5)/factorial(5));
}
