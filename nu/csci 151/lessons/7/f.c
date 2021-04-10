#include <stdio.h>
#include <math.h>

int main(){
	setvbuf(stdout, NULL, _IONBF, 0);

	int a = 0, b = 1, c = 0, d = 0;

	printf("%d\t%d\t", a, b);

	while (c < 20){
		d = a + b;
		a = b;
		b = d;
		printf("%d\t", d);
		c++;
	}

	return 0;
}

