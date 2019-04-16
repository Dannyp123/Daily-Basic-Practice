def prac_loops_two():
    factorNum = int(input("Pick a number: "))
    for n in range(1, factorNum):
        if factorNum % n == 0:
            print(f"{n} is a factor of {factorNum}")
        else:
            print(f"{n} is not a factor of {factorNum}")


def prac_diff_loops_two():
    factNum = int(input("Pick a number: "))

    n = 1
    while (n < factNum and n != 0):
        if factNum % n == 0:
            print(f"{n} is a factor of {factNum}")
        else:
            print(f"{n} is not a factor of {factNum}")
        n += 1


def main():
    prac_loops_two()
    prac_diff_loops_two()


if __name__ == "__main__":
    main()