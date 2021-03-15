# import required libraries 
import sounddevice as sd  
import wavio as wv
import speech_recognition as sr 

# Sampling frequency 
freq = 44100

# Recording duration 
duration = int(input("Please Enter the Duration of recording in seconds "))
print("Recording duration is set to : ", duration)
print("Say Something for ", duration, " seconds")

# Start recorder with the given values 
# of duration and sample frequency 
recording = sd.rec(int(duration * freq), 
				samplerate=freq, channels=2) 

# Record audio for the given number of seconds 
sd.wait() 

# Convert the NumPy array to audio file 
wv.write("recording1.wav", recording, freq, sampwidth=2)

#recording saved Now Convert

r = sr.Recognizer()

so = sr.AudioFile('recording1.wav')

with so as source:
	print("getting Audio File...")
	audio = r.record(source)
	
	try:
		print("Converting...")
		text = r.recognize_google(audio)
		print("You said : {}".format(text))
	except Exception as e:
		print(e)