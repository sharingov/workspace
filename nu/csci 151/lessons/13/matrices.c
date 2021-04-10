#include <stdio.h>
#include <math.h>
#include <time.h>
#include <stdlib.h>

int main(){
	setvbuf(stdout, NULL, _IONBF, 0);

	int a[3][3], b[3][3], c[3][3];
	srand(time(0));

	for (int i = 0; i < 3; i++){
		for (int j = 0; j < 3; j++){
			a[i][j] = rand()%100;
			b[i][j] = rand()%100;
		}
	}

	for (int i = 0; i < 3; i++){
		for (int j = 0; j < 3; j++){
			int sum = 0;
			for(int k = 0; k < 3; k++){
				sum += a[i][k] * b[k][j];
			}
			c[i][j] = sum;
		}
	}

	for (int i = 0; i < 3; i++){
		for (int j = 0; j < 3; j++){
			printf("%2d ", a[i][j]);
		}
		printf("\n"); 
	}
	printf("\n");
	for (int i = 0; i < 3; i++){
		for (int j = 0; j < 3; j++){
			printf("%2d ", b[i][j]);
		}
		printf("\n"); 
	}
	printf("\n");
	for (int i = 0; i < 3; i++){
		for (int j = 0; j < 3; j++){
			printf("%5d ", c[i][j]);
		}
		printf("\n"); 
	}
	return 0;
}

