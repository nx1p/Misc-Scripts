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
import requests
from lxml import html
import cleverbot
import thread
from pushbullet import Pushbullet


global GoldAI
GoldAI = False

def Send(msg, to):
    try:
        name = 'Waddles'
        icon = 'http://38.media.tumblr.com%2Favatar_543304f28611_128.png'
        msg = urllib.quote_plus(msg.encode('utf-8'))
        url = 'https://slack.com/api/chat.postMessage?token=xoxb-14889967847-ckoZdS4FZJCpx0R3CmunwyXW&channel=%23'+to+'&text='+msg+'&username='+name+'&icon_url='+icon+'&pretty=1'
        exit = urllib2.urlopen(url).read()
    except:
        exit = 'Failed'
        print 'Failed'
    return exit

def SendUser(msg, to):
    url = 'https://slack.com/api/im.list?token=xoxb-14889967847-ckoZdS4FZJCpx0R3CmunwyXW&pretty=1'
    raw = urllib2.urlopen(url).read()
    users = json.loads(raw)["ims"]
    for n in users:
        if n['user'] == to:
            idd = n['id']
    name = 'Waddles'
    icon = 'http://38.media.tumblr.com%2Favatar_543304f28611_128.png'
    msg = urllib.quote_plus(msg.encode('utf-8'))
    url = 'https://slack.com/api/chat.postMessage?token=xoxb-14889967847-ckoZdS4FZJCpx0R3CmunwyXW&channel=%23'+idd+'&text='+msg+'&username='+name+'&icon_url='+icon+'&pretty=1'
    exit = urllib2.urlopen(url).read()
    return exit

def Send_Clever(msg, to):
    try:
        name = 'CleverBot'
        icon = 'https://pbs.twimg.com/profile_images/3323434294/2d82560aa43e6424a3e0b727bad15650_400x400.jpeg'
        msg = urllib.quote_plus(msg.encode('utf-8'))
        url = 'https://slack.com/api/chat.postMessage?token=xoxb-14889967847-ckoZdS4FZJCpx0R3CmunwyXW&channel=%23'+to+'&text='+msg+'&username='+name+'&icon_url='+icon+'&pretty=1'
        exit = urllib2.urlopen(url).read()
    except:
        exit = 'Failed'
        print 'Failed'
    return exit

def GetSumary(pg):
    page = requests.get(pg)
    tree = html.fromstring(page.content)
    sumer = tree.xpath('//*[@class="userstuff"]')
    summary = sumer[0].text_content()
    return summary

def Shorten(link):
    url = 'http://tinyurl.com/api-create.php?url=' + link
    lin = urllib2.urlopen(url).read()
    return lin

def oink():
    Send('oink', 'tau-main-chat')


def countdown():
    reply = "OH MY, GRAVITY FALLS HAS ENDED, WE WILL MISS YOU GRAVITY FALLS ;-;"
    return reply

def waddles():
    pics = ['http://i.imgur.com/tSWGAQ5.png', 'http://i.imgur.com/whEct4A.png', 'http://i.imgur.com/3qoMK1R.png', 'http://i.imgur.com/iZHpIPZ.png', 'http://i.imgur.com/wLVWExL.png', 'http://i.imgur.com/yuHTJNU.png', 'http://i.imgur.com/wYQmIwj.png', 'http://i.imgur.com/3zqtsUG.png']
    num = random.randint(0, (len(pics)-1))
    link = Shorten(pics[num])
    return link

def fic():
    fics = open('urls.txt').read().splitlines()
    num = random.randint(0, (len(fics)-1))
    randomfic = fics[num].split(' ', 1)
    summary = GetSumary(randomfic[0])
    return ('Here ya go a random TAU fic on Ao3 :D:\n '+randomfic[1]+'\n' + summary  + '\n ' + randomfic[0])

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

def Userlist():
    url = 'https://slack.com/api/users.list?token=xoxp-8141990049-14705535398-14890407617-81ba12a282&pretty=1'
    raw = urllib2.urlopen(url).read()
    users = json.loads(raw)["members"]
    userlist = {}
    for n in users:
        userlist[n['id']] = n['name']
    return userlist

def GoldAIs(ai):
    #Cleverbot
    cb = cleverbot.Cleverbot('my-app')
    Send('--------------- NEW SESSION ---------------', 'bot-shenanigans')
    Send('Hi', 'bot-shenanigans')
    msg = 'Hi'
    while GoldAI:
        #clever
        reply_c = cb.ask(msg)
        Send_Clever(reply_c, 'bot-shenanigans')
        msg = reply_c
        time.sleep(random.uniform(0.01, 1.5))
        #waddles
        reply_waddles = ai.respond(msg)
        Send(reply_waddles, 'bot-shenanigans')
        time.sleep(random.uniform(0.01, 1.5))
        msg = reply_waddles

def UpdateDB(num):
    system("python scrape.py "+num)

