def read_matrix(rows, cols, name):
    print(f"Elements of {name} matrix:")
    return [[int(input()) for _ in range(cols)] for _ in range(rows)]


def main():
    r1 = int(input("Number of rows in first matrix : "))
    c1 = int(input("Number of columns in first matrix : "))
    first = read_matrix(r1, c1, "first")

    r2 = int(input("Number of rows in second matrix : "))
    c2 = int(input("Number of columns in second matrix : "))

    if c1 != r2:
        print("Matrices with entered orders cannot be multiplied.")
        return

    second = read_matrix(r2, c2, "second")
    result = [[sum(first[i][k] * second[k][j] for k in range(c1))
               for j in range(c2)] for i in range(r1)]

    print("After Multiplication, the result is :")
    for row in result:
        print(*row, sep="\t")

if __name__ == "__main__":
    main()
