def prac():
    elavation = 0
    above_sealevel = True
    counter_below_sealevel = 0
    example = [1, -2, 2, -2, 2, -2, 0]
    for e in example:
        elavation += e
        if elavation < 0 and above_sealevel == True:
            counter_below_sealevel += 1
            above_sealevel = False
        elif elavation >= 0 and above_sealevel == False:
            above_sealevel = True

    return counter_below_sealevel

    print("Number of times below sealevel: {}".format(counter_below_sealevel))


def test_prac():
    print(prac() == 3)


def main():
    # prac()
    test_prac()


if __name__ == "__main__":
    main()