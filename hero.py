import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes


listener=sr.Recognizer()
engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[10].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


#wish you as per time of day
def wishMe():
    hour = int(datetime.datetime.now().hour)
    print(hour)


    if hour>0 and hour<12:
        talk('Good Morning' )
    elif hour>=12 and hour <18:
        talk('Good Afternoon')
    

    else:
        talk('Good Evening' )
    
    talk('Initializing Jarvis. How is your day, how may i help you today')

def take_command():
    try:
        with sr.Microphone() as source:
            print('listening..')
            voice=listener.listen(source)
            command=listener.recognize_google(voice)
            command=command.lower()
            if 'jarvis' in command:
                command=command.replace('jarvis', '')
                print(command)
            
                

          
    except:
        pass
    return command
   
    

def run_jarvis():
    command=take_command()
    print(command)
    if 'play' in command:
        song=command.replace('play', '')
        talk('playing'+ song)
        pywhatkit.playonyt(song)

    elif 'google' in command:
        results=command.replace('google', '')
        talk('googling'+ results)
        pywhatkit.search(results)
        talk(results)

    elif 'time' in command:
        time=datetime.datetime.now().strftime('%I:%M %p')
        talk(' the time is ' + time)
        print(time)

    elif 'wikipedia' in command:
        query=command.replace('wikipedia', '')
        info=wikipedia.summary(query,2)
        print(info)
        talk(info)

    elif 'joke' in command:
        talk(pyjokes.get_joke())

    elif 'send' in command:
        message=command.replace('send', '')
        talk('sending' + message)
        pywhatkit.sendwhatmsg('+6591913519', message ,16,13)

    else:
        talk(' Please repeat your question or request')

#wishMe()
while True:
    run_jarvis()
   

