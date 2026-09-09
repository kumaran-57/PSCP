def main():
    year = int(input("Enter the Year (YYYY) : "))
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        print(f"\nThe Given year {year} is a Leap Year")
    else:
        print(f"\nThe Given year {year} is Not a Leap Year")

if __name__ == "__main__":
    main()
