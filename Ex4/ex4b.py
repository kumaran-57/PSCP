def is_armstrong(num):
    if num < 0:
        return False
    digits = str(num)
    power = len(digits)
    return sum(int(digit) ** power for digit in digits) == num


def main():
    num = int(input("Enter a number: "))
    if is_armstrong(num):
        print(f"{num} is an Armstrong number.")
    else:
        print(f"{num} is not an Armstrong number.")

if __name__ == "__main__":
    main()
