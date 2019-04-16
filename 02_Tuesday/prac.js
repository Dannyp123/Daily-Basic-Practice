function pracLoopsTwo() {
  var baseNum = 12;
  var factNum = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11];

  factNum.forEach(function(element) {
    if (element != 0) {
      if (baseNum % element == 0) {
        console.log(`${element} is a factor of ${baseNum}`);
      } else {
        console.log(`${element} is not a factor of ${baseNum}`);
      }
    }
  });
}

function pracDiffLoopsTwo() {
  num = 12;
  baseNum = 1;

  while (baseNum < num) {
    if (baseNum != 0) {
      if (num % baseNum == 0) {
        console.log(`${baseNum} is a factor of ${num}`);
      } else {
        console.log(`${baseNum} is not a factor of ${num}`);
      }
    }
    baseNum += 1;
  }
}

pracLoopsTwo();
pracDiffLoopsTwo();
