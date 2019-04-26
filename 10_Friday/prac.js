function ransomNote() {
    magazine = "Hello World"
    note = "He old"

    new_magazine = Array(magazine)
    new_note = Array(note)

    for (letter in new_note) {
        if (letter in new_magazine && letter != " ") {
            delete new_magazine[letter]
        } else if (letter == " ") {
            continue
        } else {
            return false
        }
        return true
    }

}

console.log(ransomNote())