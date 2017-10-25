var inpF, hist;
var inpFdefault = "Enter your text here.";

window.onload = setup;

function getResponse(){
  // Pushing prompt to the history
  var prompt = inpF.value;
  if (prompt === inpFdefault || prompt === "")
    return; // show warning message?
  hist = document.getElementById("history");
  hist.innerHTML += `<div class="history user">${prompt}</div>`;
  inpF.value = "";
  console.log(prompt);

  // Sending stuff to server (for now, no server)
  var nlgResponse = "SWABHA's MY FAVORITE NLPer!";
  hist.innerHTML += `<div class="history nlg">${nlgResponse}</div>`;
  hist.innerHTML += `<hr class="removable">`;
  var toSend = hist.innerText;
  /*var xmlHttp = new XMLHttpRequest();
  xmlHttp.onreadystatechange = function() { 
  	if (xmlHttp.readyState == 4 && xmlHttp.status == 200)
      callback(xmlHttp.responseText);
  }
  xmlHttp.open("GET", "localhost", true);
  xmlHttp.send();*/
}

function checkboxes(cb){
	if (cb.id === "enableDialogue"){
		if (cb.checked)
			$(".nlg").addClass("dialogue")
		else
			$(".nlg").removeClass("dialogue")
	} else if (cb.id === "separateTalkTurns" ){
		if (cb.checked)
			$(".removable").show();
		else
			$(".removable").hide();
	}
}

function setup(){
  /*Input field aesthetics*/
  inpF = document.getElementById("inputfield");
  inpF.onfocus = function(){
    if(inpF.value === inpFdefault){
      inpF.style = "color: black;font-style: normal";
      inpF.value = "";
    }
  };
  inpF.onblur = function(){
    if (inpF.value === ""){
      inpF.style = "color: grey;font-style: italic;";
      inpF.value = inpFdefault;
    }
  };
  inpF.onkeypress = function(e){
    if (e.keyCode === 13 && !e.shiftKey){
      getResponse();
      //inpF.blur();
    }
  };
}