/* Team Hard Inting :: Rayat Roy, Eric Guo
		SoftDev pd2
		K32 -- Canvas based JS animation
		2022-02-16w
		The javascript portion
*/
var c = document.getElementById("slate");
var dotButton = document.getElementById("start");
var stopButton = document.getElementById("stop");
var dvdButton = document.getElementById("DVD");
//prepare to interact with canvas in 2D
var ctx = c.getContext("2d");

//set fill color to team color
ctx.fillStyle="magenta";
var requestID;  //init global var for use with animation frames

//var clear = function(e) {
var clear = (e) => {
  console.log("clear invoked...")
  ctx.clearRect(0,0,c.offsetWidth,c.offsetHeight);
};


var radius = 5;
var growing = true;


//var drawDot = function() {
var drawDot = () => {
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
  requestID = window.requestAnimationFrame(drawDot); 
  //draws the circle
  ctx.beginPath();
  ctx.fillstyle="red";
  ctx.arc(300,300,radius,0,2 * Math.PI);
  ctx.fill();
  ctx.stroke();

};
//var stopIt = function() {
var dvdx;
var dvdy;
var dx = 2;
var dy = 2;
var dvd = () => {
  clear();
  window.cancelAnimationFrame(requestID);
  dvdx += dx;
  dvdy += dy;
  if(dvdx <= 0 || dvdx >= c.width - 60) {
    dx = dx * -1;
  }
  if (dvdy <= 0 || dvdy >= c.height - 40) {
    dy = dy * -1;
  }
  console.log(dvdx);
  console.log(dvdy);
  requestID = window.requestAnimationFrame(dvd);
  var img = new Image();
  img.src = 'logo_dvd.jpg'
  ctx.fillstyle="red";
  ctx.drawImage(img,dvdx,dvdy,60,40);
}
var dvd_helper = () => {
  dvdx = Math.floor(Math.random()*300);
  dvdy = Math.floor(Math.random()*300);
  dvd();
}
var stopIt = () => {
  console.log("stopIt invoked...")
  console.log( requestID );
  window.cancelAnimationFrame(requestID);
};


dotButton.addEventListener( "click", drawDot );
stopButton.addEventListener( "click",  stopIt );
dvdButton.addEventListener("click", dvd_helper);