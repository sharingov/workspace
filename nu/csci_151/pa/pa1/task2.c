#include <stdio.h>
#include <string.h>

int main(){
	setvbuf(stdout, NULL, _IONBF, 0);

	char text[669], word1[69], word2[69], ch;
	printf("Enter your sentence:\n");
	scanf("%[^\n]%*c", text);
	printf("Enter word1: ");
	scanf("%s", word1);
	printf("Enter word2: ");
	scanf("%s", word2);

	for (int i = 0; i < strlen(text); i++){
		//going through the sentence
		for (int j = 0; j < strlen(word1); j++){
			//comparing with word1
			char a = (text[i+j] >=65 && text[i+j] <= 90)? text[i+j]+32 : text[i+j];
			char b = (word1[j] >=65 && word1[j] <= 90)? word1[j]+32 : word1[j];
			//case insensitivity
			if(a!=b){
				printf("%c", text[i]);
				break;
				//exit the loop if it's already clear that it ain't what we're looking for
			}
			if(j==strlen(word1)-1){
				printf("%s", word2);
				i += j;
				//if it matches fully, print word2 and skip needed amount of char cells
			}
		}
	}


	return 0;
}

