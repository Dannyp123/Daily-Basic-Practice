def socks():

    # 1 is blue
    # 2 is yellow
    # 3 is green
    # 4 is red
    # 5 is pink
    # 6 is purple

    sock_colors = [1, 1, 2, 2, 3, 2]
    counted_socks = []
    counter = 0

    for sock in sock_colors:
        if sock in counted_socks:
            sock_colors.remove(sock)
            counter += 1
        else:
            counted_socks.append(sock)

    print("Pairs of socks: {}".format(counter))


def logic():
    socks()


if __name__ == "__main__":
    logic()