#include <stdio.h>
#include <math.h>

int addSub(int x[], int from, int to){
	if (from==to)
		return x[from];
	return addSub(x, from + 1, to) + x[from];
}

int main(){
	setvbuf(stdout, NULL, _IONBF, 0);

	int n, from, to;
	scanf("%d", &n);
	int x[n];
	for (int i = 0; i < n; i++){
		scanf("%d", &x[i]);
	}
	scanf ("%d %d", &from, &to);
	printf("%d", addSub(x, from, to));

	return 0;
}

