#include <stdio.h>

int main(void) {
    int limit = 12000,
        count = 0,
        top = 0,
        stack[4000],
        left = 3,
        right = 2,
        med;

    for (;;) {
        med = left + right;
        if (med > limit) {
            if (top > 0) {
                left = right;
                --top;
                right = stack[top];
            }
            else {
                break;
            }
        }
        else {
            ++count;
            stack[top] = right;
            ++top;
            right = med;
        }
    }

    printf("%d\n", count);

    return 0;
}
