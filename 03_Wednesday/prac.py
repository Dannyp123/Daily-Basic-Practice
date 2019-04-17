def get_string():
    string = input("Insert String: ")
    return string


def logic(string_one, string_two):
    string_one_list = []
    string_two_list = []
    i = 0
    similarity = ""
    for s in string_one:
        string_one_list.append(s)
    for s in string_two:
        string_two_list.append(s)

    while (i < len(string_one_list) and i < len(string_two_list)):
        if (string_one_list[i] != string_two_list[i]):
            similarity += "."
        else:
            similarity += string_one_list[i]
        i += 1

    return similarity


def main():
    string_one = get_string()
    string_two = get_string()
    print(logic(string_one, string_two))


if __name__ == '__main__':
    main()
