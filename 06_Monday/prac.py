def prac():
    lst = []
    num = int(input('How many numbers: '))

    for n in range(num):
        numbers = int(input('Enter number '))
        lst.append(numbers)

    snum = lst[0]
    bnum = lst[0]

    for num in lst:
        if num < snum:
            snum = num
        elif num > bnum:
            bnum = num
    print('The answer is {}'.format(bnum - snum))


def more_prac():
    numbers = [10, 20, 0, 10]
    i = 1
    snum = numbers[0]
    bnum = numbers[0]

    while (i < len(numbers)):
        if numbers[i] < snum:
            snum = numbers[i]
        elif numbers[i] > bnum:
            bnum = numbers[i]
        i += 1
    print('The answer is {}'.format(bnum - snum))


def main():
    prac()
    more_prac()


if __name__ == "__main__":
    main()