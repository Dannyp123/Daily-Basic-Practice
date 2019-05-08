def staircase():
    num_of_stairs = int(input("Give me a number:"))
    n = num_of_stairs - 2
    for stairs in range(1, num_of_stairs):
        spacing = ' ' * n
        making_stairs = '#' * stairs
        print(spacing, making_stairs)
        n -= 1
    print('#' * num_of_stairs)


def work():
    staircase()


if __name__ == "__main__":
    work()