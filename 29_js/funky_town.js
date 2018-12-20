/*
Zane Wang, Johnny Wong - JayZPants
SoftDev1 pd08
K29 -- Sequential Progression
2018-12-19
*/

// Fibonacci function
var fibonacci = (n) => {
    // store first 2 fib nums
    var fibSeq = [0, 1];
    if(n < 2) return (fibSeq[n]);

    // swap first or second val of fibSeq with summation of prev two values
    var inc = 2;
    while(inc <= n){
        fibSeq[inc % 2] = fibSeq[(inc + 1) % 2] + fibSeq[inc % 2];
        inc++;
    }
    return fibSeq[(inc - 1) % 2];

}

// fibWrapper manages the spitting out of the term at the fibVal index of the fibonacci
// sequence into the console and onto the page
var fibWrapper = () => {
  // fibVal is the num currently in the input field of id 'fib_num'
  var fibVal = document.getElementById('fib_num').value;

  var fibRet = fibonacci(fibVal);
  console.log(fibRet)
  // using String templates to format fibVal into the example below
  document.getElementById('pFib').innerHTML = `fibonacci(${fibVal}) is ` + fibRet
}

// adds onclick action to the button of id 'fib'
document.getElementById('fib').addEventListener('click', fibWrapper);


// gcd function following Euclid's Algo
var gcd = (a, b) => {
  if (a < b) {
    var temp = a;
    a = b;
    b = temp;
  }

  var r = a % b;
  if (r == 0) return b;
  else return gcd(b, r);
};

var studentList = ['Joan', 'Johnny', 'a-aron', 'maf', 'brown', 'bni', 'k'];

var randomStudent = () => {
  // select a random student from studentList
  var student = studentList[Math.floor(Math.random() * studentList.length)];
  console.log(student);
  document.getElementById('std').innerHTML = student
};
// adds onclick action to the button of id 'fib'
document.getElementById('rstd').addEventListener('click', randomStudent);
