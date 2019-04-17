function getString() {
    stringOne = "hello"
    stringTwo = "pillow"

    return stringOne && stringTwo
}


function logic(stringOne, stringTwo) {
    stringOneList = []
    stringTwoList = []

    i = 0
    similarity = ""
    for (s in stringOne) {
        stringOneList.push(s)
    }
    for (s in stringTwo) {
        stringTwoList.push(s)
    }

    while (i < stringOneList.length && i < stringTwoList.length) {
        if (stringOneList[i] != stringTwoList[i]) {
            similarity += "."
        } else {
            similarity += stringOneList[i]
        }
        i += 1
        return similarity
    }
}

function work() {
    stringOne = getString()
    stringTwo = getString()
    console.log(logic(stringOne, stringTwo))
}

work()