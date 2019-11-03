var timeleft = 3;
document.getElementById("end").style.display = "none";
var downloadTimer = setInterval(function(){
  document.getElementById("countdown").innerHTML = timeleft + " seconds remaining";
  timeleft -= 1;
  if(timeleft <= 0){
    clearInterval(downloadTimer);
    document.getElementById("countdown").innerHTML = "Game over"
    document.getElementById("button").style.display = "none";
    document.getElementById("end").style.display = "inline";

  }
}, 1000);




