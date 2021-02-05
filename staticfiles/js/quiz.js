console.time("program");
var script = document.createElement('script');
script.src = 'https://code.jquery.com/jquery-3.4.1.min.js';
script.type = 'text/javascript';
document.getElementsByTagName('head')[0].appendChild(script);

window.onload = function() {
var saveAnswerButton ;
var cookie = document.cookie
var csrfToken = cookie.substring(cookie.indexOf('=') + 1)
var audioElement = document.createElement("audio");

$('#next').hide();
$('#finish').hide();

initall();

$('#answer_1').change(function(){
     show_button();
});

$('#answer_2').change(function(){
    show_button();
});

$('#replay_sound').click(function(){
   say(sound);
});



function initall() {
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



function hideButtons() {
     $('#next').hide();
     $('#finish').hide();
}

function show_button() {
     $('#next').show();
     $('#finish').show();
}


function save_answers() {
    console.log('in save_answer');
    var answer = $("input:radio[name=answer]:checked").val();

    console.log('answer ' + answer);

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
      },
    }
    );

}

function placeAnswersRandomly() {
        var right_answer_place = Math.floor(Math.random() * 2);
        if (right_answer_place === 0) {
            var d = document.getElementById('first_answer');
            console.log(d);
            d.parentNode.appendChild(d);
        }
    }
}


console.timeEnd("program");

