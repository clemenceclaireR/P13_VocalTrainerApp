window.onload = initall;
var  saveAnswerButton ;


function initall() {

    saveAnswerButton=document.getElementById('finish');
    if (saveAnswerButton == null) {
        saveAnswerButton=document.getElementById('next');
        saveAnswerButton.onclick = save_answers;
    } else {
        saveAnswerButton=document.getElementById('finish');
        saveAnswerButton.onclick = save_answers;
    }

}
function save_answers() {
    console.log('in save_answer');
    var answer = $("input:radio[name=answer]:checked").val()
    console.log(answer);
    var url = '/save_answer?answer=' + answer
    ajaxPostRequest(url);

}

function ajaxPostRequest(url) {
    // GET request treatment and check its response
    // If okay, send data
    var req = new XMLHttpRequest();
    req.open("GET", url, true);
    req.addEventListener('load', function() {
        if ((req.status >= 200 && req.status < 400)) {
            callback(req.responseText);
        } else {
            console.error(req.status + " " + req.statusText + " " + url);
        }
    });
    req.addEventListener('error', function() {
        console.error("Network failure with URL " + url);
    });
    req.send();
}