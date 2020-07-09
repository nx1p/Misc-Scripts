import requests
from zalgo import zalgo
import random

def History():
    try:
        url = 'https://slack.com/api/channels.history?token=xoxp-8141990049-14705535398-14890407617-81ba12a282&channel=C0845NLR4'
        exit = requests.get(url)
    except:
        exit = 'Failed'
        print('Failed')
    return exit


def Edit(ts, tx, chan):
    print(ts + '     ....    ' + tx)
    #tx='Knowledge kills'
    INTENSITY = { "up": random.randint(0, 5), "mid": random.randint(0, 5), "down": random.randint(0, 5)}
    tx=zalgo(tx, INTENSITY)
    tok='xoxp-8141990049-14705535398-14890407617-81ba12a282'
    url = 'https://slack.com/api/chat.update?token='+tok+'&ts='+ts+'&channel='+chan+'&text='+tx
    #print url
    exit = requests.get(url)


user='U0ELRFRBQ'
history=History().json()
while True:
	for i in history['messages']:
		try:
			if 'U0ELRFRBQ' in i['user']:
				ts=i['ts']
				Edit(ts, "WE'LL MEET AGAIN", 'C0845NLR4')
		except:
			print('Failed')
