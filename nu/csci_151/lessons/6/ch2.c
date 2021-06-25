#include <stdio.h>
#include <math.h>

int main(){
	setvbuf(stdout, NULL, _IONBF, 0);

	int n, fa = 1;
	double x, sum = 1, po = 1;

	scanf("%lf\n%d", &x, &n);

	for (int i = 1; i <= n; i++){
		po *= x;
		fa *= i;
		sum += po/fa;
	}

	printf("%lf", sum);
}

