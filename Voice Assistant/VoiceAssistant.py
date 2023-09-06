import pyttsx3  # text to speech conversion
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import gtts
import googletrans
import playsound

# initialize text to speech engine. "sapi5 is the microsoft speech api, commonly used for windows"
engine = pyttsx3.init('sapi5')

voices = engine.getProperty('voices')  # to get the list of available voices

# setting the voice to be used by the engine
engine.setProperty('voice', voices[1].id)


def speak(audio):  # speak function takes text as input
    engine.say(audio)  # convert this text to speech
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if (hour >= 0 and hour < 12):
        speak("Godd Morning!")
    elif hour >= 0 and hour < 18:
        speak("good Afternoon!")
    else:
        speak("good Evening!")

    speak("I am Jarvis, how may i help you")


def takeCommand():
    # create recognizer onject from Recognizer class. This object is used to recognize speech
    r = sr.Recognizer()

    with sr.Microphone() as src:  # "with" is a context manager in py. Context managers ensure that resources are properly acquired and released when they are no longer needed   sr.Microphone is used to activate mic. src is an instance of microphone
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(src)  # this returns an audio type object
        # now convert the audio into text
        # print(audio)

    try:
        print("Recognizing...")
        # converts the audio into text
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"

    return query 

# def translategl(query):
#     speak("translating into hindi")
#     translator = Translator()


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        # logics for executing task
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak("opening youtube")
            webbrowser.open('youtube.com')

        elif 'open google' in query:
            speak("opening google")
            webbrowser.open('google.com')

        elif 'play music' in query:
            music_dir = ''
            music_dir = 'C:\\songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\mehta\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            speak("opening code")
            os.startfile(codePath)
            
        elif "translate" in query:
            speak("translating in hindi")
            translator = googletrans.Translator()
            query = query.replace("translate" ," ")
            translation = translator.translate(query, dest="hi")
            converted_audio = gtts.gTTS(translation.text, lang="hi")
            converted_audio.save("hello.mp3")
            print(translation.text)
            playsound.playsound("hello.mp3")
