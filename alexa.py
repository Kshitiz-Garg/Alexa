import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia #pip install wikipedia
import smtplib
import webbrowser as wb
import psutil #pip install psutil
import pyjokes #oio install pyjokes
import os



engine=pyttsx3.init()
def speak(audio):
   engine.say(audio)
   engine.runAndWait()

def time_():
   Time = datetime.datetime.now().strftime("%H:%M:%S")
   speak("Current time is")
   speak(Time)

def date_():
  year = datetime.datetime.now().year  
  month = datetime.datetime.now().month
  date = datetime.datetime.now().day
  speak(date)
  speak(month)
  speak(year)


def wishme():
  speak("welcome back narayan! hope you are well today!")  
  time_()
  date_()

#greetings

hour=datetime.datetime.now().hour
if hour>=12 and hour<=24:
    speak("Good Morning Sir!")
elif hour>=00 and hour<=4:
   speak("Good Afternoon Sir!")
elif hour>=4 and hour<6:
    speak("Good Evening Sir!")
else:
    speak("Good Night Sir!")    

speak("Narayan at your service! what can i do for you! I Can Do Anything What you want")

def TakeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
       print("Listening....")
       r.pause_threshhold=1
       audio = r.listen(source)

    try:
        print("recognizing")
        query = r.recognize_google(audio,language='en-US')
        print(query)
    except Exception as e:
        print(e)
        print("say that again please...")
        return "None"
    return query
def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    #for this function, you must enable low security in you gmail which you are going to use as sender
    server.login('username@gmail.com','password')
    server.sendmail('username@gmail.com',to,content)
    server.close


def cpu():
    usage = str(psutil.cpu_percent())
    speak('CPU is at'+usage)


    battery = psutil.sensors_battery()
    speak('Battery is at')
    speak(battery.percent)

def joke():
    speak(pyjokes.get_joke())



if __name__ == "__main__":  
    wishme()
    while True:
        query = TakeCommand().lower()
        #All commands will be stored in lower case in query
        #for easy recogniztion
        if 'time' in query: #tell us time when asked
            time_()
        if 'date' in query: #tell us date when asked
            date_()    
        elif 'wikipedia' in query:
            speak("searching...")
            query=query.replace('wikipedia','')
            result=wikipedia.summary(query,sentences=3)
            speak('Acording to wikipedia')
            print(result)
            speak(result)
        elif 'sendEmail' in query:
            try:
                speak("What should i say?")   
                content=TakeCommand()
                #provide reciver email address
                speak("who is the Reciver?")
                reciver=input("Enter Reciver's Email :")
                to = reciver 
                sendEmail(to,content)
                speak(content)
                speak('Email has been sent.')
            except Exception as e:
                print(e)
                speak("unable to send Email.") 

        elif 'search in chrome' in query:
            speak('What should I search?')
            chromepath ='C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s'      
            #chromepath is location of chrome's installation on computer
            search = TakeCommand().lower()
            wb.get(chromepath).open_new_tab(search+'.com') #only open website with '.com' at end.
             

        elif 'search youtube' in query:
              speak('What should I search?')
              search_Term = TakeCommand().lower()
              speak("Here We go to YOUTUBE!")
              wb.open('https://www.youtube.com/results?search_query='+search_Term)
        elif 'search google' in query:
            speak('What should I search?')
            search_Term = TakeCommand().lower()
            speak('Searching....')
            wb.open('https://www.google.com//searching?q='+search_Term)

        elif'cpu'  in query:
            cpu()


        elif 'joke' in query:
            joke()



        elif 'go offline' in query:
            speak('Going offline Sir!')
            quit()

        elif 'word' in query:
            speak('Opening MS Word....')
            ms_word = r"C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE"
            os.startfile(ms_word)

        elif 'write a note' in query:
            speak ('What should i write, Sir! ')   
            notes = TakeCommand()
            file = open('notes.text','w')
            speak("Sir should I Include Date and Time?")
            ans = TakeCommand()
            if 'yes' in ans or 'sure' in ans:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                file.write(strTime)
                file.write(':-')
                file.write(notes)
                speak('Done Taking Notes,STR!')
            else:
                file.write(notes)  

        elif 'show notes' in query:
            speak('showing notes')
            file=open('notes.txt','r')
            print(file.read())
            speak(file.read())
        elif 'play music' in query:
            songs_dir = 'D:\song'
            music = os.listdir(songs_dir)
            speak('What Should I Play?')
            ans = TakeCommand().lower()
            no = int(ans.eplace('number',''))
            os.startfile(os.path.join(songs_dir,music[no]))

