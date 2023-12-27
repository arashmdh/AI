import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import weather
import webbrowser
import wolframalpha
import os



listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[10].id)
activationword = 'anita'

# Wolfram Alpha client
appId = '9H28QX-7T5UPXG7TR'
wolframClient = wolframalpha.Client(appId)

def talk(text, rate=1):
    engine.setProperty('rate', rate) 
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('Listening ...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice,language='en_US')
            command = command.lower()
            #if 'anita' in command:
                #command = command.replace('anita', '')
    except:
        pass
    return command




def listOrDict(var):
    if isinstance(var, list):
        return var[0]['plaintext']
    else:
        return var['plaintext']    



def search_wolframalpha(keyword=''):
    response = wolframClient.query(keyword)
    # @success: Wolfram Alpha was able to resolve the query
    # @numpods: Number of results returned
    # pod: List of results. This can also contain subpods

    # Query not resolved
    if response['@success'] == 'false':
        talk('I could not compute')
    # Query resolved
    else: 
        result = ''
        # Question
        pod0 = response['pod'][0]
        # May contain answer (Has highest confidence value) 
        # if it's primary or has the title of result or definition, then it's the official result
        pod1 = response['pod'][1]
        if (('result') in pod1['@title'].lower()) or (pod1.get('@primary', 'false') == 'true') or ('definition' in pod1['@title'].lower()):
            # Get the result
            result = listOrDict(pod1['subpod'])
            # Remove bracketed section
            return result.split('(')[0]
        else:
            # Get the interpretation from pod0
            question = listOrDict(pod0['subpod'])
            # Remove bracketed section
            question = question.split('(')[0]
            # Could search wiki instead here? 
            return question    


def run_Anita():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)

    
    #elif query[0] == 'compute' or query[0] == 'computer':
               # query = ' '.join(query[1:])
                #try:
                    #result = search_wolframalpha(query)
                    #talk(result)
               # except:
                    #talk('Unable to compute')

    if 'compute' in command:
        
        compute = ' '.join(compute[1:])
        
        result = search_wolframalpha(compute)
        talk(result)
    

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is' + time)

    elif 'you answered' in command:
        talk('Sorry, I was Studying')
        


    elif 'search' in command:
        info = webbrowser.Chrome()
        print(info)
        talk('Opening browser')

    elif 'who is' in command:
        person = command.replace('Who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)

    elif 'what is' in command:
        person = command.replace('what is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)    

    elif 'tell me' in command:
        person = command.replace('tell me', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)    

    elif 'good morning' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('I Still have no idea it is morning or night or whatever, but I can tell you time is ' + time)


    elif 'good evening' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('I Still have no idea it is morning or night or whatever, but I can tell you time is ' + time)    


    elif 'good night' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('I Still have no idea it is morning or night or whatever, but I can tell you time is ' + time)    


    elif 'anita' in command:
        talk('How can I help you?')

    elif 'love you' in command:
        talk('Thanks but I am not ready for love')


    elif 'laugh' in command:
        talk('Let me know if you want hear my jokes')

    elif 'who are you' in command:
        talk('my name is Anita, I am your assistant')   

    elif 'how are you' in command:
        talk('Thanks, I am fine') 

    elif 'joke' in command:
        talk(pyjokes.get_joke)

    elif 'fun' in command:
        talk(pyjokes.get_joke)

    elif 'bored' in command:
        talk(pyjokes.get_joke)  

    elif 'hello' in command:
        talk('Hello, How can I help you?')

    elif 'hi' in command:
        talk('Hi there, How can I help you?')

    elif 'owner' in command:
        talk('I am developed by Arash')

    elif 'are you from' in command:
        talk('I born and rais in Sweden')

    elif 'your name' in command:
        talk('my name is Anita, I am your assistant')
    elif 'you name' in command:
        talk('my name is Anita, I am your assistant')
    elif 'old are you' in command:
        talk('I just born but I am growing fast')    

    elif 'where you' in command:
        talk('I was Studying')

    elif 'help' in command:
        talk('Thanks for asking, at the momment I can help you with the weather and time, search for the information or play music or movie for you. By the way I can make you laugh. This is my fun part')   
    else:
        talk('Please repeat again.')



while True:
 run_Anita()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()