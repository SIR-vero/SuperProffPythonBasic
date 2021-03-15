import speech_recognition as sr

r = sr.Recognizer()

so = sr.AudioFile('recording1.wav')

with so as source:
	print("Say something ")
	audio = r.record(source)
	
	try:
		text = r.recognize_google(audio)
		print("You said : {}".format(text))
	except Exception as e:
		print(e)