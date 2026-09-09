#include <stdio.h>

void fibonacci(int n) {
    int a = 0, b = 1, c;
    printf("Fibonacci Sequence: %d %d ", a, b);
    while ((a + b) <= n) {
        c = a + b;
        printf("%d ", c);
        a = b;
        b = c;
    }
}

int main() {
    int num;
    printf("Enter a number: ");
    scanf("%d", &num);
    fibonacci(num);
    return 0;
}
