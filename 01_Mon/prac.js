function pracLoops() {
    var baseNum = [1, 2, 3, 4, 5, 6, 7, 8];
    baseNum.forEach(function (element) {
        if (element != 0) {
            if (element % 2 == 0) {
                console.log(element + ": Even")
            } else {
                console.log(element + ": Odd")
            }
        }
    })
}

function pracDiffLoop() {
    num = 24
    baseNum = 1;

    while (baseNum < num) {
        if (baseNum != 0) {
            if (baseNum % 2 == 0) {
                console.log(`${baseNum} : Even`)
            } else {
                console.log(`${baseNum} : Odd`)
            }
        }
        baseNum += 1;
    }



}

pracLoops()
pracDiffLoop()