#Import Libraries

from speech_recognition import *
import pyttsx3 as tts
import webbrowser
import re
import os
from datetime import datetime as dt 

'''
Recognizer() -- class used to recognize your voice:
	We used two methods
	listen() --listen voice
	recognize_google()--process our voice in google API

Microphone() -- class used to capture our voice through system mic
'''

# Opening application
open_notepad = r'open (notepad|the notepad)'
open_word = r'open (word|the word|document|the document|word document|the word document)'
open_excel = r'open (excel|the excel|excel file|the excel file)'
open_firefox = r'open (firefox|the firefox|mozilla|the mozilla|mozilla firefox|the mozilla firefox)'
open_chrome = r'open (chrome|the chrome)'


# Closing application
close_notepad = r'close (notepad|the notepad)'
close_word = r'close (word|the word|document|the document|word document|the word document)'
close_excel = r'close (excel|the excel|excel file|the excel file)'
close_firefox = r'close (firefox|the firefox|mozilla|the mozilla|mozilla firefox|the mozilla firefox)'
close_chrome = r'close (chrome|the chrome)'

# Websites
google = r'google|google.com'
youtube = r'youtube|youtube.com'
sentdex = r'pythonprogramming.net|sentdex'
facebook = r'facebook|facebook.com|fb'
snc = r'snc|servicenow|servicenow.com'
udemy = r'udemy|udemy.com'



# Asking questions
asking_qns = r'i am fine how are you|how (are|about) you'

# Date, Time and Day details
date = r'what is the date today|today date|date|the date'
time = r'what is the time today|today time|time|the time|time now'
day = r'what is the day today|day|the day'

days = {'1': 'Monday', '2' : 'Tuesday', '3' : 'Wednesday', '4' : 'Thursday', '5' : 'Friday', '6' : 'Saturday', '7' : 'Sunday'}

# Terminate commands
terminate = r'stop|cancel|exit|quit|good bye|bye|see you|thanks'

running = True

def text_to_speech(cmd):	
	global running
	cmd = cmd.lower()
	engine = tts.init()

# Terminate the program	

	if re.findall(terminate,cmd):
		engine.say('Thanks sir, will see you later.')
		running = False

# Opening the websites

	elif re.findall(google, cmd):
		webbrowser.open('https://www.google.com')
		engine.say('opening google')

	elif re.findall(facebook, cmd):
		webbrowser.open('https://www.facebook.com')
		engine.say('opening facebook')

	elif re.findall(youtube, cmd):
		webbrowser.open('https://www.youtube.com')
		engine.say('opening youtube')

	elif re.findall(sentdex, cmd):
		webbrowser.open('https://www.pythonprogramming.net')
		engine.say('opening pythonprogramming.net')

	elif re.findall(snc, cmd):
		webbrowser.open('https://flextronics.service-now.com')
		engine.say('opening servicenow')

	elif re.findall(udemy, cmd):
		webbrowser.open('https://www.udemy.com/home/my-courses/learning')
		engine.say('opening udemy')


# Opening the Windows Application
	
	elif re.findall(open_notepad, cmd):
		os.system('start notepad.exe')
		engine.say('opening notepad')

	elif re.findall(open_word, cmd):
		os.system('start winword.exe')
		engine.say('opening word document')

	elif re.findall(open_excel, cmd):
		os.system('start excel.exe')
		engine.say('opening excel')

	elif re.findall(open_firefox, cmd):
		os.system('start firefox.exe')
		engine.say('opening firefox')

	elif re.findall(open_chrome, cmd):
		os.system('start chrome.exe')
		engine.say('opening chrome')

# closing the Windows Application

	elif re.findall(close_notepad, cmd):
		os.system("TASKKILL /F /IM notepad.exe")
		engine.say('closing notepad')

	elif re.findall(close_word, cmd):
		os.system("TASKKILL /F /IM winword.exe")
		engine.say('closing word document')

	elif re.findall(close_excel, cmd):
		os.system("TASKKILL /F /IM excel.exe")
		engine.say('closing excel')

	elif re.findall(close_firefox, cmd):
		os.system("TASKKILL /F /IM firefox.exe")
		engine.say('closing firefox')

	elif re.findall(close_chrome, cmd):
		os.system("TASKKILL /F /IM chrome.exe")
		engine.say('closing chrome')

# Interacting with Bot

	elif cmd =='what' and cmd == 'your name' or cmd =='what is your name' or cmd == 'who are you' or (cmd == 'give me' and cmd == 'intro'):
		engine.say('i am your python commander. you created me and i am here to assist you sir.')
		print('i am your python commander. you created me and i am here to assist you sir.')

	elif re.findall(asking_qns, cmd):
		engine.say('Thanks for asking me. I am fine sir.')
		print('Thanks for asking me. I am fine sir.')

	elif cmd == 'what is your favourite colour':
		engine.say('i like blue, because i like sky')
		print('blue')


# Date, Time and Day details

	elif re.findall(date, cmd):
		engine.say(str(dt.today())[0:10])
		print(str(dt.today())[0:10])

	elif re.findall(time, cmd):
		engine.say(str(dt.today())[11:19])
		print(str(dt.today())[11:19])

	elif re.findall(day, cmd):
		no = str(dt.today().isoweekday())
		engine.say(days[no])
		print(days[no])


# It will tell , what we told it

	else:
		engine.say(cmd)
	engine.setProperty('rate', 100)
	engine.setProperty('volume', 1)
	engine.runAndWait()


def speech_to_text():

	r = Recognizer()

	with Microphone() as voice:
		print('I am listening you, say something.....')
		audio = r.listen(voice)

	command = ''
	try:
		command = r.recognize_google(audio)	
	except UnknownValueError:
	    print("Could not understand audio")
	except RequestError as e:
	    print("Could not request results; {0}".format(e))
	
	print('Bro you said '+ command)
	text_to_speech(command)

while running:
	speech_to_text()
