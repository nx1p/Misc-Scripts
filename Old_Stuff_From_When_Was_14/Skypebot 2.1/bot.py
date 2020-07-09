import aiml
import Skype4Py
import commands
import sys
import time
import commands
import urllib2
import json
import time
from time import gmtime, strftime
from threading import Thread
from os import system
import marshal # sesje
import os.path
from random import randint
import json
from pprint import pprint
global skype
global k
k = aiml.Kernel()
skype = Skype4Py.Skype()
skype.Attach()
brain="brain.br"
pre = []
 
# read dictionary and create brain in file brain.brp
 
if os.path.isfile(brain):
	k.bootstrap(brainFile = brain)
else:
	homedir=os.getcwd()
	#Change to the directory whe	re the AIML files are located
	os.chdir('./dic') # going to dictionary
	list=os.listdir('./');
	for item in list: #load dictionary one by one
		k.learn(item)
	   
	 
	#k.setPredicate("master","ravi")
	 
	#Change back to homedir to save the brain for subsequent loads
	os.chdir(homedir)
	k.saveBrain(brain) # save new brain


# name of bot
nameb = 'KiritoBot'
k.setBotPredicate('name', nameb)
k.setBotPredicate('master', 'Kirito')


def addcontact(user):
	if user.IsAuthorized == False:
		user.IsAuthorized = True
		print "Added new contact called: " + user.Handle
		skype.SendMessage(user.Handle, "Type !commands for list of commands")

def status(Message, Status):
	if Status == 'RECEIVED': 
		Thread(target=process, args=(Message,1)).start()
def spam(user, times, *args):
	x = 0
	global skype
	while(x < times):
		msgj = str(randint(10000000000000 ,1000000000000000000))
		skype.SendMessage(user, msgj)
		x += 1
