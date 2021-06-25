#include <stdio.h>
#include <math.h>

int main(){
	setvbuf(stdout, NULL, _IONBF, 0);

	char ch;
	int c = 0;
	
	do{
		ch = getchar();
		if(ch == 'a') {
			c++;
		}
	} while (ch != '\n');

	printf("%d", c);

	return 0;
}

