function say(m) {
   var msg = new SpeechSynthesisUtterance();
   var voices = window.speechSynthesis.getVoices();
   msg.voice = voices[2];
   msg.voiceURI = "native";
   msg.volume = 1;
   msg.rate = 0.6;
   msg.pitch = 0.8;
   msg.text = m;
   msg.lang = 'en-US';
   speechSynthesis.speak(msg);
}