#include <stdio.h>
#include <math.h>

void printBinary(int n){
	if (n==0)
		return;
	printBinary(n/2);
	printf("%d", n%2);
}

int main(){
	setvbuf(stdout, NULL, _IONBF, 0);

	int n;
	scanf("%d", &n);
	printBinary(n);
	return 0;
}

