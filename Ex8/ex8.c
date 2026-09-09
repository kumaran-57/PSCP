#include <stdio.h>

// Define a structure for representing a book
struct Book {
    char title[100];
    char author[50];
    int year;
};

int main() {
    int numBooks;

    printf("Enter the number of books: ");
    scanf("%d", &numBooks);

    // Declare an array of structures
    struct Book library[numBooks];

    // Input data for each book
    for (int i = 0; i < numBooks; i++) {
        printf("\nEnter details for Book %d:\n", i + 1);

        printf("Title: ");
        scanf(" %99[^\n]", library[i].title);

        printf("Author: ");
        scanf(" %49[^\n]", library[i].author);

        printf("Year of Publication: ");
        scanf("%d", &library[i].year);
    }

    // Output details for each book
    printf("\nLibrary Contents:\n");
    for (int i = 0; i < numBooks; i++) {
        printf("\nBook %d\n", i + 1);
        printf("Title: %s\n", library[i].title);
        printf("Author: %s\n", library[i].author);
        printf("Year: %d\n", library[i].year);
    }

    return 0;
}
