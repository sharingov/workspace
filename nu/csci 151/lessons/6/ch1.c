#include <stdio.h>
#include <math.h>

int main(){
	setvbuf(stdout, NULL, _IONBF, 0);
	
	int n;
	double x, val = 1;

	scanf("%lf\n%d", &x, &n);

	if ((int)x == 1){
		printf("%d", n);
		return 0;
	}

	for (int i = 0; i <	n; i++){
		val *= x;
	}

	double sum = x * (val - 1) / (x - 1);

	printf("%lf", sum);

}

