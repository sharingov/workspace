#include <stdlib.h>
#include <stdio.h>
#include <math.h>

int main(){
	setvbuf(stdout, NULL, _IONBF, 0);
	double *xptr = (double*)malloc(sizeof(double));
	if(xptr == NULL){
		return 1;
	}
	*xptr = 123.4;
	printf("%lf", *xptr);
	free(xptr);
	return 0;
}

