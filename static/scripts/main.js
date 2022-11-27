const cro_alph = "abcćčdđefghijklmnoprsštuvzž"
let word = "";
let words = [];
let current_id = 1;

// TODO not done
function handleSubmitWord() {
  //lenght of word
  if (word.length != 5) {
    console.log("Please enter a word with 5 letters!");
    alert("Please enter a word with 5 letters!");
    return;
  }

  //put the & in between the words
  let bar = "";
  let foo;
  for (let k=1;k<30;k++){
    foo = document.getElementById(String(k));
    bar += foo.innerText.toLowerCase()
    if (k%5==0 && k!==0 && document.getElementById(String(k+1)).innerText !== ""){
      bar += "&"
      console.log("Making &")
    }
    console.log("foo="+foo.innerText)
    console.log("bar="+bar)
  }
  bar += document.getElementById(String(30)).innerText
  console.log("Redirecting to "+"/wordle/"+bar)
  
  window.location.href = "/wordle/"+bar;
}


function handleDeleteLetter() {
  //do nothing if the letter is the first in the five-letter sequence
  if (current_id % 5 === 1) return;


  const Check_last_space = document.getElementById(String(current_id));
  //if end of row and last row is not empty
  if ((current_id) % 5 == 0 && Check_last_space.textContent != "") {

    console.log("Deleting" + (current_id));
    word = word.slice(0, word.length - 1);
    const Space = document.getElementById(String(current_id));
    Space.textContent = "";

    //if there isn't anything on the last row
  } else {
    //delete the letter and decrement the id
    console.log("Deleting" + (current_id - 1));
    word = word.slice(0, word.length - 1);
    const Space = document.getElementById(String(current_id - 1));
    Space.textContent = "";

    current_id--;
  }
}

function handleAddLetter(letter) {
  console.log(letter);
  const Space = document.getElementById(String(current_id));
  console.log(Space);
  Space.textContent = letter;

  //check if last letter
  if (current_id % 5 != 0) {
    word = word.concat(letter);
    current_id++;
  }
  else {
    word = word.slice(0, word.length);
    word = word.concat(letter);
  }
}

function set_current_id() {
  //get the current_id
  for (let i = 1; i <= 30; i++) {
    let foo = document.getElementById(String(i));
    words.push(foo.innerText)
    if (foo.innerText === "") {
      current_id = i;
      break;
    }
  }
}

document.addEventListener('keydown', function (event) {
  const key = event.key.toLowerCase(); // "a", "1", "Shift", etc.
  console.log(key);
  if (cro_alph.includes(key)) {
    handleAddLetter(key);
  } else if (key === "backspace") {
    handleDeleteLetter();
  } else if (key === "enter") {
    handleSubmitWord();
  }
});


document.addEventListener("DOMContentLoaded", () => {

  //set the onload events
  const keys = document.querySelectorAll(".keyboard-row button");
  for (let i = 0; i < keys.length; i++) {
    keys[i].onclick = ({ target }) => {
      const letter = target.getAttribute("data-key");

      if (letter === "enter") {
        handleSubmitWord();
        return;
      }

      if (letter === "del") {
        handleDeleteLetter();
        return;
      }

      handleAddLetter(letter);
    };
  }

  set_current_id()

  //did we win
  for (let i = current_id - 1; i > current_id - 5; i--) {
    if (document.getElementById(String(i)).style.backgroundColor !== "green") return;
  }
  alert("You won, congrats!")
  current_id = 31

});

