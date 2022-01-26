document.addEventListener('DOMContentLoaded', function() {

function myFunction() {
  alert("Hello\nHow are you?");
}
document.getElementById("likes").addEventListener("mouseover", mouseOver);
document.getElementById("likes").addEventListener("mouseout", mouseOut);

function mouseOver() {
  document.getElementById("likes").style.color = "red";
}

function mouseOut() {
  document.getElementById("likes").style.color = "black";

}


});