#include <stdio.h>
#include <math.h>

int main(){
	setvbuf(stdout, NULL, _IONBF, 0);	

	int n;
	do{
		scanf("%d", &n);
		printf("%d\n", n*n);
	} while (n > 0);
	
	return 0;
}

