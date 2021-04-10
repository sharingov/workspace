#include <stdio.h>
#include <math.h>

int main(){
	setvbuf(stdout, NULL, _IONBF, 0);

	printf("n\t2^n\n-------------\n");

	for (int i = 1; i <= 16; i++){
		printf("%i\t%.0f\n", i, pow(2, i));
	}
}

