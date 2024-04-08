import subprocess
import datetime
import pyautogui
import speech_recognition as sr
import smtplib
import wikipedia
import webbrowser
import pywhatkit
import clipboard
import os
import pytesseract
import pyperclip
import openai
import pyjokes
import string
import random
from nltk.tokenize import word_tokenize




# Set up OpenAI API key
openai.api_key = 'your API key'

def speak(audio, voice="Daniel"):
    subprocess.run(["say", "-v", voice, audio])

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak('The current time is', voice="Daniel")
    speak(Time, voice="Daniel")

def date():
    now = datetime.datetime.now()
    Year = now.year
    month = now.strftime("%B")  # Full month name
    date = now.day
    full_date = f'{date} {month} {Year}'
    speak('Today is', voice="Daniel")
    speak(full_date, voice="Daniel")

def greetings():
    Hour = datetime.datetime.now().hour
    if 6 <= Hour < 12:
        speak("Good Morning chief", voice="Daniel")
    elif 12 <= Hour < 18:
        speak("Good Afternoon chief!", voice="Daniel")
    elif 18 <= Hour < 24:
        speak("Good Evening Chief", voice="Daniel")
    else:
        speak("Good Night Chief", voice="Daniel")
    
def wishme():
     
      speak("Welcome back chief!", voice="Daniel")
wishme()
time()
date()
greetings()
speak("Linga at your service, please tell me how can I help you chief?", voice="Daniel")


def takeCommandCMD():
    query = input("please tell me how can I help you chief?\n")
    return query


def takeCommandMic():
    r = sr.Recognizer()
    with sr.Microphone()  as source:
        print("Listening...")
        r.pause_threshold = 1
        try:
            audio = r.listen(source) 
            print("Recognizing")
            query = r.recognize_google(audio, language='en-IN')
            print(query)
            return query
        except Exception as e:
            print(e)
            speak("Say that again please")
            return "None"


def SentMail():

    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()





def searchgoogle():
    query = takeCommandMic().lower()
    if 'linga search on google' in query:
        speak("What should I search, chief?")
        search = takeCommandMic()
        webbrowser.open('https://www.google.com/search?q=' + search)
    else:
        speak("Sorry, I didn't understand that command.")

searchgoogle()



def playyoutube():
    query = takeCommandMic().lower()
    if 'play video in youtube' in query:
        speak("What video should I search on YouTube, chief?")
        topic = takeCommandMic()
        pywhatkit.playonyt(topic)
    else:
        speak("Sorry, I didn't understand that command.")

playyoutube()

def t2s():
    text = clipboard.paste()
    if text:
        print(text)
        speak(text)
    else:
        speak("Sorry, there is no text copied to the clipboard.")


def open_website():
    speak("Which website do you want to open?")
    website = takeCommandMic().lower()

    if website == "google":
        webbrowser.open("https://www.google.com")
    elif website == "youtube":
        webbrowser.open("https://www.youtube.com")





def read_code_from_screen():
    # Use pytesseract to read text from the screen
    # (Note: You need to have Tesseract-OCR installed on your system)
    # Adjust the coordinates according to the region where the code is displayed on your screen
    code = pytesseract.image_to_string('screenshot.png')
    return code


def read_code_from_clipboard():
    # Use pyperclip to get text from the clipboard
    code = pyperclip.paste()
    return code

def ask_gpt(question, context):
    response = openai.Completion.create(
      engine="davinci",
      prompt=f"Question: {question}\nContext: {context}\nAnswer:",
      temperature=0.5,
      max_tokens=150
    )
    answer = response.choices[0].text.strip()
    return answer

def display_answer(answer):
    speak("Here's the answer:")
    speak(answer)
    # Copy the answer to clipboard
    pyperclip.copy(answer)

def solve_coding_problem():
    code = read_code_from_clipboard()
    speak("What do you want to ask about the code?")
    question = input("Enter your question: ")
    answer = ask_gpt(question, code)
    display_answer(answer)

def screenshot():
    name_img=  (datetime.datetime.now().timestamp())
    name_img = '//Users//yogeshdevil//Desktop//jarvis//screenshot'
    img = pyautogui.screenshot(name_img)
    img.show()


def passwordgen():
    s1 = string.ascii_uppercase
    s2 = string.ascii_lowercase
    s3 = string.digits
    s4 = string.punctuation

    passlen = 8
    s =[]
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))

    random.shuffle(s)
    newpass = (" ".join(s[0:passlen]))
    print(newpass)
    speak(newpass)

def flip():
    speak("Flipping a coin... cheif")
    coin = ['heads','tails']
    toss = []
    toss.extend(coin)
    random.shuffle(toss)
    toss = (" ".join(toss[0]))
    speak ("The result is " + toss)


if __name__ == "__main__":
    while True:
        query = takeCommandMic().lower()
        query = word_tokenize(query)
        print(query)
        
        if 'solve' in query:
            solve_coding_problem()
        
        elif 'time' in query:
            time()
        
        
        elif 'date' in query:
            date()
        
        
        
        elif 'wikipedia' in query:
            speak("Searching on Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        
        
        elif 'linga search on google' in query:
            searchgoogle()

        elif 'youtube' in query:
            playyoutube()

        elif 'open website' in query:
            open_website()




        elif 'read' in query:
            t2s()
        

        elif 'open' in query:
            os.system();
        # paste the path which to open by jarvis
        
        elif 'jokes' in query:
            speak(pyjokes.get_joke())

        elif 'screenshot' in query:
            screenshot()
        
        elif 'remember that'  in query:  # Remember this as a fact
            speak("What should i remember cheif?")
            data = takeCommandMic()
            speak= ("You said me to remember that" +data)
            remember = open('data.txt','w')
            remember.write(data)
            remember.close()


        elif 'Do you know anything' in query:
            remember = open('data.txt','r')
            speak("You told me to remember that "+remember.read())

        elif 'password' in query:
            passwordgen()


        elif 'flip' in query:
            flip()
        

        elif 'offline' in query:
            quit()


