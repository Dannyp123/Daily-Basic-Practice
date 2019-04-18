function prac() {
    var num1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    var num2 = [1, 2, 3, 4]


    num1.forEach(function (element) {
        if (element != 0) {
            var num = num2.length;
            total = element * num
            console.log(`${element} * ${num} = ${total}`)
        }
    })
}

function pracWhile() {
    num1 = 24
    num2 = 1;

    while (num2 < num1) {
        var total = num2 * num1
        console.log(`${num2} * ${num1} = ${total}`)

        num2 += 1
    }
}

// prac()
pracWhile()