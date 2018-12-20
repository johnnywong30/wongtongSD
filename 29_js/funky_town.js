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
  // swap a and b if a is less than b
  if (a < b) {
    var temp = a;
    a = b;
    b = temp;
  }

  var remainder = a % b;
  // return b if divisor b goes into dividend a nicely
  if (remainder == 0){
    return b;
  }
  // else return gcd between b and the remainder
  return gcd(b, remainder);
}

// gcdWrapper manages the spitting out of the gcd between the two
// inputs of id 'gcd_num1' and id 'gcd_num2' and spits out the
// gcd into the console and onto the page
var gcdWrapper = () => {
  // get two inputs
  var a = document.getElementById('gcd_num1').value;
  var b = document.getElementById('gcd_num2').value;
  // make sure both inputs are filled in
  if (a == '' || b == ''){
    var error = 'Please fill in both inputs fam';
    console.log(error);
    document.getElementById('gcdspit').innerHTML = error;
  }
  // spit out the gcd of a and b
  else{
    var theGCD = gcd(a, b);
    console.log(theGCD);
    document.getElementById('gcdspit').innerHTML = `gcd(${a}, ${b}) is ` + theGCD;
  }
}

// adds onclick action to the button of id 'gcd'
document.getElementById('gcd').addEventListener('click', gcdWrapper);

var randomStudent = () => {
  // select a random student from studentList
  var studentList = ['Joan', 'Johnny', 'a-aron', 'maf', 'brown', 'bni', 'k'];
  var student = studentList[Math.floor(Math.random() * studentList.length)];
  console.log(student);
  document.getElementById('std').innerHTML = student
}
// adds onclick action to the button of id 'fib'
document.getElementById('rstd').addEventListener('click', randomStudent);
