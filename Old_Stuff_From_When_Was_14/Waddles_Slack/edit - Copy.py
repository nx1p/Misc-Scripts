import requests
import json
import random
from zalgo import zalgo

def Edit(ts, tx, chan):
    print(ts + '     ....    ' + tx)
    #tx='Knowledge kills'
    INTENSITY = { "up": 5, "mid": 0, "down": 5}
    tx=zalgo(tx, INTENSITY)
    tok='xoxp-8141990049-14705535398-14890407617-81ba12a282'
    url = 'https://slack.com/api/chat.update?token='+tok+'&ts='+ts+'&channel='+chan+'&text='+tx
    #print url
    exit = requests.get(url)

#tau = C0845NLR4
#kate= D0F8H8TPZ
#rayland = D0HL3M5NF
ts='1478367405.006056'

while(True):
     ran = random.randint(0, 10000)
     Edit(ts, str(ran), 'C0845NLR4')
