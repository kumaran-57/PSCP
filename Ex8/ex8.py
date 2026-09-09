from dataclasses import dataclass


@dataclass
class Book:
    title: str
    author: str
    year: int


def main():
    num_books = int(input("Enter the number of books: "))
    library = []

    for i in range(num_books):
        print(f"\nEnter details for Book {i + 1}:")
        title = input("Title: ")
        author = input("Author: ")
        year = int(input("Year of Publication: "))
        library.append(Book(title, author, year))

    print("\nLibrary Contents:")
    for i, book in enumerate(library, 1):
        print(f"\nBook {i}")
        print(f"Title: {book.title}")
        print(f"Author: {book.author}")
        print(f"Year: {book.year}")

if __name__ == "__main__":
    main()
