#include <stdio.h>

int count(int n, int left, int right) {
	int med = left + right;
	if (med > n)
		return 0;
	return 1 + count(n, left, med) + count(n, med, right);
}

int main(void) {
	printf("%d\n", count(12000, 3, 2));
	return 0;
}
