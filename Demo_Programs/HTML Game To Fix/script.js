var items = document.getElementsByClassName('valueItem');

var skip = Math.floor(Math.random() * items.length);  

for (var i = 0; i < items.length; i++){
	if (i === skip){continue;}
	items[i] . textContent = i;
}

function inputAnswer(information){
	if (information === skip){
		document.getElementById("overlay").style.display = "block";
	}
}

function off() {
  document.getElementById("overlay").style.display = "none";
}