#include <stdio.h>
#include <math.h>

int smallest(int len, double arr[]){
	int smallest = 0;
	for (int i = 1; i < len; i++){
		if(arr[i] < arr[smallest])
			smallest = i;
	}
	return smallest;
}

double maxVal(int len, double arr[len][len]){
	double max = arr[0][0];
	for(int i = 0; i < len; i++){
		for(int j = 0; j < len; j++){
			if (arr[i][j] > max)
				max = arr[i][j];
		}
	}
	return max;
}

void reverse(int len, double arr[]){
	for(int i = 0; i < (len-2)/2; i++){
		double temp = arr[i];
		arr[i] = arr[len-1-i];
		arr[len-1-i] = arr[i];
	}
}

void transpose(int x, int y, double	orig[x][y], double result[y][x]){
	for (int i = 0; i < x; i++){
		for (int j = 0; j < y; j++){
			result[j][i] = orig[i][j];
		}
	}
}

int main(){
	setvbuf(stdout, NULL, _IONBF, 0);

	return 0;
}

