#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
#include <time.h>

typedef struct {
	_Bool hasRobot; // 1 (true) a robot is here; 0 (false) the space is clear
	int robHeading; // 0 (west), 1 (north), 2 (east), 3 (south)
	_Bool robAlive; // 1 (true) for running robot; (false) when crashed
} gridSquare;

int main() {
	srand(time(0));
	setvbuf(stdout, NULL, _IONBF, 0);
	gridSquare grid[10][10];
	for (int i = 0; i < 10; i++) {
		for (int j = 0; j < 10; j++) {
			grid[i][j] = (gridSquare){.hasRobot=0, .robAlive = 1};
		} 
	}
	int row, column, liveCount = 10;
	for (int i = 0; i < 10; i++) {
		do {
			row = rand() % 10;
			column = rand() % 10;
		} while (grid[row][column].hasRobot);
		grid[row][column] = (gridSquare){.hasRobot = 1, .robHeading = rand()%4, .robAlive = 1};
	}

	do {
		for (int i = 0; i < 10; i++) {
			for (int j = 0; j < 10; j++) {
				printf("%c", grid[i][j].hasRobot? grid[i][j].robAlive? 'R' : '@' : '.');
			}
			printf(" %d\n", i);
		}
		printf("0123456789\n");

		char cmd;
		printf("Input action and coordinates, please: ");
		scanf(" %c %i %i", &cmd, &row, &column);

		if (grid[row][column].hasRobot && grid[row][column].robAlive) {
			if (cmd == 'L') {
				grid[row][column].robHeading -= grid[row][column].robHeading==0? -3 : 1;
			} else if (cmd == 'R') {
				grid[row][column].robHeading = (grid[row][column].robHeading+1)%4;
			} else if (cmd == 'F') {
				switch (grid[row][column].robHeading) {
					case 0: // Pointing west
				 		if (column > 0) { 
				 			if(grid[row][column-1].hasRobot) {
				 				grid[row][column].robAlive = 0;
								liveCount--;
								if (grid[row][column-1].robAlive) {
				 					grid[row][column-1].robAlive = 0;
							 		liveCount--;
							 	}
							} else {
							 	grid[row][column-1].hasRobot = 1;
								grid[row][column-1].robHeading = 0;
								grid[row][column].hasRobot = 0;
							} 
						}
						break;
					case 1: // Pointing north
						if (row > 0) {
							if(grid[row-1][column].hasRobot) {
								grid[row][column].robAlive = 0;
								liveCount--;
								if (grid[row-1][column].robAlive) {
									grid[row-1][column].robAlive = 0;
									liveCount--;
								}
							} else {
								grid[row-1][column].hasRobot = 1;
								grid[row-1][column].robHeading = 1;
								grid[row][column].hasRobot = 0;
							}
						}
						break;
					case 2: // Pointing east
						if (column < 9) {
							if(grid[row][column+1].hasRobot) {
								grid[row][column].robAlive = 0;
								liveCount--;
								if (grid[row][column+1].robAlive) {
									grid[row][column+1].robAlive = 0;
								 	liveCount--;
								} 
							} else {
								grid[row][column+1].hasRobot = 1;
								grid[row][column+1].robHeading = 2;
								grid[row][column].hasRobot = 0;
							}
						}
						break;
					case 3: // Pointing south
						if (row < 9) {
							if(grid[row+1][column].hasRobot) {
								grid[row][column].robAlive = 0;
								liveCount--;
								if (grid[row+1][column].robAlive) {
									grid[row+1][column].robAlive = 0;
									liveCount--;
								}
							} else {
								grid[row+1][column].hasRobot = 1;
								grid[row+1][column].robHeading = 3;
								grid[row][column].hasRobot = 0;
							}
						}
						break;
					default: // Shouldn't happen
						break;
				}
			}
		}
	} while (liveCount > 0);
	return 0;
}
