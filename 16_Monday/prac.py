def take_a_walk(walking_direction):
    walking_direction = walking_direction
    x = 0
    y = 0
    for d in walking_direction:
        if d == "n":
            x += 1
        elif d == "s":
            x -= 1
        elif d == "w":
            y -= 1
        elif d == "e":
            y += 1

    if  len(walking_direction) == 10 and x == y:
        return True
    else:
        return False


def logic():
    print(take_a_walk([
        "n",
    ]))


if __name__ == "__main__":
    logic()