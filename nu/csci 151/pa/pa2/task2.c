#include <stdio.h>
#include <string.h>
#include <stdlib.h>

typedef struct{
	int id;
	char firstName[100];
	char lastName[100];
	int birthYear;
	int score;
} wrestler;

int getNumberOfWrestlers(char inputFile[]){
	char temp[100];
	FILE *file = fopen(inputFile, "r");
	fscanf(file, "%s", temp);
	fclose(file);
	return(atoi(temp));
}

void init(wrestler list[], char inputFile[]){
	FILE *file = fopen(inputFile, "r");
	char temp[100]; 
	fscanf(file, "%s", temp);
	int val = fscanf(file, "%s", temp);
	for(int i = 0; val != EOF; i++){
		list[i].id = atoi(temp);
		fscanf(file, "%s", temp);
		strcpy(list[i].firstName, temp);
		fscanf(file, "%s", temp);
		strcpy(list[i].lastName, temp);
		fscanf(file, "%s", temp);
		list[i].birthYear = atoi(temp);
		fscanf(file, "%s", temp);
		list[i].score = atoi(temp);
		val = fscanf(file, "%s", temp);
	}
	fclose(file);
}

void printScoreboard(wrestler list[], int n){
	printf("Printing the score board\n");
	for(int i = 0; i < n; i++){
		printf("%d\t%s\t\t%s\t\t\t%d\t\t%d\n", list[i].id, list[i].firstName, list[i].lastName, list[i].birthYear, list[i].score);
	}
}

void writeTheChampion(wrestler list[], int n){
	int winner = 0;
	for(int i = 1; i < n; i++){
		if(list[i].score > list[winner].score)
			winner = i;
	}
	printf("The champion is\n");
	printf("%d\t%s\t\t%s\t\t\t%d\t\t%d\n", list[winner].id, list[winner].firstName, list[winner].lastName, list[winner].birthYear, list[winner].score);
}

void processGames(char inputFile[], wrestler list[], int n){
	FILE *file = fopen(inputFile, "r");
	int wrestler1;
	int val = fscanf(file, "%d", &wrestler1);
	while(val != EOF){
		int wrestler2, winner, score;
		fscanf(file, "%d %d %d", &wrestler2, &winner, &score);
		for(int j = 0; j < n; j++){
			if(list[j].id == wrestler1)
				wrestler1 = j;
		}
		for(int j = 0; j < n; j++){
			if(list[j].id == wrestler2)
				wrestler2 = j;
		}
		if(winner != 1)
			list[wrestler2].score += score;
		if(winner != 2)
			list[wrestler1].score += score;
		val = fscanf(file, "%d", &wrestler1);
	}
	fclose(file);
}

int main(){
	char inputFile[100];
	strcpy(inputFile, "in.txt");
	int n = getNumberOfWrestlers(inputFile);
	wrestler list[n];
	init(list, inputFile);
	printScoreboard(list, n);
	writeTheChampion(list, n);
	strcpy(inputFile, "games.txt");
	processGames(inputFile, list, n);
	printScoreboard(list, n);
	writeTheChampion(list, n);
	return 0;
}

