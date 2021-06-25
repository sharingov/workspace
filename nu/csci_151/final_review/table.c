#include <stdio.h>
#include <math.h>

int main(){
	setvbuf(stdout, NULL, _IONBF, 0);

	for(int i = 1; i <= 5; i++){
		for(int j = 1; j <= 5; j++){
			printf("%i\t", (int)pow(i, j));
		}
		printf("\n");
	}

	return 0;
}

