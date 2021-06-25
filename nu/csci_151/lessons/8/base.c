#include <stdio.h>
#include <math.h>

int main(){
	setvbuf(stdout, NULL, _IONBF, 0);

	int n, base;
	scanf("%d%d", &base, &n);
	while(n>0){
		printf("%d =", n);
		for(int i = 0; n > 0; i++){
			printf(" + (%d * %d^%d)", n%base, base, i);
			n /= base;
		}
		printf("\n");
		scanf("%d", &n);
	}

	return 0;
}

