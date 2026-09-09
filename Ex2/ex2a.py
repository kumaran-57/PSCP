def main():
    n = int(input("Enter a positive integer: "))

    if n == 1:
        print("1 is neither prime nor composite.")
        return

    flag = False
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            flag = True
            break

    if flag:
        print(f"{n} is not a prime number.")
    else:
        print(f"{n} is a prime number.")

if __name__ == "__main__":
    main()
