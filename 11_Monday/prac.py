def split_bill(bill, allergy_index, money_recieved):
    allergy_index = bill[allergy_index]
    total = 0
    shared_total = 0
    payment = 0
    jt_pays = 0

    total += sum(bill)

    bill.remove(allergy_index)

    shared_total += sum(bill)

    jt_pays += shared_total / 2

    payment += money_recieved - jt_pays

    print("Jt's Change: {}".format(payment))


def logic():
    split_bill([9.50, 11.75, 18.50, 3.00, 3.00], 0, 30)


if __name__ == "__main__":
    logic()