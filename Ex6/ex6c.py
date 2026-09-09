def main():
    text = input("Enter a string: ")
    start, end = 0, len(text) - 1
    is_palindrome = True

    while start < end:
        if text[start] != text[end]:
            is_palindrome = False
            break
        start += 1
        end -= 1

    if is_palindrome:
        print("The string is a palindrome.")
    else:
        print("The string is not a palindrome.")

if __name__ == "__main__":
    main()
