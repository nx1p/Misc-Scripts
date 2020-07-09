import aiml
from os import system
import sys
import commands
import os.path

#setup
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

while(True):
	print 'AI> ' + ai.respond(raw_input('Me> '))