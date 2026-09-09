def sum_of_digits(n):
    n = abs(n)
    if n == 0:
        return 0
    return n % 10 + sum_of_digits(n // 10)


def main():
    num = int(input("Enter a positive integer: "))
    print(f"Sum of digits of {num} is {sum_of_digits(num)}")

if __name__ == "__main__":
    main()
