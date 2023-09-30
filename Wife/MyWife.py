
import speech_recognition as sr# for we to speek with my future wife
import pyttsx3# for my future wife to speek with me
import pywhatkit #to playing the song in youtube
import datetime

listner=sr.Recognizer()
engine=pyttsx3.init()#  creating engine which speek with us and intialised it
voices=engine.getProperty('voices')# getting the voice property
engine.setProperty('voice',voices[1].id)# setting the voice to femail voice

def talk(text): #defing the function which get input as text give thevoice output
        engine.say(text)
        engine.runAndWait()
def take_command():
    try:
        with sr.Microphone() as source:
            print("Listening.....")
            voice=listner.listen(source)
            command=listner.recognize_google(voice)
            command=command.lower()
            if 'future wife' in command:#printing output only when future wife is in command
                command=command.replace('future wife','')#we dont want to search or proced with command including "future wife"
                print(command)#passing command as a text to talk
    except:
        pass
    return command
def run_future_wife():
    command=take_command()#returned command is assigned to the command
    print(command)
    if 'play' in command:
        song = command.replace('play','')
        talk('playing'+song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time=datetime.datetime.now().strftime('%I:%M %p')
        talk('current time is '+time)
    elif 'how' in command:
        h='I am fine How are you ?'
        talk(h)
        run_future_wife()
    elif 'fine' in command:
        f='ok what are you doing'
        talk(f)
    elif'jevan' in command:
        t='Not yet What About You ?'
        talk(t)

    elif'talk' in command :
        v='Yes tell me i  am  hear to listen you only '
        talk(v)
    elif'marry' in command :
        m='First get a better job And then Ask'
        talk(m)
        
        
    elif'give' in command :
        g='God bless You !'
        talk(g)

run_future_wife()