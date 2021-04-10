#include <stdio.h>
#include <math.h>

int main(){
	setvbuf(stdout, NULL, _IONBF, 0);

	char in[69], out[69];
	FILE *infile;
	FILE *outfile;
	scanf("%s %s", in, out);
	infile = fopen(in, "r");
	outfile = fopen(out, "w");

	if (infile == NULL || outfile == NULL){
		printf("Problem.\n");
		return 1;
	}

	do{
		putc(getc(infile), outfile);
	} while(!feof(infile));

	return 0;
}

