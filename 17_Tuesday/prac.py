def triple_up(numbers):
    for num in range(0, len(numbers) - 2):
        add_one = numbers[num + 1]
        previous = numbers[num]
        add_two = numbers[num + 2]
        if add_one > previous and add_two > add_one:
            return True

    return False


def work():
    print(triple_up([1, -10, -5, -3]))


if __name__ == "__main__":
    work()