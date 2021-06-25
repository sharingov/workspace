#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <time.h>

int main(){
	setvbuf(stdout, NULL, _IONBF, 0);
	int ar[20], min = 100, max = 50, sum = 0;
	double av;
	srand(time(0));

	for (int i = 0; i < 20; i++){
		ar[i] = rand() % 51 + 50;
		min = ar[i] < min? ar[i] : min;
		max = ar[i] > max? ar[i] : max;
		sum += ar[i];
		printf("%d\t", ar[i]);
	}

	printf("\nmax = %d\tmin = %d\t average = %.2lf\n", max, min, sum/20.0);

	return 0;
}

