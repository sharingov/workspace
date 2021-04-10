#include <stdio.h>
#include <math.h>

int main(){
	setvbuf(stdout, NULL, _IONBF, 0);

	char name[69];
	scanf("%s", name);
	FILE *file1, *file2, *file3;
	file1 = fopen("values.txt", "r");
	file2 = fopen("story.txt", "r");
	file3 = fopen(name, "w");

	if (file1 == NULL || file2 == NULL) {
		printf("Problem opening files.");
		return 1;
	}

	while(!feof(file2)){
		char ch = getc(file2);
		if(ch=='$') {
			char str[69];
			fscanf(file1, "%s", str);
			printf("%s", str);
			fprintf(file3, "%s", str);
		}
		else {
			printf("%c", ch);
			fprintf(file3, "%c", ch);
		}
	}

	fclose(file1);
	fclose(file2);
	fclose(file3);

	return 0;
}
