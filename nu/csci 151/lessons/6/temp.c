#include <stdio.h>
#include <math.h>

int main(){
	setvbuf(stdout, NULL, _IONBF, 0);

	for (int i = -50; i <=40; i++){
		printf("%i - %i\n", i, i*9/5+32);
	}

}

