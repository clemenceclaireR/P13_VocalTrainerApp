// grant jquery access in script
var script = document.createElement('script');
script.src = 'https://code.jquery.com/jquery-3.4.1.min.js';
script.type = 'text/javascript';
document.getElementsByTagName('head')[0].appendChild(script);

window.onload = function() {

  // variable initiation
  var saveAnswerButton ;
  var cookie = document.cookie
  var csrfToken = cookie.substring(cookie.indexOf('=') + 1)
  var audioElement = document.createElement("audio");

  // hide next/finish button until user click on an answer
  $('#next').hide();
  $('#finish').hide();


  // listen on event in order to show next/finish button if
  // user click on an answer
  document.getElementById("answer_1").addEventListener("change", show_button, false);
  document.getElementById("answer_2").addEventListener("change", show_button, false);
  // replay sound if user click on the replay button
  document.getElementById("replay_sound").addEventListener("change", say_sound, false);


  init_all();


function init_all() {
    // play sound when window is displayed, shuffle answers
    // and save answer when next/finish button is clicked
    say(sound);
    placeAnswersRandomly()
    saveAnswerButton=document.getElementById('finish');
    if (saveAnswerButton == null) {
        saveAnswerButton=document.getElementById('next');
        saveAnswerButton.onclick = save_answers;
    } else {
        saveAnswerButton=document.getElementById('finish');
        saveAnswerButton.onclick = save_answers;
    }

}


function say_sound() {
  // triggers sound playing
  say(sound);
}


function show_button() {
  // display hidden next/finish button
  $('#next').show();
  $('#finish').show();
}


function save_answers() {
  // get user answer and send it to django through ajax request
  // if success, goes to next page
  var answer = $("input:radio[name=answer]:checked").val();

    $.ajax({
      type: "POST",
      url: "/save_answer",
      data: {
        'answer':answer, 'page':page, 'csrfmiddlewaretoken': $("input[name=csrfmiddlewaretoken]").val()
      },
      headers: {
           'X-CSRFToken': csrfToken
         },
      dataType: 'json',
      success: function (data) {
        console.log("SUCCESS")
        window.location.href = next_page;
      },
    }
    );

}

function placeAnswersRandomly() {
  // place right answer randomly to left or right
  var right_answer_place = Math.floor(Math.random() * 2);
  if (right_answer_place === 0) {
    var d = document.getElementById('first_answer');
    d.parentNode.appendChild(d);
  }
}

}




