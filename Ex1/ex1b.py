def main():
    a, b = 10, 5

    total = 0
    total += a
    print(f"sum after += a: {total}")

    product = 1
    product *= b
    print(f"product after *= b: {product}")

    maximum = a if a > b else b
    print(f"Maximum of {a} and {b} is: {maximum}")

    x, y = 15, 12
    result = x - y if x > y else (y - x if y > x else 0)
    print(f"Absolute difference between {x} and {y} is: {result}")

if __name__ == "__main__":
    main()
