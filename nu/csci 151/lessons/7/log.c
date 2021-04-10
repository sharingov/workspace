#include <stdio.h>
#include <math.h>

int main(){
	setvbuf(stdout, NULL, _IONBF, 0);

	int n, k = 0, val = 1;
	scanf("%d", &n);

	while(n >= val){
		k++;
		val *= 2;
	}

	printf("%d", k-1);

	return 0;
}

