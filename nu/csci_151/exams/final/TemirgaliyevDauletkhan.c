#include <stdio.h>
#include <string.h>

int countGroups(char str[]){
	int i = 0;
	char temp, group;
	int ans = 0;
	while(str[i] != '\0'){
		if(i == 0){
			temp = str[i];
			group = temp;
			i++;
			continue;
		}
		if(str[i] != ' ' && str[i] == temp && temp != group){
			ans++;
			group = temp;
		}
		temp = str[i];
		i++;
	}
	return ans;
}

int main(void) {
	setvbuf(stdout, NULL, _IONBF, 0);

	char str1[]="   111111  bb 222222 ccc 11" ;
	printf("%i\n",countGroups(str1));
	char str2[]="     aaabcc   ";
	printf("%i\n",countGroups(str2));
	char str3[]="abcabcabc";
	printf("%i\n",countGroups(str3));
	char str4[]="a a a a a   a";
	printf("%i\n",countGroups(str4));
	


	return 0;
}

