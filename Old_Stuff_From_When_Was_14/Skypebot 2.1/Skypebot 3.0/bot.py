#Skype Bot 3.0
#By Savant

import Skype4Py
import time
import os
import sys
import aiml
from time import gmtime, strftime
from subprocess import Popen,PIPE,STDOUT,call
global ai
global skype

#Setup functions
def setup():
	print 'Attaching to Skype'
	setupSkype()
	print 'Setting up AI'
	ReadConfig()
	sys.stdout = open(os.devnull, "w")
	setupAI()
	sys.stdout = sys.__stdout__
	os.chdir('../')
	print 'Ready!'
def setupSkype():
	global skype
	skype = Skype4Py.Skype()
	skype.Attach()
	skype.OnMessageStatus = MessageProcessing
def setupAI():
	global ai
	ai = aiml.Kernel()
	brain="brain.br"
	os.chdir('modules/storage')
	if os.path.isfile(brain):
		ai.bootstrap(brainFile = brain)
	else:
		homedir=os.getcwd()
		os.chdir('./AIData') 
		list=os.listdir('./');
		for item in list:
			ai.learn(item)
		os.chdir(homedir)
	ai.saveBrain(brain)
	ai.setBotPredicate('name', BotName)
	ai.setBotPredicate('master', "Savant")
def ReadConfig():
	global BotName
	BotName = open('config/BotName.txt').read()
	global ConfigLog
	ConfigLog = bool(open('config/Log.txt').read().splitlines()[0])


#Send Function
def SendMessage(msg, Message):
	global BotName
	Log(BotName + '> ' + msg)
	Message.Chat.SendMessage(msg)

#Logging Function
def Log(msg):
	print msg
	if Log:
		with open("storage/log.txt", "a") as text_file:
			text_file.write(strftime("[%H:%M:%S] ", gmtime()) + msg + '\n')

#Processing Functions
def CheckIfInListOfModules(msg, modules):
	if msg in modules:
		return True
	else:
		return False
def GetListOfModulesAndCleanUpFileExtenstions():
	UncleanModules = [ f for f in os.listdir(os.curdir) if os.path.isfile(os.path.join(os.curdir,f)) ]
	for x in xrange(0,len(UncleanModules)):
		y = x - 1
		UncleanModules[y] = UncleanModules[y].split('.')[0]
	CleanModules = UncleanModules
	return CleanModules
def GetListOfModulesAndDontCleanUpFileExtenstions():
	UncleanModules = [ f for f in os.listdir(os.curdir) if os.path.isfile(os.path.join(os.curdir,f)) ]
	return UncleanModules
def ProcessAndLoadModule(fullModList, modules, file, msg, user):
	orginialMsg = msg
	msg = msg.replace(file[0] + ' ', '')
	if msg == orginialMsg:
		command = fullModList[modules.index(file[0])] + ' ""' + ' "' + user + '"'
	elif not msg == orginialMsg:
		command = fullModList[modules.index(file[0])] + ' "' + msg + '" "' + user + '"'
	process = Popen(command, shell=True, stdout=PIPE, )
	return process.communicate()[0]
	

	
	
	
#Main Processing Function
def MessageProcessing(Message, Status):
	global AI
	if Status == 'RECEIVED': 
		msg = Message.Body
		sender = Message.FromHandle
		Log(sender + '> ' + msg)
		if msg.startswith('#'): #Because of how long it takes to load the AI and a couple of other reasons the AI command has to be hard coded in
			SendMessage(ai.respond(msg.replace('#', '')), Message)
		else:
			file = msg.split()
			modules = GetListOfModulesAndCleanUpFileExtenstions()
			fullModList = GetListOfModulesAndDontCleanUpFileExtenstions()
			if CheckIfInListOfModules(file[0], modules):
				SendMessage(ProcessAndLoadModule(fullModList, modules, file, msg, sender), Message)





print '================='
print '  Skype Bot 3.0'
print '    By Savant'
print '================='
time.sleep(1.6)
setup()

while(True):
	raw_input('')