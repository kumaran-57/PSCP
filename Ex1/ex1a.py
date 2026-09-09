def main():
    num1, num2 = map(int, input("Enter two integers: ").split())

    total = num1 + num2
    difference = num1 - num2
    product = num1 * num2
    quotient = num1 / num2

    print("Arithmetic Operations:")
    print(f"Sum: {total}")
    print(f"Difference: {difference}")
    print(f"Product: {product}")
    print(f"Quotient: {quotient:.2f}")

    a, b, c = map(int, input("\nEnter three integers: ").split())
    maximum = max(a, b, c)
    minimum = min(a, b, c)
    is_even = num1 % 2 == 0 and num2 % 2 == 0
    is_positive = a > 0 and b > 0 and c > 0

    print("\nRelational and Logical Operations:")
    print(f"Maximum among {a}, {b}, {c}: {maximum}")
    print(f"Minimum among {a}, {b}, {c}: {minimum}")
    print(f"Both numbers are{' ' if is_even else ' not '}even.")
    print(f"All numbers are{' ' if is_positive else ' not '}positive.")

if __name__ == "__main__":
    main()
