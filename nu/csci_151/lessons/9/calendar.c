#include <stdio.h>
#include <math.h>

int main(){
	setvbuf(stdout, NULL, _IONBF, 0);

	int n;
	scanf("%d", &n);
	if (n < 1 || n > 366) return 0;

	switch(n%7){
		case 0:
			printf("Thursday, ");
			break;
		case 1:
			printf("Friday, ");
			break;
		case 2:
			printf("Saturday, ");
			break;
		case 3:
			printf("Sunday, ");
			break;
		case 4:
			printf("Monday, ");
			break;
		case 5:
			printf("Tuesday, ");
			break;
		case 6:
			printf("Wednesday, ");
			break;
	}

	switch(n){
		case 1 ... 31:
			n-=0;
			printf("January %d", n);
			break;
		case 32 ... 60:
			n-=31;
			printf("February %d", n);
		   break;	
		case 61 ... 91:
			n-=60;
			printf("March %d", n);
			break;
		case 92 ... 121:
			n-=91;
			printf("April %d", n);
			break;
		case 122 ... 152:
			n-=121;
			printf("May %d", n);
			break;
		case 153 ... 182:
			n-=152;
			printf("June %d", n);
			break;
		case 183 ... 213:
			n-=182;
			printf("July %d", n);
			break;
		case 214 ... 244:
			n-=213;
			printf("August %d", n);
			break;
		case 245 ... 274:
			n-=244;
			printf("September %d", n);
			break;
		case 275 ... 305:
			n-=274;
			printf("October %d", n);
			break;
		case 306 ... 335:
			n-=305;
			printf("November %d", n);
			break;
		case 336 ... 366:
			n-=335;
			printf("December %d", n);
			break;
	}

	return 0;
}

