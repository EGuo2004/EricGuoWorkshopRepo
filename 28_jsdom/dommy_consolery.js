/*
   your PPTASK:
   
   Test drive each bit of code in this file,
    and insert comments galore, indicating anything
     you discover,
    	have questions about,
    		or otherwise deem notable.
    		
    		Write with your future self or teammates in mind.
    		
    		If you find yourself falling out of flow mode, consult 
    		other teams
    		MDN

   A few comments have been pre-filled for you...
   
   (delete this block comment once you are done)
*/

// Team Phantom Tollbooth :: Clyde Sinclair, Fierce Dragon 
// SoftDev pd0
// K28 -- Getting more comfortable with the dev console and the DOM
// 2022-02-08t
// --------------------------------------------------


//send diagnostic output to console
//(Ctrl-Shift-K in Firefox to reveal console)
//Ayo works immediately
console.log("AYO");

var i = "hello";
var j = 20;


//assign an anonymous fxn to a var
var f = function(x) {
  var j=30;
  return j+x;
};


//instantiate an object
var o = { 'name' : 'Thluffy',
          age : 15,
          items : [10, 20, 30, 40],
          morestuff : {a : 1, b : 'ayo'},
          func : function(x) {
            return x+30;
          }
        };


var addItem = function(text) {
  var list = document.getElementById("thelist");
  var newitem = document.createElement("li");
  newitem.innerHTML = text;
  list.appendChild(newitem);
};


var removeItem = function(n) {
  var listitems = document.getElementsByTagName('li');
  listitems[n].remove();
};


var red = function() {
  var items = document.getElementsByTagName("li");
  for(var i = 0; i < items.length; i++) {
    items[i].classList.add('red');
  }
};

red();

var stripe = function() {
  var items = document.getElementsByTagName("li");
  for(var i = 0; i < items.length; i++) {
    if (i%2==0){
      items[i].classList.add('red');
    } else {
      items[i].classList.add('blue');
    }
  }
};


let fib = (n) => {
  if(n == 0) {
      return 0;
  } else if(n <= 2) {
      return 1;
  } else {
      return fib(n - 1) + fib(n - 2);
  }
}

let factorial = (n) => {
  if (n == 0) {
      return 1;
  } else {
      return factorial(n - 1) * n;
  }
}

let gcd = (a, b) => {
  let gcdNum;
  if (a > b) {
      for (i = 2; i <= b; i++){
          if (a % i == 0 && b % i == 0) {
              gcdNum = i
          }
      }
      return gcdNum
  } else if (a == b) {
      return a;
  } else {
      for (i = 2; i <= a; i++){
          if (a % i == 0 && b % i == 0) {
              gcdNum = i
          }
      }
      return gcdNum;
  }
}

let buton = () => {
  var b = document.getElementByID("b");
  b.addEventListener('click',addItem("ButonTest"));
}

var y = factorial(5);
console.log(y);
var z = fib(6);
console.log(z);
var w = gcd(10, 25);
console.log(w);