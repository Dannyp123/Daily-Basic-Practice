def repetiton(letters, truncate_at):
    num_of_a = letters.count("a")
    if len(letters) > 0 and letters.count("a") > 0:
        remainder = truncate_at % len(letters)
        string_length = letters[:remainder].count("a")
        num = len(letters)
        answer = (truncate_at // num) * (num_of_a) + (string_length)
    else:
        answer = 0
    print(answer)


def logic():
    repetiton("ab", 1)
    repetiton("a", 50)
    repetiton("A", 100)
    repetiton(" ", 1)
    repetiton("ab", 5)


if __name__ == "__main__":
    logic()