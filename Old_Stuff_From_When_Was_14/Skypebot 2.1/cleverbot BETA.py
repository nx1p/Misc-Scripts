import Skype4Py
from chatterbotapi import ChatterBotFactory, ChatterBotType

factory = ChatterBotFactory()
bot1 = factory.create(ChatterBotType.CLEVERBOT)
bot1session = bot1.create_session()
skype = Skype4Py.Skype()
skype.Attach()

def status(Message, Status):
	ignore = open('ignore.txt').read().splitlines()
	if not Message.FromHandle in ignore:
		print Message.FromHandle + '> ' + Message.Body
		s = bot1session.think(Message.Body)
		print 'Bot> ' + s.upper()
		Message.Chat.SendMessage(s.upper())
skype.OnMessageStatus = status
print 'Ready.'
while(True):
	raw_input('')