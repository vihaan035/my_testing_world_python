import pyttsx3
import webbrowser
import smtplib
import random
import speech_recognition as sr
import wikipedia
import datetime
import wolframalpha
import os
import sys

engine = pyttsx3.init('sapi5')

client = wolframalpha.Client('Your_App_ID')

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[len(voices)-1].id)

def speak(audio):
    print('Jarvis: ' + audio)
    engine.say(audio)
    engine.runAndWait()

def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        speak('Good Morning!')

    if currentH >= 12 and currentH < 18:
        speak('Good Afternoon!')

    if currentH >= 18 and currentH !=0:
        speak('Good Evening!')

greetMe()

speak('How may I help you?')

def myCommand():
   
    r = sr.Recognizer()                                                                                   
    with sr.Microphone() as source:                                                                       
        print("Listening...")
        r.pause_threshold =  1
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-in')
        print('Vihaan: ' + query + '\n')
        
    except sr.UnknownValueError:
        speak('Sorry Vihaan! didn\'t get that! Try typing the command!')
        query = str(input('Command: '))

    return query
        

if __name__ == '__main__':

    while True:
    
        query = myCommand();
        query = query.lower()
        
        if 'open youtube' in query:
            speak('okay')
            webbrowser.open('www.youtube.com')

        elif 'open google' in query:
            speak('okay')
            webbrowser.open('www.google.co.in')

        elif 'open gmail' in query:
            speak('okay')
            webbrowser.open('www.gmail.com')

        elif 'play music' in query:
            speak("Here is your music")
            print("Here is your music")
            import Music_Player.py

        elif 'who is Jarvis' in query:
            print("It's me!")

        elif 'play online' in query or 'play music online' in query:
            speak('Ok Vihaan, Redirecting you to Gaana.com')
            webbrowser.open('https://gaana.com/')

        elif 'pinterest' in query or 'open pinterest' in query:
            speak('Ok Vihaan, opening PINTEREST')
            webbrowser.open('https://www.pinterest.com/')

        elif 'facebook' in query or 'open facebook' in query:
            speak('Ok Vihaan, opening FACEBOOK')
            webbrowser.open('https://www.facebook.com/')

        elif 'whatsapp' in query or 'open whatsapp' in query:
            speak('Ok Vihaan, opening WHATSAPP')
            webbrowser.open('https://web.whatsapp.com/')

        elif 'play games' in query or 'games' in query:
            games = ['hangman','snake']
            (random.choice(games))
            if games == 'snake':
                import First_Successful_Pycharm_Project.py
            elif games == 'hangman':
                import Hangman.py

        elif 'open calculater' in query or 'calculator' in query:
            speak("Opening Calculator")
            print("Opening Calculator")
            import Calculator.py

        elif 'start stopwatch' in query or 'stopwatch' in query:
            speak("Starting Stopwatch")
            print("Starting Stopwatch")
            import stop_watch.py
            
        elif "what\'s up" in query or 'how are you' in query:
            stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy']
            speak(random.choice(stMsgs))

        elif 'how are you' in query:
            print("I am fine...")

        elif "tell me a joke" in query or 'joke' in query:
            jokes = ['Mummy, Sofa letne ke liye nahi, baithne ke liye hota hai. Beta, Haan toh Chappal bhi maarne ke liye nahi chalne ke liye hoti hai', 'I am fine!']
            speak(random.choice(jokes))

        elif 'email' in query:
            speak('Who is the recipient? ')
            recipient = myCommand()

            if 'MI' in recipient:
                try:
                    speak('What should I say? ')
                    content = myCommand()
        
                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.ehlo()
                    server.starttls()
                    server.login("vihaangupta035@gmail.com", 'onlysecret@123')
                    server.sendmail("vihaangupta035@gmail.com", "rajeshgpec@gmail.com", content)
                    server.close()
                    speak('Email sent!')

                except:
                    speak('Sorry Sir! I am unable to send your message at this moment!')


        elif 'nothing' in query or 'abort' in query or 'stop' in query or 'exit' in query:
            speak('okay')
            speak('Bye Vihaan, have a good day.')
            sys.exit()
           
        elif 'hello' in query:
            speak('Hello Vihaan')

        elif 'bye' in query:
            speak('Bye Vihaan, have a good day.')
            sys.exit()
                                    
        elif 'play music' in query:
            music_folder = Your_music_folder_path
            music = [music1, music2, music3, music4, music5]
            random_music = music_folder + random.choice(music) + '.mp3'
            os.system(random_music)
                  
            speak('Okay Vihaan, here is your music! Enjoy!')
            

        else:
            query = query
            speak('Searching...')
            try:
                try:
                    res = client.query(query)
                    results = next(res.results).text
                    speak('WOLFRAM-ALPHA says - ')
                    speak('Got it.')
                    speak(results)
                    
                except:
                    results = wikipedia.summary(query, sentences=2)
                    speak('Got it.')
                    speak('WIKIPEDIA says - ')
                    speak(results)
        
            except:
                webbrowser.open('www.google.com')
        
        speak('Next Command! Vihaan!')
