def get_string():
    string = input("Give me a string: ")
    return string


def logic(string):
    for ch in string:
        distance = (ord(ch.lower()) - 97) + 1
        if (distance > 0 and distance <= 26):
            print(ch * distance)
        else:
            print(ch)


def main():
    string = get_string()
    logic(string)


if __name__ == '__main__':
    main()