def process(Message, *args):
	global k
	bl = open('blacklist.txt').read().splitlines()
	netfl = open('netflix.txt').read().splitlines()
	mc = open('mc.txt').read().splitlines()
	pre = open('pre.txt').read().splitlines()
	admin = open('admin.txt').read().splitlines()
	ban = open('ban.txt').read().splitlines()
	input = Message.Body
	fromMsg = Message.FromHandle
	print fromMsg + '> ' + input
	#input = raw_input("YOU> " )
	if fromMsg in admin:
		if input.startswith("!pre"):
			input = input.replace("!pre ", "")
			if input in pre:
				Message.Chat.SendMessage('User ' + input + ' is already a premuim user.')
			else:
				with open("pre.txt", "a") as text_file:
					text_file.write(input + '\n')
				pre.append(input)
				Message.Chat.SendMessage('User ' + input + ' is now a premuim user.')
		#if "!blacklist" in input:
		#	input = input.replace("!blacklist ", "")
		#	if input in bl:
		#		Message.Chat.SendMessage('User ' + input + ' is already in the skype resolver blacklist.')
		#	else:
		if input.startswith("!blacklist"):
			input = input.replace("!blacklist ", "")
			if input in bl:
				Message.Chat.SendMessage('User ' + input + ' is already in the Blacklist.')
			else:
				with open("blacklist.txt", "a") as text_file:
					text_file.write(input + '\n')
				bl.append(input)
				Message.Chat.SendMessage('User ' + input + ' is now in the Blacklist.')
		if input.startswith("!ban"):
			input = input.replace("!ban ", "")
			if input in ban:
				Message.Chat.SendMessage('User ' + input + ' is already banned.')
			else:
				with open("ban.txt", "a") as text_file:
					text_file.write(input + '\n')
				ban.append(input)
				Message.Chat.SendMessage('User ' + input + ' is now banned!')
	else:
		if input.startswith("!pre"):
			Message.Chat.SendMessage('Sorry, but you have to be admin for that.')
		if input.startswith("!blacklist"):
			Message.Chat.SendMessage('Sorry, but you have to be admin for that.')
		if input.startswith("!ban"):
			Message.Chat.SendMessage('Sorry, but you have to be admin for that.')
	if fromMsg in ban:
		if input.startswith("!"):
			Message.Chat.SendMessage("Sorry, but you're banned. :P")
		if input.startswith("#"):
			Message.Chat.SendMessage("Sorry, but you're banned. :P")
	else:
		if fromMsg in pre:
			if '!netflix' == input:
				netnum = randint(0,len(netfl)-1)
				Message.Chat.SendMessage(netfl[netnum]) 
			if '!mc' == input:
				mcnum = randint(0,len(netfl)-1)
				Message.Chat.SendMessage(mc[mcnum])
		else:
			if '!netflix' == input:
				Message.Chat.SendMessage("Sorry, but you're not premuim. :P")
			if '!mc' == input:
				Message.Chat.SendMessage("Sorry, but you're not premuim. :P")		
		if "!online" == input:
			Message.Chat.SendMessage("I am online.")
		if input.startswith("!spam"):
			inputt = input.replace("!spam ", "").split()
			user = inputt[0]
			k = 1
			if len(inputt) == 2:
				if inputt in bl:
					Message.Chat.SendMessage("I'm Sorry. That username is blacklisted.")
				else:
					try:
						times = int(inputt[1])
					except:
						Message.Chat.SendMessage("Usage: !spam <username> <amount>")
						k = 0
					if k:
						Message.Chat.SendMessage("Sending "+inputt[1]+" random spam messages to "+inputt[0])
						spam(user, times, 1)
					else:
						Message.Chat.SendMessage("Usage: !spam <username> <amount>")
			else:
				Message.Chat.SendMessage("Usage: !spam <username> <amount>")
		if input.startswith("!resolve"):
			input = input.replace("!resolve ", "")
			if input in bl:
				Message.Chat.SendMessage("I'm sorry. That username is blacklisted.")
			else:
				url = "http://api.c99.nl/skyperesolver.php?key=epic321craft123server&username=" + input
				req2 = urllib2.Request(url, headers={ 'User-Agent': 'Mozilla/5.0' })
				info2 = urllib2.urlopen(req2).read()
				Message.Chat.SendMessage (info2)
		if "!commands" == input:
			Message.Chat.SendMessage("Current commands are:")
			Message.Chat.SendMessage("!dox		  | Doxes anything!")
			Message.Chat.SendMessage("!whois		| Will give you all the info possible about a Website.")
			Message.Chat.SendMessage("!resolve	  | Resolve skype username")
			Message.Chat.SendMessage("!geolocation  | Gives you the location and Internet Service Provider of an IP address")
			Message.Chat.SendMessage("!isup		 | Tells you if a website is online")
			Message.Chat.SendMessage("!spam		 | Spam the username with 1000 messages")
			Message.Chat.SendMessage("Accounts:")
			Message.Chat.SendMessage("!netflix	  | Replies with a random netflix account.")
			Message.Chat.SendMessage("!mc		   | Replies with a random minecraft account.")
			Message.Chat.SendMessage("Date and Time:")
			Message.Chat.SendMessage("!time		 | Tells you the current GMT time")
			Message.Chat.SendMessage("!date		 | Tells you the current GMT date")
			Message.Chat.SendMessage("Facts and Jokes:")
			Message.Chat.SendMessage("!fact		 | Tells you a random fact to do with numbers")
			Message.Chat.SendMessage("!cat		  | Tells you a random fact to do with cats")			
			Message.Chat.SendMessage("!chucknorris  | Generates a random Chuck Norris joke")
			Message.Chat.SendMessage("Other fun Things:")
			Message.Chat.SendMessage("!url		  | Shorten a url")
			Message.Chat.SendMessage('!online	   | Replies with "I am online"')
			Message.Chat.SendMessage("#hey		  | Chat with the AI by putting # in front of a message")
		if input.startswith("#"):
			response = '' + k.respond(input)
			print nameb+'> '+response
			Message.Chat.SendMessage(response)
		if input.startswith("!shorten"):
			input = input.replace("!shorten ", "")
			url = "https://los.so/api/?key=ZYJaAgDXhFWxwh6a&url=" + input + "&format=plain"
			req = urllib2.Request(url, headers={ 'User-Agent': 'Mozilla/5.0' })
			url = urllib2.urlopen(req).read()
			Message.Chat.SendMessage(url)
		if input.startswith("!url"):
			input = input.replace("!url ", "")
			url = "https://los.so/api/?key=ZYJaAgDXhFWxwh6a&url=" + input + "&format=plain"
			req = urllib2.Request(url, headers={ 'User-Agent': 'Mozilla/5.0' })
			url = urllib2.urlopen(req).read()
			Message.Chat.SendMessage (url)
		if input.startswith("!isup"):
			input = input.replace("!isup ", "")
			url = "https://zigibot.com/papis/isup.php?key=saibot&url=" + input
			req = urllib2.Request(url, headers={ 'User-Agent': 'Mozilla/5.0' })
			url = urllib2.urlopen(req).read()
			Message.Chat.SendMessage(url)
		if "!time" == input:
			Message.Chat.SendMessage(strftime("The time is: %H:%M:%S", gmtime()))
		if "!date" == input:
			Message.Chat.SendMessage(strftime("The date is: %d/%m/%Y", gmtime()))
		if "!fact" == input:
			url = "http://numbersapi.com/random"
			req = urllib2.Request(url, headers={ 'User-Agent': 'Mozilla/5.0' })
			url = urllib2.urlopen(req).read()
			Message.Chat.SendMessage(url)
		if "!cat" == input:
			url = "http://catfacts-api.appspot.com/api/facts"
			req = urllib2.Request(url, headers={ 'User-Agent': 'Mozilla/5.0' })
			url = urllib2.urlopen(req).read()
			url = url.replace('{"facts": ["', "")
			url = url.replace('"], "success": "true"}', "")
			Message.Chat.SendMessage(url)
		if "!chucknorris" == input:
			url = "http://api.icndb.com/jokes/random"
			req = urllib2.Request(url, headers={ 'User-Agent': 'Mozilla/5.0' })
			url = urllib2.urlopen(req).read()
			data = json.loads(url)
			pprint(data)
			Message.Chat.SendMessage(data['value']['joke'])
		if input.startswith("!whois"):
			input = input.replace("!whois ", "")		
			url = "https://zigibot.com/papis/whois/?key=saibotzz0Ze87Qhad3xVkX34uP&domain=" + input
			req = urllib2.Request(url, headers={ 'User-Agent': 'Mozilla/5.0' })
			info = urllib2.urlopen(req).read()
			Message.Chat.SendMessage ("\n" + info)
		if input.startswith("!dox"):
			input = input.replace("!dox ", "")		
			url = "https://zigibot.com/papis/dox.php?key=saibotqZOc6iSuUQFVbVygAVnR&name=" + input
			req = urllib2.Request(url, headers={ 'User-Agent': 'Mozilla/5.0' })
			info = urllib2.urlopen(req).read()
			Message.Chat.SendMessage ("" + info)
				#if "!mc" == input:
				 #	   url = "http://blitzboot.com/mc/mc.php"
				  #	  req = urllib2.Request(url, headers={ 'User-Agent': 'Mozilla/5.0' })
				   #	 url = urllib2.urlopen(req).read()
					#	url = url.replace("<br><iframe data-aa='45441' src='//ad.a-ads.com/45441?size=200x90' scrolling='no' style='width:200px; height:90px; border:0px; padding:0;overflow:hidden' allowtransparency='true'></iframe>", "")
					 #   Message.Chat.SendMessage(url)
		if input.startswith("!geolocation"):
			input = input.replace("!geolocation ", "")
			url = "http://ip-api.com/line/" + input
			req = urllib2.Request(url, headers={ 'User-Agent': 'Mozilla/5.0' })
			info = urllib2.urlopen(req).read().splitlines()
			##for item in info:
			##	Message.Chat.SendMessage(item)
			if info[0] == "success":
				Message.Chat.SendMessage("Here is the Info for the IP: " + info[13])
				Message.Chat.SendMessage("County: " + info[1])
				if info[4] == "":
					Message.Chat.SendMessage("Country: Not Found")
				else:
					Message.Chat.SendMessage("Country: " + info[4])
				if info[5] == "":
					Message.Chat.SendMessage("City: Not Found")
				else:
					Message.Chat.SendMessage("City: " + info[5])
				if info[10] == "":
					Message.Chat.SendMessage("ISP: Not Found")
				else:
					Message.Chat.SendMessage("ISP: " + info[10])
			else:
				Message.Chat.SendMessage("The details for this IP could not be found.")
	# print out on the shell
		
#while True:
skype.OnMessageStatus = status
skype.OnUserAuthorizationRequestReceived = addcontact
print 'Ready.'
while(True):
	raw_input('')
