import pyttsx3
import pyaudio
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
engine=pyttsx3.init('sapi5') #windows api for voices
voices=engine.getProperty('voices')
engine.setProperty('voices',voices[1].id)
# print(voices[1].id) #dui voices hunchha male and female. 1 is for female. female voice liye maile

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning aarya!")
    elif hour>=12 and hour<18:
        speak("good afternoon")
    else: 
        speak("good evening")
    speak("i am jarvis, please tell me how i can help you")
def takeCommand():
    #it takes microphone input from the user and returns string output
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold =1 #maaile bolda boldai 1 second pause gare bhane jarvis le mero command lai tyo point ma complete assume na garos
        audio=r.listen(source)
    try:
        print("recognizing...")
        query=r.recognize_google(audio, language='en-in')
        print(f"User said :{query}\n")
    except Exception as e:
        # print(e)
        print("say that again please...")
        return "None"
    return query 
def sendEmail(to, content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com','your-password')
    server.send('youremail@gmail.com',to,content)
if __name__=="__main__":
    wishMe()
    if 1: 
      query = takeCommand().lower()
      #logic for executing tasks based on query
      if 'wikipedia' in query:
          speak('Searching Wikipedia...')
          query=query.replace("wikipedia","")
          results=wikipedia.summary(query,sentences=2)
          #wikipedia bata 2 sentences return garcha
          speak("according to wikipedia")
          print(results)
          speak(results)
      elif "open youtube" in query:  
          webbrowser.open("youtube.com")
      elif "open google" in query:  
          webbrowser.open("google.com")
      elif "open stackoverflow" in query:  
          webbrowser.open("stackoverflow.com")
      elif 'play music' in query: 
          music_dir="D:\\Non critical\\songs\\favorite Songs2"
          songs = os.listdir(music_dir)
          print(songs)
          os.startfile(os.path.join(music_dir, songs[0]))
      elif 'the time' in query:
          strTime=datetime.datetime.now().strftime("%H:%M:%S")
          speak(f"the time is {strTime}")
      elif 'open code' in query:
         codePath="C:\\Users\\Dell\\AppData\\Local\\Programs\\Microsoft VS Code\Code.exe" 
         os.startfile(codePath)
      elif 'email to harry' in query:
          try:
              speak("what should i send")
              content=takeCommand() #je bolecko chu teslai string ma return garcha takecommand le 
              to = "harryyouremail@gmail.com"
              sendEmail(to, content)
              speak("Email has been sent")
          except Exception as e:
              print(e)
              speak("couldnt send email")


