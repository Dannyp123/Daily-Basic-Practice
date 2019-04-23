def prac():
    number_of_0 = 0
    number_of_1 = 0

    numbers = [0, 0, 1,1,1,1]
    for n in numbers:
        if n == 0:
            number_of_0 += 1
        elif (n == 1):
            number_of_1 += 1
    return number_of_1 > number_of_0


def more_prac():
    number_of_0 = 0
    number_of_1 = 0

    numbers = [0, 0, 1,1,1,1]

    n = 1
    while (n < len(numbers)):
        if n == 0:
            number_of_0 += 0
        elif (n ==1):
            number_of_1 += 1
        n += 1
    return number_of_1 > number_of_0



def main():
    print(prac())
    print(more_prac())


if __name__ == "__main__":
    main()