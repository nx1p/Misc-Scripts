import Skype4Py

skype = Skype4Py.Skype()
skype.Attach()

def status(Message, Status):
	print Message.FromHandle + '> ' + Message.Body
skype.OnMessageStatus = status
print 'Ready.'
while(True):
	raw_input('')