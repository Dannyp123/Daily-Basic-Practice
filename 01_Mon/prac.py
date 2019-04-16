def prac_loops():
    num = int(input("Pick a number: "))
    for number in range(num):
        if number != 0:
            if number % 2 == 0:
                print(f" {number} : Even")

            else:
                print(f" {number} : Odd")
        else:
            print("Sorry... no ")


def prac_diff_loops():
    num = int(input("Pick a number: "))
    i = 1
    while (i < num):
        if i != 0:
            if i % 2 == 0:
                print(f" {i} : Even")

            else:
                print(f" {i} : Odd")
        i += 1


def main():
    prac_loops()
    prac_diff_loops()


if __name__ == "__main__":
    main()