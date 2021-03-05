function verify_WSA_compatibility() {
  // if browser does not recognize Web Speech API,
  // display alert message in the window.
  if (!window.speechSynthesis) {
    document.getElementById("warning_browser").style.display = "block";
  }
}