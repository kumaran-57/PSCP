def main():
    a, b = map(int, input("Enter two integers: ").split())
    print(f"Before swapping: a = {a}, b = {b}")

    # XOR swap, matching the bitwise operation used in the original exercise.
    a = a ^ b
    b = a ^ b
    a = a ^ b

    print(f"After swapping: a = {a}, b = {b}")

if __name__ == "__main__":
    main()
