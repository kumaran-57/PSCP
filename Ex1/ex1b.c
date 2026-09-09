#include <stdio.h>

int main()
 {
    int a = 10, b = 5;

    // Assignment Operators
    int sum = 0;
    sum += a; 
    printf("sum after += a: %d\n", sum);

    int product = 1;
    product *= b; 
    printf("product after *= b: %d\n", product);

    // Conditional Operator
    int max = (a > b) ? a : b;
    printf("Maximum of %d and %d is: %d\n", a, b, max);

    // Nested Conditional Operator
    int x = 15, y = 12;
    int result = (x > y) ? (x - y) : ((y > x) ? (y - x) : 0);
    printf("Absolute difference between %d and %d is: %d\n", x, y, result);

    return 0;
}
