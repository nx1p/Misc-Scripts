import urllib2
import urllib
from slackclient import SlackClient
import time
import json
import datetime
import random
from os import system
import sys
import commands
import os.path
import cleverbot

def Send(msg, to):
    try:
        name = 'CleverBot'
        icon = 'https://pbs.twimg.com/profile_images/3323434294/2d82560aa43e6424a3e0b727bad15650_400x400.jpeg'
        msg = urllib.quote_plus(msg)
        url = 'https://slack.com/api/chat.postMessage?token=xoxb-14889967847-ckoZdS4FZJCpx0R3CmunwyXW&channel=%23'+to+'&text='+msg+'&username='+name+'&icon_url='+icon+'&pretty=1'
        exit = urllib2.urlopen(url).read()
    except:
        exit = 'Failed, trying again'
        print 'Failed, trying again'
    return exit

#setup
api = "xoxb-100160608497-NRrpka9LXo4zYtaCCdWqN8aU"
print 'Setting up'
print 'Loading AI'
#Cleverbot
cb = cleverbot.Cleverbot()
#Setup Slack connection
slack = SlackClient(api)


print 'Connecting to Slack'
if slack.rtm_connect():
    print 'Ready'
    while True:
        data = slack.rtm_read()
        if not data == []:
            data = data[0]
            if data['type'] == "message" and "text" in data and not 'username' in data:
                msg = data['text']
                print msg
                reply = cb.ask(msg)
                print 'Bot > ' + reply
                Send(reply, 'tau-main-chat')
        time.sleep(0.1)
