import sys
import urllib2

def RetrieveMessage():
	try:
		return sys.argv[1]
	except:
		return ''
def CheckIfMessageExists(msg):
	if not msg == '':
		return True
	else:
		return False
def dox(name):
	url = "https://zigibot.com/papis/dox.php?key=saibotqZOc6iSuUQFVbVygAVnR&name=" + name
	req = urllib2.Request(url, headers={ 'User-Agent': 'Mozilla/5.0' })
	return urllib2.urlopen(req).read()
	
msg = RetrieveMessage()
if CheckIfMessageExists(msg):
	print dox(msg) 
else:
	print 'Usage: !dox <username/email>'