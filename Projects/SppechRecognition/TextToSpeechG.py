import os
from gtts import gTTS
import playsound

def speak(text, lan = 'en'):
	tts = gTTS(text=text, lang=lan)
	audioFile="file.mp3"
	tts.save(audioFile)
	playsound.playsound(audioFile)
	os.remove(audioFile)
	
while True:
	x = input("Enter : ")
	lan = input("Enter language\n en :- Eglish\n ru :- russian: ")
	speak(x,lan)