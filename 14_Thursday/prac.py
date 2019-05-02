def fizzin_buzzin():
    num_range = range(1, 51)
    for num in num_range:
        if num % 3 == 0 and num % 5 == 0:
            num = "FizzBuzz"
        elif num % 3 == 0:
            num = "Fizz"
        elif num % 5 == 0:
            num = "Buzz"
        else:
            num = num
        print(num)


def logic():
    fizzin_buzzin()


if __name__ == "__main__":
    logic()