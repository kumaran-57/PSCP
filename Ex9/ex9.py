from dataclasses import dataclass


@dataclass
class EmployeeInfo:
    # Python does not have a direct C-style union. This class demonstrates
    # the same idea: one selected value is stored at a time.
    kind: str
    value: object


def main():
    print("1. Employee ID")
    print("2. Salary")
    print("3. Department")
    choice = input("Choose the type of data to store: ").strip()

    if choice == "1":
        employee = EmployeeInfo("Employee ID", int(input("Enter Employee ID: ")))
    elif choice == "2":
        employee = EmployeeInfo("Salary", float(input("Enter Salary: ")))
    elif choice == "3":
        employee = EmployeeInfo("Department", input("Enter Department: "))
    else:
        print("Invalid choice.")
        return

    print("\nEmployee Information:")
    print(f"{employee.kind}: {employee.value}")

if __name__ == "__main__":
    main()
