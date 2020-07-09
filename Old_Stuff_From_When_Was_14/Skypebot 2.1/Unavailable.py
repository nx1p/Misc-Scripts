import Skype4Py
import thread

print '========================='
print '    	Skype Auto Reply'
print '========================='
print 'Attaching to Skype'
skype = Skype4Py.Skype()
skype.Attach()


def real(Message):
	time.sleep(1)
	s = 'The person you are trying to reach at the moment is not available. Please try again later.'
	Message.Chat.SendMessage(s)
	print 'Bot> ' + s

def status(Message, Status):
	if Status == 'RECEIVED': 
		print Message.FromHandle + '> ' + Message.Body
		print 'Bot> Hi'
		Message.Chat.SendMessage('Hi')
		thread.start_new_thread(real, (Message))
		
skype.OnMessageStatus = status
print 'Ready to chat'
while(True):
	raw_input('')