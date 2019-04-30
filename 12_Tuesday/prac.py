def repetiton(letters, truncate_at):
    num_of_a = letters.count("a")
    string_length = max(1, len(letters[:truncate_at]))
    stop = num_of_a * truncate_at // string_length
    print(stop)


def logic():
    repetiton("ab", 1)
    repetiton("a", 50)
    repetiton("A", 100)
    repetiton(" ", 1)


if __name__ == "__main__":
    logic()