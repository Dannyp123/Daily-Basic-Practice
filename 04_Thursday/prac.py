def prac():
    num1 = int(input("Give me a number: "))
    num2 = int(input("Give me another number: "))

    for num in range(num2 + 1):
        total = num * num2
        if num > 0:
            print(f"{num} * {num2} = {total}")


def prac_while():
    num1 = int(input("Give me a number: "))
    num2 = int(input("Give me another number: "))

    n = 1
    while (n < num2):
        total = n * num2
        print(f"{n} * {num2} = {total}")

        n += 1


def main():
    prac()
    prac_while()


if __name__ == "__main__":
    main()