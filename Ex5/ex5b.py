def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


def main():
    num = int(input("Enter a positive integer: "))
    if num < 0:
        print("Factorial is not defined for negative numbers.")
    else:
        print(f"Factorial of {num} is {factorial(num)}")

if __name__ == "__main__":
    main()
