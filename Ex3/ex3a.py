def read_matrix(rows, cols, name):
    print(f"Elements of {name} matrix:")
    return [[int(input()) for _ in range(cols)] for _ in range(rows)]


def main():
    rows = int(input("Number of rows of matrices to be added : "))
    cols = int(input("Number of columns matrices to be added : "))
    first = read_matrix(rows, cols, "first")
    second = read_matrix(rows, cols, "second")

    print("Sum of entered matrices :")
    for i in range(rows):
        result_row = [first[i][j] + second[i][j] for j in range(cols)]
        print(*result_row, sep="\t")

if __name__ == "__main__":
    main()
