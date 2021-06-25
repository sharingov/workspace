#include <stdio.h>
#include <string.h>

int main(){
	setvbuf(stdout, NULL, _IONBF, 0);

	char val[69]; //storing an integer as an array of chars
	scanf("%s", val);
	int n = strlen(val);
	int current = 47; //ascii code for character before '0' 
	_Bool isIncreasing = 1; 
	_Bool isPalindrom = 1; //the sequence is increasing and is a palindrom untill proven otherwise

	for(int i = 0; i < (n+1)/2; i++){
		if(val[i] != val[n-1-i]){ //compare for palindrom
			isPalindrom = 0;
			break;
		}
		if (val[i] <= current) isIncreasing = 0; //compare for increase
		
		current = val[i]; //changing status quo
	}

	if(isPalindrom && (n+1)/2==1) isIncreasing = 0; //in case of 1 or 2 digits

	printf("This number is%sa palindrom", isPalindrom? " " : " not ");
	if(isPalindrom) printf(" of which the sequence of the first ceil(n/2) digits is%sincreasing", isIncreasing? " " : " not ");

	return 0;
}

