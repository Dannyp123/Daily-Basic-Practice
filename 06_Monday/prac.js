function prac() {
    const lst = [10, 20, 0, 10]

    let snum = lst[0]
    let bnum = lst[0]

    for (var num of lst) {
        if (num < snum) {
            snum = num
        } else if (num > bnum) {
            bnum = num
        }

    }
    console.log(`The answer is ${bnum - snum}`)

}

function diffPrac() {
    const lst = [10, 20, 0, 10]

    let snum = lst[0]
    let bnum = lst[0]

    lst.forEach(function (element) {
        if (element < snum) {
            snum = element
        } else if (element > bnum) {
            bnum = element
        }
    })
    console.log(`The answer is ${bnum - snum}`)
}
prac()
diffPrac()