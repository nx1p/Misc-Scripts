import sys
import urllib2

def LoadBlackList():
	return open('storage/blacklist.txt').read().splitlines()
def CheckBlackList(sender):
	if not sender in blacklist:
		return True
	else:
		return False
def RetrieveMessage():
	try:
		return sys.argv[1]
	except:
		return ''
def RetrieveSender():
	try:
		return sys.argv[2]
	except:
		return ''
def CheckIfMessageExists(msg):
	if not msg == '':
		return True
	else:
		return False
def resolve(name):
	url = "http://api.predator.wtf/resolver/?arguments=" + name
	req = urllib2.Request(url, headers={ 'User-Agent': 'Mozilla/5.0' })
	return urllib2.urlopen(req).read()
	
blacklist = LoadBlackList()
msg = RetrieveMessage()
sender = RetrieveSender()
if CheckIfMessageExists(msg):
	if CheckBlackList(msg):
		print resolve(msg) 
	else:
		print 'Sorry that user is blacklisted, please try a different person.'
else:
	print 'Usage: !resolve <username>'