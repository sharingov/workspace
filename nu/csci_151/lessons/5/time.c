#include <stdio.h>
#include <math.h>

int main(){
	setvbuf(stdout, NULL, _IONBF, 0);
	
	int n;
	scanf("%d", &n);
	n %= 86400;
	
	int h = n/(60*60);
	int m = n%(60*60)/60;
	int s = n%(60*60)%60;


	printf("%d:%d:%d", h, m, s);
}

