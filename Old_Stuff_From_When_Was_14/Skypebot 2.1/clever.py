import Skype4Py
import cleverbot
import random
import time
import thread
print '========================='
print '      Skype AI Bot'
print '========================='
print 'Setting up AI'
bot = cleverbot.Cleverbot()
print 'Attaching to Skype'
skype = Skype4Py.Skype()
skype.Attach()

def real(bot, Message):
	time.sleep(1)
	s = bot.ask(Message.Body)
	Message.Chat.SendMessage(s)
	print 'Bot> ' + s
def status(Message, Status):
	ignore = open('ignore.txt').read().splitlines()
	if not Message.FromHandle in ignore:
		if Status == 'RECEIVED': 
			print Message.FromHandle + '> ' + Message.Body
			s = bot.ask(Message.Body)
			print 'Bot> ' + s
			Message.Chat.SendMessage(s)
			n = random.randint(1, 10)
			if n < 4:
				thread.start_new_thread(real, (bot, Message))
				
skype.OnMessageStatus = status
print 'Ready to chat'
while(True):
	raw_input('')