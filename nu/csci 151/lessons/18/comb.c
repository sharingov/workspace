#include <math.h>
#include <stdio.h>

long choose(int n, int k) {
  if (k == 0)
    return 1;
  return choose(n - 1, k - 1) * n / k;
}

int main() {
  setvbuf(stdout, NULL, _IONBF, 0);

  int n, k;
  scanf("%d %d", &n, &k);
  printf("%d", choose(n, k));

  return 0;
}
