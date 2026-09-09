def main():
    text = input("Enter a string: ")
    length = 0
    index = 0
    while index < len(text):
        length += 1
        index += 1
    print(f"Length of the string: {length}")

if __name__ == "__main__":
    main()
