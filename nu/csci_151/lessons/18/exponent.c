#include <math.h>
#include <stdio.h>

double power(double x, int n) {
  if (n == 0)
    return 1;
  if (n == 1)
    return x;
  if (n < 0)
    return 1 / power(x, -n);
  return power(x, n / 2) * power(x, (n + 1) / 2);
}

int main() {
  setvbuf(stdout, NULL, _IONBF, 0);

  double x;
  int n;
  scanf("%lf %d", &x, &n);
  printf("%lf", power(x, n));

  return 0;
}
