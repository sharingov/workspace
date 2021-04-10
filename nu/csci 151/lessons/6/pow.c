#include <stdio.h>
#include <math.h>

int main(){
	setvbuf(stdout, NULL, _IONBF, 0);
	int n;
	double x, sum = 1;

	scanf("%lf\n%d", &x, &n);

	for(int i = 0; i < n; i++) {
		sum *= x;
	}

	printf("%lf", sum);
}

