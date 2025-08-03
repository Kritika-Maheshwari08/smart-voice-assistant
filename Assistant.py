import pyttsx3
import datetime
import wikipedia
import speech_recognition as sr
import webbrowser
import os
print("Control your digital world with just your voice, meet Kritika's smart assistant!")
print("Speak up Quit or Exit for ending... Let's Begin :)")
# Initialize text-to-speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# Set to a female voice (usually index 1)
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 150)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Hello.Good morning. I am Kritika's made assistant. How may I assist you? Speak your needs — from Google to Spotify, your assistant handles it all!")
        
    elif 12 <= hour < 18:
        speak("Hello. Good afternoon. I am Kritika's made assistant. How may I assist you?Speak your needs — from Google to Spotify, your assistant handles it all!")
    else:
        speak("Hello. good evening. I am Kritika's made assistant. How may I assist you? Speak your needs — from Google to Spotify, your assistant handles it all! ")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}\n")
    except Exception:
        print("Please say that again.")
        return "none"
    return query
   
if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()           
        if 'wikipedia' in query:
            print("Please wait. I am searching on Wikipedia.")
            query = query.replace('wikipedia', '')
            try:
                results = wikipedia.summary(query, sentences=2)
                clean_results = results.encode('ascii', 'ignore').decode('ascii') # Remove non-ASCII chars
                print(clean_results)
            except Exception as e:
                print("Error fetching Wikipedia summary:", str(e))
                print("Sorry, I could not find that on Wikipedia.")
        elif ' youtube' in query:
            print("Opening YouTube.")
            webbrowser.open("https://www.youtube.com")       
        elif ' google' in query or 'chrome' in query:
            print("Opening Google.")
            webbrowser.open("https://www.google.com")      
        elif ' instagram' in query or 'login instagram' in query:
            print("Opening Instagram.")
            webbrowser.open("https://www.instagram.com/")  
        elif ' music' in query or ' song' in query or ' spotify' in query:
            print("Opening the spotify for you :)")
            webbrowser.open("https://open.spotify.com/track/6G8vN5EUtcDxOXOXadF6kp")        
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"DEBUG: Time is {strTime}")
        elif 'date' in query:
            today = datetime.datetime.now().strftime("%A, %d %B %Y")
            print(f"Today is {today}")
        elif 'linkedin' in query:
            print("Opening linkedin.")
            webbrowser.open("https://www.linkedin.com/feed/") 
        elif ' github' in query:
            print("Opening github.")
            webbrowser.open("https://github.com/") 
        elif 'exit' in query or 'quit' in query:
            speak("Goodbye! Have a great day.")
            break
