#include <stdio.h>
#include <stdlib.h>
#include <math.h>

char* stringCopy(char *fromStr){
	char *sptr = (char*)malloc(sizeof(char));
	*sptr = *fromStr;
	return sptr;
}

int main(){
	setvbuf(stdout, NULL, _IONBF, 0);
	char *sptr = stringCopy("dsdf");
	printf("%s", sptr);
	free(sptr);
	return 0;
}

