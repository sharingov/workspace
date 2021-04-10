#include <stdio.h>
#include <math.h>

int main(){
	setvbuf(stdout, NULL, _IONBF, 0);
	
	for(int i = 0; i < 6; i++){
		for(int j = 0; j < 5; j++){
			printf("%c", i+j<5? '+' : '*');
		}
		printf("\n");
	}

}

