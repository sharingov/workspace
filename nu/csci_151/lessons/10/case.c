#include <stdio.h>
#include <math.h>

int main(){
	setvbuf(stdout, NULL, _IONBF, 0);

	char s[69];
	scanf("%s", s);

	for (int i = 0; s[i] != '\0'; i++) {
		putchar(s[i]>='a'&&s[i]<='z'? s[i]-32: s[i]);
	}
	
	return 0;
}

