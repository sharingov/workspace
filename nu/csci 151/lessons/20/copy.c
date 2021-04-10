#include <stdio.h>
#include <math.h>

void stringCopy(char from[], char to[]){
	int i;
	for(i = 0; from[i] != '\0'; i++){
		to[i] = from[i];
	}
	to[i] = '\0';
}

void reverse(char from[], char to[]){
	int i, j;
	for(i = 0; from[i] != '\0'; i++){}
	for(j = 0, i = i - 1; i >= 0; j++, i--){
		to[j] = from[i];
	}
	to[j] = '\0';
}

_Bool areEqual(char str1[], char str2[]){
	for(int i = 0; str1[i]==str2[i]; i++){
		if (str1[i] == '\0') return 1;
	}
	return 0;
}

int main(){
	setvbuf(stdout, NULL, _IONBF, 0);
	char str1[32], str2[32];
	scanf("%s", str1);
	scanf("%s", str2);
	reverse(str1, str2);
	return 0;
}
