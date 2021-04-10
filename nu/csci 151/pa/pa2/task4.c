#include <stdio.h>
#include <math.h>

void printTriples(int n, int arr[n]){
	_Bool has = 0;
	for(int i = 0; i < n - 2; i++){
		double ratio = (double)arr[i+1]/arr[i];
		if(ratio == (double)arr[i+2]/arr[i+1]){
			has = 1;
			printf("(%d %d %d), r = %lf\n", arr[i], arr[i+1], arr[i+2], ratio);
		}
	}
	if(!has)
		printf("None\n");
}

int main(){
	setvbuf(stdout, NULL, _IONBF, 0);
	int n;
	scanf("%d", &n);
	int arr[n];
	for(int i = 0; i < n; i++){
		scanf("%d", &arr[i]);
	}
	printTriples(n, arr);
	return 0;
}

