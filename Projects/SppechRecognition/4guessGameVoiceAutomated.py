# Create a random number using random module.
# ask the User to guess that number.
# give the user 10 tries.

import random
import speech_recognition as sr
import os
from gtts import gTTS
import playsound
random_num = random.randint(1, 100)

#print("ran num: ", random_num)


def listen():
	r = sr.Recognizer()

	with sr.Microphone() as source:
		print("Say Something: ")
		audio = r.listen(source)
		
		try:
			text = r.recognize_google(audio)
			return text
		except Exception as e:
			print(e)



def speak(text, lan = 'en'):
	tts = gTTS(text=text, lang=lan)
	audioFile="file.mp3"
	tts.save(audioFile)
	playsound.playsound(audioFile)
	os.remove(audioFile)
	


speak("we have a random number between 1-100 ")
speak("guess that number")
speak("(you have 10 tries)")

count = 1
while count <= 10:
	speak("What's your guess: ")
	x = int(listen())
	if x == random_num:
		speak("you guessed correct! ")
		break
	else :
		speak("WRONG, you have " + str(10-count) + " tries left")
		if random_num < x:
			speak("go a little lower !")
		else:
			speak("go a little higher !")
	count = count + 1
if x == random_num:
	speak("Congrats ! ")
else:
	speak("no tries left the number was " + str(random_num))


