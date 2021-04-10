#include <stdio.h>
#include <stdlib.h>
#include <time.h>

typedef struct {
	_Bool mine;
	_Bool seen;
	int  around;
} cell;

void printGrid(int x, int y, cell grid[x][y]){
	for  (int i = 0; i < x; i++){
		for (int j = 0; j < y; j++){
			if(!grid[i][j].seen){
				printf("%c", '?');
			} else if(grid[i][j].mine){
				printf("%c", 'B');
			} else{
				printf("%c", grid[i][j].around==0? '.' : grid[i][j].around+48);
			}
		}
		printf("\n");
	}
}

int main(){
	setvbuf(stdout, NULL, _IONBF, 0);
	int x, y, n;
	scanf("%d %d %d", &x, &y, &n);
	cell grid[x][y];
	srand(time(0));
	for(int i = 0; i < x; i++){
		for(int j = 0; j < y; j++){
			grid[i][j] = (cell) {.mine = 0, .seen = 0, .around = 0};
		}
	}
	for(int i = 0; i < n; i++){
		int row, column;
		do{
			row = rand()%x;
			column = rand()%y;
		} while (grid[row][column].mine);
		grid[row][column].mine = 1;
		for(int a = row - (row != 0); a <= row + (row != x-1); a++){
			for(int b = column - (column != 0); b <= column + (column != y-1); b++){
				grid[a][b].around++;
			}
		}
	}

	for (int count = 0; count < x*y-n; count++){
		printGrid(x, y, grid);
		int i, j;
		scanf("%d %d", &i, &j);
		grid[i][j].seen = 1;
		if(grid[i][j].mine){
			printGrid(x, y, grid);
			printf("You fucking lost");
			break;
		}
	}
	printGrid(x, y, grid);

	return 0;
}

