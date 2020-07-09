import Skype4Py

skype = Skype4Py.Skype()
skype.Attach()

def status(Message, Status):
	ignore = open('ignore.txt').read().splitlines()
	if not Message.FromHandle in ignore:
		if Status == 'RECEIVED': 
			print Message.FromHandle + '> ' + Message.Body
			print 'Bot> Yeah'
			Message.Chat.SendMessage('Yeah')
skype.OnMessageStatus = status
print 'Ready.'
while(True):
	raw_input('')