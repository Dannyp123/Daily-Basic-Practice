function letterPrac(phrase) {
    for (let i in phrase) {
        let n = phrase.toLowerCase().charCodeAt(i);
        let distance = n - 96;
        let s = '';
        if (distance >= 0 && distance < 26) {
            for (let j = 0; j < distance; j++) {
                s += phrase.charAt(i);
            }
        } else {
            s = '(' + phrase.charAt(i) + ')';
        }
        console.log(s);
    }

}
letterPrac("Danny 123 Base Camp!!");