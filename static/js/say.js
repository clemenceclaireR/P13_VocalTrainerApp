// load voices from Web Speech API
const loadVoices = async () => {
    const response = await window.speechSynthesis.getVoices()

    return response
}

// wait for voices to be loaded before checking
// if voices are available or not
const fetchVoices = async () => {
    const result = await loadVoices()
    console.log(result.length);
    // if no voices is available in the system, then
    // display alert message in the window
    if (result.length == 0) {
      console.log("No voices available")
      document.getElementById('warning_voices').style.display = "block";
    } else {
      document.getElementById('warning_voices').style.display = "none";
    }
    return result
}


function say(m) {
  // loads Web Speech API in order to
  // play sound text

  var synth = window.speechSynthesis;

  // sound text item is given to
  // Web Speech API
  var msg = new SpeechSynthesisUtterance(m);

  // load system voices
  var voices = (async () => {
    await fetchVoices()
  })()

  speechSynthesis.onvoiceschanged = voices;


  // custom config for Chrome according
  // to Web Speech API documentation :
  // wait for the event to fire before populating the list
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



}
