import requests
import json
import random
import time
import datetime

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

def History():
    try:
        url = 'https://slack.com/api/channels.history?token=xoxp-8141990049-14705535398-14890407617-81ba12a282&channel=C0845NLR4'
        exit = requests.get(url)
    except:
        exit = 'Failed'
        print('Failed')
    return exit


def Edit(ts, tx):
    chan='C0845NLR4'
    print(ts + '     ....    ' + tx)
    #tx='Knowledge kills'
    url = 'https://slack.com/api/chat.update?token=xoxp-8141990049-14705535398-14890407617-81ba12a282&ts='+ts+'&channel='+chan+'&text='+tx
    #print url
    exit = requests.get(url)


user='U0ELRFRBQ'
history=History().json()
for i in history['messages']:
    try:
        if 'U0ELRFRBQ' in i['user']:
            ts=i['ts']
            Edit(ts, countdown())
    except:
        print('Failed')
