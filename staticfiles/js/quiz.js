window.onload = function() {
var saveAnswerButton ;
 initall();


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
    //document.querySelector('input:radio[name=answer]:checked').value;
    var answer = $("input:radio[name=answer]:checked").val();
    console.log('answer ' + answer);
    //var url = '/save_answer?answer=' + encodeURIComponent(answer);
    var url = '/save_answer';
    console.log(url);
    ajaxPostRequest(url, answer);
}



function ajaxPostRequest(url, answer) {
    // POST request treatment and check its response
    // If okay, send data
    var req = new XMLHttpRequest();

    req.data = {'answer':answer};
    req.open('POST', url);
    req.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    req.addEventListener('load', function() {
    console.log('status' + req.status);
        if ((req.status >= 200 && req.status < 400)) {
            console.log(req.status);
        } else {
            console.error(req.status + " " + req.statusText + " " + url);
        }
    });
    req.addEventListener('error', function() {
        console.error("Network failure with URL " + url);
    });

    req.send("answer="+answer);
    console.log(req)
    console.log('answer sent : ' + answer);
    console.log('data sent');
}






}

