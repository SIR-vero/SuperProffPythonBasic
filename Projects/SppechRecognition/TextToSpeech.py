import pyttsx3
def SpeakText(command): 
      
    # Initialize the engine 
    engine = pyttsx3.init() 
    engine.say(command)  
    engine.runAndWait() 
	
com = input("Enter text : ")
com = com.lower()
SpeakText(com)