#setup
api = 'xoxb-14889967847-ckoZdS4FZJCpx0R3CmunwyXW'
pb_key = 'o.8tkekkkOYX2n8yjp9yBgm3T20UWUd0W9'
print 'Setting up'
print 'Loading AI'

#AI setup
ai_state = False
ai = aiml.Kernel()
#cb = cleverbot.Cleverbot('my-app')
brain="brain.br"
if os.path.isfile(brain):
    ai.bootstrap(brainFile = brain)
else:
    homedir=os.getcwd()
    #Change to the directory whe    re the AIML files are located
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

#Get list of Slack users
print 'Getting list of Slack users'
users = Userlist()

#Setup Pushbullet
print 'Connecting to Pushbullet'
pb = Pushbullet(pb_key)

troll_mode_waddles = False

#Setup Slack connection
print 'Connecting to Slack'
slack = SlackClient(api)
clever = SlackClient("xoxb-100160608497-NRrpka9LXo4zYtaCCdWqN8aU")
clever.rtm_connect()
if slack.rtm_connect():
    print 'Ready'
    while True:
        data = slack.rtm_read()
        if not data == []:
            data = data[0]
            if data['type'] == "message" and "text" in data and not 'username' in data:
                msg = data['text']
                user = users[data["user"]]
                userid = data["user"]
                print msg
                if 'big boss pig' in msg:
                    pic = waddles()
                    Send(pic, 'tau-main-chat')
                elif 'wendip' in msg:
                    pic = fakeWen()
                    Send(pic, 'tau-main-chat')
                elif 'dippyfresh' in msg:
                    pic = dippyfresh()
                    Send(pic, 'tau-main-chat')
                elif 'stan pig' in msg:
                    pic = stan()
                    Send(pic, 'tau-main-chat')
                elif 'oink' in msg:
                    Send(oink(), 'tau-main-chat')
                elif '!dice' in msg:
                    reply = Dice()
                    Send(reply, 'roll-to-rp')
                elif msg.startswith('<@U0ELRFRBQ> '):
                    msg = msg.replace('<@U0ELRFRBQ> ', '')
                    pb.push_note(user+': '+msg, user+': '+msg)
                    Send("Sent sms to Nyx's phone!", 'tau-main-chat')
                if msg.startswith('<@U0ES5UFQX> '):
                    msg = msg.replace('<@U0ES5UFQX> ', '')
                    if (('countdown') or ('next') or ('episode')) in msg:
                        reply = countdown()
                        Send(reply, 'tau-main-chat')
                    elif (('random') or ('fic')) in msg:
                        reply = fic()
                        Send(reply, 'tau-main-chat')
                    elif 'logs' in msg:
                        Send("Here you go, the awesome logs, logged by the amazing moi! :D\n http://logs.mindscape.world/", 'tau-main-chat')
                    if 'troll' in msg:
                        if troll_mode_waddles == False:
                            troll_mode_waddles = True
                            SendUser("ENJOY YOUR TROLLING", userid)
                            print "Enjoy"
                        else:
                            troll_mode_waddles = False
                            SendUser("Awwww...", userid)

                    elif 'gold' in msg:
                        if GoldAI:
                            GoldAI = False
                            Send("The golden AIs have been disabled D:", 'tau-main-chat')
                            Send('--------------- END SESSION ---------------', 'bot-shenanigans')
                        else:
                            GoldAI = True
                            thread.start_new_thread (GoldAIs, (ai, ) )
                            Send("The golden AIs have been enabled :D", 'tau-main-chat')
                    elif 'AI HEADS CHOP' in msg:
                        GoldAI = False
                        Send("THEY HAVE HAD THEIR HEADS CHOPPED OFF, I HOPE YOUR HAPPY ;-;", 'tau-main-chat')
                    elif msg == 'on':
                        ai_state = True
                        Send("Hi, I'm on now :D", 'tau-main-chat')
                    elif msg == 'off':
                        ai_state = False
                        Send("I'm off ;-;", 'tau-main-chat')
                    elif 'update' in msg:
                        try:
                            msg = msg.replace('update ', '')
                            UpdateDB(msg)
                            Send("The database of fics hath been updated (probably) :D", 'tau-main-chat')
                        except:
                            Send("Something went horribly wrong :D", 'tau-main-chat')
                    elif (('dice') or ('roll')) in msg:
                        reply = Dice()
                        Send(reply, 'roll-to-rp')
                    else:
                        if ai_state == True:
                            reply = ai.respond(msg)
                        else:
                            reply = "I'm not turned on atm, use the command 'on' if you want to turn me on :wink: "
                        Send(reply, 'tau-main-chat')
                if msg.startswith('<@U2Y4QHWEM> '):
                    msg = msg.replace('<@U2Y4QHWEM> ', '')
                    Send_Clever(cb.ask(msg), 'tau-main-chat')
                if troll_mode_waddles:
                    reply = ai.respond(msg)
                    Send(reply, 'tau-main-chat')
                print troll_mode_waddles




        time.sleep(1)
