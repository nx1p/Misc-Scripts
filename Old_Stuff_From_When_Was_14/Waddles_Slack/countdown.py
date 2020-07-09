import requests
import json
import random
import time
import datetime


def Edit(ts, tx, chan):
    print(ts + '	....    ' + tx)
    tok='xoxp-8141990049-14705535398-14890407617-81ba12a282'
    url = 'https://slack.com/api/chat.update?token='+tok+'&ts='+ts+'&channel='+chan+'&text='+tx
    #print url
    exit = requests.get(url)
	
def countdown():
    air_time = datetime.datetime(2016, 2, 15, 8)
    total_sec = (air_time - datetime.datetime.now()).total_seconds()
    sec = int(total_sec % 60)
    mins = int(total_sec / 60 % 60)
    hours = int(total_sec / 60 / 60 % 24)
    day = int(total_sec / 60 / 60 / 24)
    epi_name='Take Back the Falls'
    formatted = str(day)+' days, '+str(hours)+' hours, '+str(mins)+' minutes, '+str(sec)+' seconds until '+epi_name+'! D:'
    return str(formatted)



#tau = C0845NLR4
#kate= D0F8H8TPZ
#rayland = D0HL3M5NF
ts='1455086359.005991'
x = 0

while(True):
	Edit(ts, countdown(), 'C0845NLR4')