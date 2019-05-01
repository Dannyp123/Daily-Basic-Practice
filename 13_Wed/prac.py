def square_sum(numbers):

    new_squares = []
    square_one = sum(
        [numbers[0][0], numbers[0][1], numbers[1][0], numbers[1][1]])

    new_squares.append(square_one)
    square_two = sum(
        [numbers[0][1], numbers[0][2], numbers[1][1], numbers[1][2]])

    new_squares.append(square_two)
    square_three = sum(
        [numbers[1][0], numbers[1][1], numbers[2][0], numbers[2][1]])

    new_squares.append(square_three)
    square_four = sum(
        [numbers[1][1], numbers[1][2], numbers[2][1], numbers[2][2]])

    new_squares.append(square_four)
    print(max(new_squares))


def logic():
    square_sum([[1, 2, 3], [4, 5, 6], [7, 8, 9]])


if __name__ == "__main__":
    logic()