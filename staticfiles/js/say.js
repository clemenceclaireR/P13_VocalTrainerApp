var synth = window.speechSynthesis;
var voices = [];


function say(m) {
var msg = new SpeechSynthesisUtterance(m);

voices = synth.getVoices();
// for chrome
if (speechSynthesis.onvoiceschanged !== undefined) {
  speechSynthesis.onvoiceschanged = voices;
}
for(i = 0; i < voices.length ; i++) {
    if(voices[i].lang === 'en-US') {
      msg.voice = voices[i];
    }
  }
  msg.pitch = 0.8;
  msg.volume = 1;
  msg.rate = 0.6;
  msg.lang = 'en-US'
  msg.text = m;
  synth.speak(msg);
}
