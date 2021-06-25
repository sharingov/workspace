#include <stdio.h>
#include <math.h>

int main(){
	setvbuf(stdout, NULL, _IONBF, 0);

	int ar[10];
	ar[0] = 1;
	for (int i = 1; i < 10; i++){
		ar[i] = i*ar[i-1];
	}

	return 0;
}

