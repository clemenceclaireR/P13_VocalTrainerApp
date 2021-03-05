function say(m) {
  // loads Web Speech API in order to
  // play sound text

  var synth = window.speechSynthesis;

  // sound text item is given to
  // Web Speech API
  var msg = new SpeechSynthesisUtterance(m);

  // load system voices
  var voices = synth.getVoices();
  console.log(typeof voices.length);
  console.log(voices.length);

  // custom config for Chrome according
  // to Web Speech API documentation
  if (speechSynthesis.onvoiceschanged !== undefined) {
    speechSynthesis.onvoiceschanged = voices;
  }

  // keep only US english voices
  for (i = 0; i < voices.length ; i++) {
    if(voices[i].lang === 'en-US') {
      msg.voice = voices[i];
    }
  }

  // voice options settings
  msg.pitch = 0.8;
  msg.volume = 1;
  msg.rate = 0.6;
  msg.lang = 'en-US'
  msg.text = m;

  // play sound
  synth.speak(msg);

  // if no voices is available in the system, then
  // display alert message in the window
  if (voices.length == 0) {
    console.log("no voices available")
    document.getElementById('warning_voices').style.display = "block";
  } else {
    document.getElementById('warning_voices').style.display = "none";
    }
}
