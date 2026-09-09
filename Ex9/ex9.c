#include <stdio.h>
#include <string.h>

// Define a union to store employee information
union EmployeeInfo {
    int employeeID;
    float salary;
    char department[50];
};

int main() {
    union EmployeeInfo employee;

    // Input employee information
    printf("Enter Employee ID: ");
    scanf("%d", &employee.employeeID);

    printf("Enter Salary: ");
    scanf("%f", &employee.salary);

    printf("Enter Department: ");
    scanf("%s", employee.department);

    // Output employee information
    printf("\nEmployee Information:\n");
    printf("Employee ID: %d\n", employee.employeeID);
    printf("Salary: %.2f\n", employee.salary);
    printf("Department: %s\n", employee.department);

    return 0;
}
