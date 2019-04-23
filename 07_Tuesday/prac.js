function prac() {
    numberOf0 = 0
    numberOf1 = 0

    numbers = [0, 0, 1, 1, 1, 1]

    for (n of numbers) {
        if (n == 0) {
            numberOf0 += 1;
        } else if (n == 1) {
            numberOf1 += 1;
        }
    }
    return numberOf1 > numberOf0
}

function morePrac() {
    numberOf0 = 0
    numberOf1 = 0

    numbers = [0, 0, 1, 1, 1, 1]

    numbers.forEach(element => {
        if (element == 0) {
            numberOf0 += 1;
        } else if (element == 1) {
            numberOf1 += 1;
        }
    });
    return numberOf1 > numberOf0
}

console.log(prac())
console.log(morePrac())