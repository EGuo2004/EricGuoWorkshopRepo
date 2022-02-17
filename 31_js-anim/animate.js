/* Rayat Roy, Eric Guo
		SoftDev pd2
		K32 -- Canvas based JS animation
		2022-02-16w
		The javascript portion
*/
let c = document.getElementById("slate");
let dotButton = document.getElementById("start");
let stopButton = document.getElementById("stop");
let dvdButton = document.getElementById("DVD");
//prepare to interact with canvas in 2D
let ctx = c.getContext("2d");

//set fill color to team color

let requestID;  //init global let for use with animation frames

//let clear = function(e) {
let clear = (e) => {
  console.log("clear invoked...")
  ctx.clearRect(0,0,c.offsetWidth,c.offsetHeight);
};


let radius = 5;
let growing = true;


//let drawDot = function() {
let drawDot = () => {
  ctx.clearRect(0,0,c.width,c.height); //get rid of the old circle
  //console.log("drawDot invoked..."); helpful log info
  //console.log(requestID);
  window.cancelAnimationFrame(requestID); //It's a bit odd, but the cancelling needs to happen before the redrawing, it'll work
  console.log(growing)
  //this just changes the size of the circle correctly
  if(radius >= 300 && growing === true){
    growing = false;
  }
  if(radius <= 0 && growing === false){
    growing = true;
  }
  if(growing === true){
    radius = radius + 1;
  }
  else{
    radius = radius - 1;
  }
  //console.log("radius: "+ radius)
  requestID = window.requestAnimationFrame(drawDot); //this gets the request ID for the cancelling frame from above. I don't entirely get it tho.
  //draws the circle
  ctx.beginPath();
  ctx.arc(300,300,radius,0,2 * Math.PI);
  ctx.fill();
  ctx.stroke();

};
//let stopIt = function() {
let dvdx = Math.floor(Math.random());
let dvdy = Math.floor(Math.random());
let dx = 1;
let dy = 1;
let dvd = () => {
  clear();
  window.cancelAnimationFrame(requestID);
  dvdx += Math.floor(Math.random());
  dvdy += Math.floor(Math.random());
  if(dvdx == 0 || dvdx == c.width) {
    dx = dx * -1;
  }
  if (dvdy == 0 || dvdy == c.height) {
    dy = dy * -1;
  }
  console.log(dvdx);
  console.log(dvdy);
  requestID = window.requestAnimationFrame(dvd);
  ctx.beginPath();
  ctx.arc(dvdx,dvdy,2,0,2 * Math.PI);
  ctx.fill();
  ctx.stroke();
}
let stopIt = () => {
  console.log("stopIt invoked...")
  console.log( requestID );
  window.cancelAnimationFrame(requestID);
};


dotButton.addEventListener( "click", drawDot );
stopButton.addEventListener( "click",  stopIt );
dvdButton.addEventListener( "click", dvd);
