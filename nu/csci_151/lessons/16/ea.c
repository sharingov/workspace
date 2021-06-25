#include <stdio.h>
#include <math.h>

double expApprox(double x, int n){
	int fa = 1;
	double sum = 1, po = 1;

	for (int i = 1; i <= n; i++){
		po *= x;
		fa *= i;
		sum += po/fa;
	}
	return sum;
}
double sinApprox(double x, int n){
	int fa = 1;
	double sum = 0;

	for(int i = 1; i <= n; i+=2){
		sum = sum + ((i-1)%4==0? +pow(x, i)/fa : -pow(x, i)/fa);
		fa = fa * (i+1) * (i+2);
	}

	return sum;
}
_Bool isPrime(int n){
	for(int i = 2; i <= sqrt(n); i++){
		if (n%i==0)
			return 0;
	}
	return 1;
}
int sumOfDigits(int n){
	int sum = 0;
	while(n!=0){
		sum += n%10;
		n /= 10;
	}
	return sum;
}
_Bool isIdeal(int n){
	int sum = 1;
	for(int i = 2; i <= sqrt(n); i++){
		if(n%i==0)
			sum = sum + i + (n/i==i? 0 : n/i);
	}
	return sum==n;
}

int main(){
	setvbuf(stdout, NULL, _IONBF, 0);
	return 0;
}

