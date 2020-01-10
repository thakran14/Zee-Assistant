import pyttsx3
import datetime
import pyaudio
import webbrowser
import wikipedia
import os
import speech_recognition as sr
import sys


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[1].id)



def speak(audio):
 engine.say(audio)
 engine.runAndWait()
 
 
def wishMe():
 hour = int(datetime.datetime.now().hour)
 if hour>=0 and hour<12:
  print("Good morning")
  speak("Good morning")

  
 elif hour>=12 and hour<18:
  print("Good afternoon")
  speak("Good afternoon")
  
 else:
  print("Good evening")
  speak("Good evening")
 print("Hi! My name is Zee! How can I help you!\n")
 speak("Hi! My name is Zee! How can I help you!")
 
 print("I can open common websites like Google, Youtube, FaceBook and LinkedIn")
 speak("I can open common websites like Google, Youtube, FaceBook and LinkedIn")

 print("Search for anything on wikipedia")
 speak("Search for anything on wikipedia")

 print("Tell you the time!\n")
 speak("Tell you the time!\n")

 print("To exit, say bye\n")
 speak("To exit, say bye\n")
 
def takeCommand():
 r = sr.Recognizer()
 with sr.Microphone() as source:
  print("Listening. . .")
  r.pause_threshold = 1
  audio = r.listen(source)

 try:
  print("Recognizing. . .")
  query = r.recognize_google(audio, language='en-in')
  print(f"User said: {query}\n")
  
 except Exception as e:
  # print(e)
  print("Say that again please. . .")
  return "None"
 return query 


if __name__ == "__main__":
 wishMe()
 while True:
  query = takeCommand().lower()
  
  #logic
  if 'wikipedia' in query:
   speak('Searching Wikipedia')
   query = query.replace("wikipedia","")
   results = wikipedia.summary(query, sentences=2)
   speak("According to wikipedia")
   print(results)
   speak(results)
   
  elif 'open youtube' in query:
   webbrowser.open("youtube.com")
   
  elif 'open google' in query:
   webbrowser.open("google.com")
   
  elif 'open facebook' in query:
   webbrowser.open("facebook.com")
   
  elif 'open google' in query:
   webbrowser.open("linkedin.com")
  
  elif 'the time' in query:
   strTime = datetime.datetime.now().strftime("%H:%M:%S")
   speak(f"Time is {strTime}")
   
  elif 'bye' in query:
   print("It was nice meeting you, goodbye")
   speak("It was nice meeting you, goodbye :)")

   sys.exit(0)

 
 
 