#include <stdio.h>
#include <math.h>

int main(){
	setvbuf(stdout, NULL, _IONBF, 0);

	int a[3];
	scanf("%d %d %d", &a[0], &a[1], &a[2]);

	//sorting an array
	for(int i = 0; i < 2; i++){
		int min = i;
		for(int j = i+1; j < 3; j++){
			if (a[i] == a[j]) { 
				a[j] = 0; //getting rid of duplicates
			}
			if (a[j] < a[min]) {min = j;}
		}
		int temp = a[i];
		a[i] = a[min];
		a[min] = temp;
		//selection sorting
	}

//	printf("%d %d %d", a[0], a[1], a[2]);

	for(int i = 0; i < 3; i++){
		for(int j = 0; j < a[i]; j++){
			printf("%d ", a[i]);
			if(j==a[i]-1) {printf("\n");}
		}
	}

	return 0;
}

