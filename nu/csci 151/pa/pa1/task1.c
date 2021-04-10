#include <stdio.h>

int main(){
	setvbuf(stdout, NULL, _IONBF, 0);

	FILE *file;
	file = fopen("in.txt", "r");
	int k;
	fscanf(file, "%d", &k);
	int grid[k][k];
	int score1 = 0;
	int score2 = 0;
	for(int i = 0; i < k; i++){
		getc(file);
		for(int j = 0; j < k; j++){
			grid[i][j] = getc(file)=='X'? 1 : 0;
		}
	}
	//turning txt file into a matrix
	
/*	for(int i = 0; i < k; i++){
		for(int j = 0; j < k; j++){
			printf("%d", grid[i][j]);
		}
	 	printf("\n");
	}
*/

	for(int i = 0; i < k; i++){
		for(int j = 0; j < k; j++){
			_Bool a=j<k-2,b=i<k-2,c=j>1; //checking so i won't hit the boundaries of a grid
			_Bool x=grid[i][j]; // value of the cell
			if(a) {
				if(grid[i][j] == grid[i][j+1] && grid[i][j] == grid[i][j+2]){
					x? score1++ : score2++;
					//horizontal check
				}
			}
			if(b) {
				if(grid[i][j] == grid[i+1][j] && grid[i][j] == grid[i+2][j]){
					x? score1++ : score2++;
					//vertical check
				}
				if(c && grid[i][j] == grid[i+1][j-1] && grid[i][j] == grid[i+2][j-2]) {
					x? score1++ : score2++;
					//diagonal down and left check
				}
				if(a && grid[i][j] == grid[i+1][j+1] && grid[i][j] == grid[i+2][j+2]) {
					x? score1++ : score2++;
					//diagonal down and right check
				}
			}
		}
	}

	printf("X scored %d and O scored %d", score1, score2);


	return 0;
}
