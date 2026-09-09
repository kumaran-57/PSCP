#include <stdio.h>

int main() {
    // Arithmetic Operations
    int num1, num2;
    printf("Enter two integers: ");
    scanf("%d %d", &num1, &num2);

    int sum = num1 + num2;
    int difference = num1 - num2;
    int product = num1 * num2;
    double quotient = 0.0;
    if (num2 != 0) {
        quotient = (double)num1 / num2;
    }

    printf("Arithmetic Operations:\n");
    printf("Sum: %d\n", sum);
    printf("Difference: %d\n", difference);
    printf("Product: %d\n", product);
    if (num2 != 0)
        printf("Quotient: %.2f\n", quotient);
    else
        printf("Quotient: undefined (division by zero)\n");

    // Relational and Logical Operations
    int a, b, c;
    printf("\nEnter three integers: ");
    scanf("%d %d %d", &a, &b, &c);

    // Relational operators
    int max = (a > b && a > c) ? a : (b > c) ? b : c;
    int min = (a < b && a < c) ? a : (b < c) ? b : c;

    // Logical operators
    int isEven = (num1 % 2 == 0) && (num2 % 2 == 0);
    int isPositive = (a > 0) && (b > 0) && (c > 0);

    printf("\nRelational and Logical Operations:\n");
    printf("Maximum among %d, %d, %d: %d\n", a, b, c, max);
    printf("Minimum among %d, %d, %d: %d\n", a, b, c, min);

    printf("Both numbers are%s even.\n", isEven ? "" : " not");
    printf("All numbers are%s positive.\n", isPositive ? "" : " not");

    return 0;
}
