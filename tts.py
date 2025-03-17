from gtts import gTTS

def generate_tts(text, lang='hi'):
    tts = gTTS(text=text, lang=lang)
    tts.save("output.mp3")
    return "output.mp3"
