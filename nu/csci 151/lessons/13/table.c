#include <stdio.h>
#include <math.h>

int main(){
	setvbuf(stdout, NULL, _IONBF, 0);

	int ar[12][12];

	for(int i = 0; i < 12; i++){
		for(int j = 0; j < 12; j++){
			ar[i][j] = (i+1)*(j+1);
			printf("%3d ", ar[i][j]);
		}
		printf("\n");
	}

	return 0;
}

