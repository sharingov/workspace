#include <stdio.h>
#include <math.h>

typedef struct{
	int h, m;
	_Bool am;
} time;

int main(void){
	setvbuf(stdout, NULL, _IONBF, 0);

	time now = {5, 29, 0};
	int adv;
	printf(now.am? "%d:%d am\n" : "%d:%d pm\n", now.h, now.m);
	scanf("%d", &adv);
	adv %= 1440;
	if(now.m + adv%60 >= 60){
		now.h++;
	}
	now.m = (now.m + adv%60)%60;
	for (int i = 0; i < (now.h + adv/60)/12; i++){
		now.am = !now.am;
	}
	now.h = (now.h + adv/60)%12;
	if(now.h == 0){now.h= 12;}
	printf(now.am? "%d:%d am\n" : "%d:%d pm\n", now.h, now.m);


	return 0;
}

