#include <stdio.h>
#include <stdlib.h>

typedef struct{
	int h, w, imgdata[64][96];
} image;

image convert(image orig, int threshold){
	image result = {.h = orig.h, .w = orig.w};
	for(int i = 0; i < result.h; i++){
		for(int j = 0; j < result.w; j++){
			result.imgdata[i][j] = orig.imgdata[i][j] > threshold? 1 : 0;
		}
	}
	return result;
}

int main(){
	setvbuf(stdout, NULL, _IONBF, 0);
	FILE *file = fopen("img.txt", "r");
	image orig = {.h = 64, .w = 92};
	int temp;
	for(int i = 0; i < orig.h; i++){
		for(int j = 0; j < orig.w; j++){
			fscanf(file, "%d", &temp);
			orig.imgdata[i][j] = temp;
		}
	}
	fclose(file);

	FILE *binary1 = fopen("binary1.txt", "w");
	FILE *binary2 = fopen("binary2.txt", "w");
	FILE *binary3 = fopen("binary3.txt", "w");
	image result1 = convert(orig, 64);
	image result2 = convert(orig, 128);
	image result3 = convert(orig, 192);

	for(int i = 0; i < orig.h; i++){
		for(int j = 0; j < orig.w; j++){
			fprintf(binary1, "%d ", result1.imgdata[i][j]);
			fprintf(binary2, "%d ", result2.imgdata[i][j]);
			fprintf(binary3, "%d ", result3.imgdata[i][j]);
		}
		fprintf(binary1, "\n");
		fprintf(binary2, "\n");
		fprintf(binary3, "\n");
	}

	return 0;
}

