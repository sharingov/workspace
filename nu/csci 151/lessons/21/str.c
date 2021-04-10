#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(){
	setvbuf(stdout, NULL, _IONBF, 0);

	FILE *file = fopen("input.txt", "r");
	char s[128];
	int sum = 0;
	while(fscanf(file, "%s", s) != EOF){
		sum += atoi(s);
	}
	printf("%d", sum);
	return 0;
}

