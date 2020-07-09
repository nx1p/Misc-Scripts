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
def whois(site):	
	url = "https://zigibot.com/papis/whois/?key=saibotzz0Ze87Qhad3xVkX34uP&domain=" + site
	req = urllib2.Request(url, headers={ 'User-Agent': 'Mozilla/5.0' })
	return urllib2.urlopen(req).read()
	
msg = RetrieveMessage()
if CheckIfMessageExists(msg):
	print whois(msg) 
else:
	print 'Usage: !whois <site/ip>'