#include <stdio.h>
#include <string.h>

int recursiveCount (char str[]){
	return (str[0] == '\0'? 0: (int)(str[0] == '!') + recursiveCount(str + 1));
}

int main(void) {

	setvbuf(stdout, NULL, _IONBF, 0);

	//Test your function before submission
	
	char str1[]="abc ! abc !";
	printf("%i\n",recursiveCount(str1));
	char str2[]="!! 10 ! !  ";
	printf("%i\n",recursiveCount(str2));
	char str3[]="!!!!!!!!";
	printf("%i\n",recursiveCount(str3));
	char str4[]="";
	printf("%i\n",recursiveCount(str4));
	


	return 0;
}

