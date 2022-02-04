// Team Doorstuck :: Eric Guo, Andy Lin
// SoftDev pd2
// K27 -- Basic functions in JavaScript
// 2022-02-04
// --------------------------------------------------


// as a duo...
// pair programming style,
// implement a fact and fib fxn

// (define fib (lambda (n)
//               (if (= n 0)
//                   0
//                   (if (<= n 2)
//                       1
//                       (+ (fib(- n 1)) (fib(- n 2)))
//                       )
//                   )
//               )
//   )

// (define factorial(lambda (x)
//                   (if(= x 0)
//                      1
//                      (* (factorial(- x 1)) x)
//                      )
//                   )
//   )


  var fib = (n) => {
      if(n == 0) {
          return 0;
      } else if(n <= 2) {
          return 1;
      } else {
          return fib(n - 1) + fib(n - 2);
      }
  }

  var factorial = (n) => {
      if (n == 0) {
          return 1;
      } else {
          return factorial(n - 1) * n;
      }
  }

  var y = factorial(5);
  console.log(y);
  var z = fib(6);
  console.log(z);
//Do whatever you think is needed. Think: S I M P L E.   Think: S M A R T.
