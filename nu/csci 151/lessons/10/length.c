#include <stdio.h>
#include <math.h>
#include <string.h>

int main(){
	setvbuf(stdout, NULL, _IONBF, 0);

	char s[69];
	int n = 0;

	do{
		scanf("%s", s);
		printf("%d ", strlen(s));
		n = strlen(s)>n? strlen(s) : n;
	} while (getchar() != '\n');

	printf("\nThe longest word has %d characters", n);

	return 0;
}

