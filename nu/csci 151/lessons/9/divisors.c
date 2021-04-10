#include <stdio.h>
#include <math.h>

int main(){
	setvbuf(stdout, NULL, _IONBF, 0);

	int n;
	scanf("%d", &n);

	for(int i = 2; i <= n/2; i++) {
		if (n%i==0) printf("%d ", i);
	}
	return 0;
}

