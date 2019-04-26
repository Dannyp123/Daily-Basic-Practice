def ransom_note():
    magazine = "Hello World"
    note = "He old"
    new_magazine = list(magazine)
    new_note = list(note)

    for letter in new_note:
        if letter in new_magazine and letter != " ":
            new_magazine.remove(letter)
        elif letter == " ":
            continue
        else:
            return False
    return True


def logic():
    print(ransom_note())


if __name__ == "__main__":
    logic()