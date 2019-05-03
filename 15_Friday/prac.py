def streaking(list_of_numbers):
    list_of_numbers = list_of_numbers
    current_item = None
    current_number = 0
    highest_item = None
    highest_number = 0

    if len(list_of_numbers) > 0:
        current_list_item = list_of_numbers[0]
        highest_streak_item = list_of_numbers[0]
        for i in list_of_numbers:
            if i == current_list_item:
                current_number += 1
                if current_number > highest_number:
                    highest_number = current_number
                    highest_streak_item = current_list_item
            else:
                current_list_item = i
                current_number = 1
    print(f"({highest_streak_item}, {current_number})")


def logic():
    streaking([1, 2])


if __name__ == "__main__":
    logic()