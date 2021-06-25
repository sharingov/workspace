#include <stdio.h>

int split (int A[], int n){
	int sum = 0;
	for(int i = 0; i < n; i++){
		sum += A[i];
	}
	if(sum%2==0){
		for(int i = 0, nSum = 0; nSum < sum/2; i++){
			nSum += A[i];
			if(nSum == sum/2)
				return 1;
		}
	}
	return 0;
}

int main(void) {
	setvbuf(stdout, NULL, _IONBF, 0);
	int a[] = {1, 1, 1, 5};
	printf("%d", split(a, 4));
	return 0;
}
