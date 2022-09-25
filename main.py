import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia

listener =sr.Recognizer()


engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print("listening...")
            voice=listener.listen(source)
            command =listener.recognize_google(voice)
            command = command.lower()
            if 'victoria' in command:
                command=command.replace('victoria','')
                print(command)

    except:
        pass

    return command

def run_victoria():
    command=take_command()
    print(command)
    if 'play' in command:
        song=command.replace('play','')
        talk('playing' +song)
        pywhatkit.playonyt(song)
    elif 'the time' in command:
        time=datetime.datetime.now().strftime('%I:%M %p')
        time=time.replace(':','    ')
        time=time.replace('00','0')
        time = time.replace('01', '1')
        time = time.replace('02', '2')
        time = time.replace('03', '3')
        time = time.replace('04', '4')
        time = time.replace('05', '5')
        time = time.replace('06', '6')
        time = time.replace('07', '7')
        time = time.replace('08', '8')
        time = time.replace('09', '9')
        print(time)
        talk('time is ' + time)
    elif 'who is' in command:
        person=command.replace('who is','')
        info=wikipedia.summary(person,2)
        print(info)
        talk(info)

    else:
        talk('please say the command again')
while True:
    run_victoria()