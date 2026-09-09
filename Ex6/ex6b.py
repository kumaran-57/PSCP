def main():
    str1 = input("Enter the first string: ")
    str2 = input("Enter the second string: ")

    result = []
    ptr1 = 0
    ptr2 = 0

    while ptr1 < len(str1):
        result.append(str1[ptr1])
        ptr1 += 1

    while ptr2 < len(str2):
        result.append(str2[ptr2])
        ptr2 += 1

    print("Concatenated string:", "".join(result))

if __name__ == "__main__":
    main()
