def main():
    count = 0
    print("\nNumbers from 1 to 100 not divisible by 2,3 & 5\n")
    for x in range(1, 101):
        if x % 2 != 0 and x % 3 != 0 and x % 5 != 0:
            print(x, end="\t")
            count += 1
    print(f"\nTotal Numbers:{count}")

if __name__ == "__main__":
    main()
