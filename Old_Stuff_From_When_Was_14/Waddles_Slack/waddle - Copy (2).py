import aiml
import urllib2
import urllib
from slackclient import SlackClient
import time
import json
import datetime
import random
from os import system
import sys
import commands
import os.path
import cleverbot

def Send(msg, to):
	try:
		name = 'Waddles'
		icon = 'http://38.media.tumblr.com%2Favatar_543304f28611_128.png'
		msg = urllib.quote_plus(msg)
		url = 'https://slack.com/api/chat.postMessage?token=xoxb-14889967847-ckoZdS4FZJCpx0R3CmunwyXW&channel=%23'+to+'&text='+msg+'&username='+name+'&icon_url='+icon+'&pretty=1'
		exit = urllib2.urlopen(url).read()
	except:
		exit = 'Failed, trying again'
		print 'Failed, trying again'
	return exit
	
def Send_Clever(msg, to):
	try:
		name = 'CleverBot'
		icon = 'https://pbs.twimg.com/profile_images/3323434294/2d82560aa43e6424a3e0b727bad15650_400x400.jpeg'
		msg = urllib.quote_plus(msg)
		url = 'https://slack.com/api/chat.postMessage?token=xoxb-14889967847-ckoZdS4FZJCpx0R3CmunwyXW&channel=%23'+to+'&text='+msg+'&username='+name+'&icon_url='+icon+'&pretty=1'
		exit = urllib2.urlopen(url).read()
	except:
		exit = 'Failed, trying again'
		print 'Failed, trying again'
	return exit

#setup
api = 'xoxp-8141990049-14705535398-14890407617-81ba12a282'
print 'Setting up'
print 'Loading AI'
#AI setup
ai_state = False
ai = aiml.Kernel()
brain="brain.br"
if os.path.isfile(brain):
	ai.bootstrap(brainFile = brain)
else:
	homedir=os.getcwd()
	#Change to the directory whe	re the AIML files are located
	os.chdir('./dic') # going to dictionary
	list=os.listdir('./');
	for item in list: #load dictionary one by one
		ai.learn(item)
	#Change back to homedir to save the brain for subsequent loads
	os.chdir(homedir)
	ai.saveBrain(brain) # save new brain
# name of bot
nameb = 'Waddles'
ai.setBotPredicate('name', nameb)
ai.setBotPredicate('master', 'Mabel')
ai.setBotPredicate('email', 'NyxTheDarkness@riseup.net')
ai.setBotPredicate('gender', 'Nyx')
ai.setBotPredicate('state', 'OR')
ai.setBotPredicate('city', 'Gravity Falls')
ai.setBotPredicate('domain', 'Pig')
ai.setBotPredicate('job', 'being a pig')
#Cleverbot
cb = cleverbot.Cleverbot()
#Setup Slack connection
slack = SlackClient(api)


print 'Connecting to Slack'
if slack.rtm_connect():
	print 'Ready'
	Send('Hi', 'bot-shenanigans')
	print 'Bot> Hi'
	msg = 'Hi'
	while True:
		#clever
		reply_c = cb.ask(msg)
		print 'CleverBot > ' + reply_c
		Send_Clever(reply_c, 'bot-shenanigans')
		msg = reply_c
		time.sleep(random.uniform(0.01, 1.5))
		#waddles
		reply_waddles = ai.respond(msg)
		print 'Waddles > ' + reply_waddles
		Send(reply_waddles, 'bot-shenanigans')
		time.sleep(random.uniform(0.01, 1.5))
		msg = reply_waddles
