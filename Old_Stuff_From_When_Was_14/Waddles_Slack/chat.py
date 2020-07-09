import aiml
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

def Send(msg, to):
    try:
        name = 'Waddles'
        icon = 'http://38.media.tumblr.com%2Favatar_543304f28611_128.png'
        msg = urllib.quote_plus(msg)
        url = 'https://slack.com/api/chat.postMessage?token=xoxb-20578501765-E7WoPujIWlXE5YFtSwaq6dLo&channel=%23'+to+'&text='+msg+'&username='+name+'&icon_url='+icon+'&pretty=1'
        exit = urllib2.urlopen(url).read()
    except:
        exit = 'Failed, trying again'
        print 'Failed, trying again'
    return exit

def Shorten(link):
    url = 'http://tinyurl.com/api-create.php?url=' + link
    lin = urllib2.urlopen(url).read()
    return lin

def oink():
    Send('oink', 'general')


def countdown():
    air_time = datetime.datetime(2015, 11, 24, 8)
    total_sec = (air_time - datetime.datetime.now()).total_seconds()
    sec = int(total_sec % 60)
    mins = int(total_sec / 60 % 60)
    hours = int(total_sec / 60 / 60 % 24)
    day = int(total_sec / 60 / 60 / 24)
    epi_name='Weirdmageddon Part 2'
    formatted = str(day)+' days, '+str(hours)+' hours, '+str(mins)+' minutes, '+str(sec)+' seconds until '+epi_name+'! :D'
    print formatted
    return str(formatted)

def waddles():
    pics = ['http://i.imgur.com/tSWGAQ5.png', 'http://i.imgur.com/whEct4A.png', 'http://i.imgur.com/3qoMK1R.png', 'http://i.imgur.com/iZHpIPZ.png', 'http://i.imgur.com/wLVWExL.png', 'http://i.imgur.com/yuHTJNU.png', 'http://i.imgur.com/wYQmIwj.png', 'http://i.imgur.com/3zqtsUG.png']
    num = random.randint(0, (len(pics)-1))
    link = Shorten(pics[num])
    return link

def fic():
    fics = open('urls.txt').read().splitlines()
    num = random.randint(0, (len(fics)-1))
    return ('Here ya go a random TAU fic on Ao3: '+fics[num]+' :D')

def fakeWen():
    pics = ['http://i.imgur.com/9rKC7Fo.png', 'http://i.imgur.com/KubLjG1.png', 'http://i.imgur.com/r0Q4M8V.png', 'http://i.imgur.com/L1aT1xl.png']
    num = random.randint(0, (len(pics)-1))
    link = Shorten(pics[num])
    return link

def dippyfresh():
    pics = ['http://i.imgur.com/CyqAPod.jpg', 'http://i.imgur.com/hfxQ71c.png', 'http://i.imgur.com/sP0a5Ra.jpg', 'http://i.imgur.com/w8o4xo8.jpg']
    num = random.randint(0, (len(pics)-1))
    link = Shorten(pics[num])
    return link

def stan():
    pics = ['http://i.imgur.com/Rvqi5CB.gif']
    num = random.randint(0, (len(pics)-1))
    link = Shorten(pics[num])
    return link

def Dice():
    ran_num = 'You rolled a ' + urllib2.urlopen('https://www.random.org/integers/?num=1&min=1&max=10&col=1&base=10&format=plain&rnd=new').read()
    return ran_num

#setup
api = 'xoxb-20578501765-E7WoPujIWlXE5YFtSwaq6dLo'
print 'Setting up'
print 'Loading AI'

#AI setup
ai_state = False
ai = aiml.Kernel()
brain="brain.br"
if os.path.isfile(brain):
	ai.bootstrap(brainFile = brain)
else:
	homedir=os.getcwd()
	#Change to the directory whe	re the AIML files are located
	os.chdir('./dic') # going to dictionary
	list=os.listdir('./');
	for item in list: #load dictionary one by one
		ai.learn(item)
	#Change back to homedir to save the brain for subsequent loads
	os.chdir(homedir)
	ai.saveBrain(brain) # save new brain
# name of bot
nameb = 'Waddles'
ai.setBotPredicate('name', nameb)
ai.setBotPredicate('master', 'Mabel')
ai.setBotPredicate('email', 'NyxTheDarkness@riseup.net')
ai.setBotPredicate('gender', 'Nyx')
ai.setBotPredicate('state', 'OR')
ai.setBotPredicate('city', 'Gravity Falls')
ai.setBotPredicate('domain', 'Pig')
ai.setBotPredicate('job', 'being a pig')
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
                if 'big boss pig' in msg:
                    pic = waddles()
                    Send(pic, 'general')
                if 'wendip' in msg:
                    pic = fakeWen()
                    Send(pic, 'spoilery-chat')
                if 'dippyfresh' in msg:
                    pic = dippyfresh()
                    Send(pic, 'spoilery-chat')
                if 'stan waddles pic' in msg:
                    pic = stan()
                    Send(pic, 'general')
                if 'oink' in msg:
                    Send(oink(), 'general')
                if '!dice' in msg:
                    reply = Dice()
                    Send(reply, 'roll-to-rp')
                if msg.startswith('<@U0LH0ERNH>: '):
                    msg = msg.replace('<@U0ES5UFQX>: ', '')
                    if (('countdown') or ('next') or ('episode')) in msg:
                        reply = countdown()
                        Send(reply, 'general')
                    elif (('random') or ('fic')) in msg:
                        reply = fic()
                        Send(reply, 'general')
                    elif msg == 'on':
                        ai_state = True
                        Send("Hi, I'm on now :D", 'general')
                    elif msg == 'off':
                        ai_state = False
                        Send("I'm off ;-;", 'general')
                    elif (('dice') or ('roll')) in msg:
                        reply = Dice()
                        Send(reply, 'general')
                    else:
                        if ai_state == True:
                            reply = ai.respond(msg)
                        else:
                            reply = "I'm not turned on atm, use the command 'on' if you want to turn me on :wink: "
                        Send(reply, 'general')




        time.sleep(1)
