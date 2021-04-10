#include <math.h>
#include <stdio.h>

int main(){
	setvbuf(stdout, NULL, _IONBF, 0);
	double a, b, c;
	printf("Enter coefficents:\n");
	scanf("%lf %lf %lf", &a, &b, &c);
	double d = b*b-4*a*c;
	double x1, x2;

	x1 = (-b+sqrt(d))/(2*a);
	x2 = (-b-sqrt(d))/(2*a);

	printf ("Sqares are: %lf %lf", x1, x2);

}
