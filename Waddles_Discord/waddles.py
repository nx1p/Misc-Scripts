import discord
from urllib.request import urlopen
import time
import random
import aiml
from os import system
import sys
import os.path
from lxml import html
import requests
from scrape import UpdateDatabase

global ai
client = discord.Client()

def Dice(minn, maxx):
    print(minn)
    print(maxx)
    print(str(random.randint(int(minn), int(maxx))))
    ran_num = "You rolled a "+str(random.randint(int(minn), int(maxx)))
    return ran_num
def Shorten(link):
    url = 'http://tinyurl.com/api-create.php?url=' + link
    lin = urlopen(url).read().decode('utf-8')
    return lin

def waddles():
    pics = ['http://i.imgur.com/tSWGAQ5.png', 'http://i.imgur.com/whEct4A.png', 'http://i.imgur.com/3qoMK1R.png', 'http://i.imgur.com/iZHpIPZ.png', 'http://i.imgur.com/wLVWExL.png', 'http://i.imgur.com/yuHTJNU.png', 'http://i.imgur.com/wYQmIwj.png', 'http://i.imgur.com/3zqtsUG.png']
    num = random.randint(0, (len(pics)-1))
    link = Shorten(pics[num])
    return link

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
    link = pics[num]
    return link

def fic():
    fics = open('urls.txt').read().splitlines()
    num = random.randint(0, (len(fics)-1))
    randomfic = fics[num].split(' ', 1)
    summary = GetSumary(randomfic[0])
    return (':two_hearts: :black_heart:     _Here_ ya go, a **random** __TAU tagged fic__ on _Ao3_     :black_heart: :two_hearts:```'+randomfic[1]+'```' + summary  + '```md\n#Link```' + randomfic[0])

def GetSumary(pg):
    page = urlopen(pg).read().decode('utf-8')
    tree = html.fromstring(page)
    sumer = tree.xpath('//*[@class="userstuff"]')
    print(pg)
    summary = sumer[0].text_content()
    return summary

def UpdateDB():
    UpdateDatabase()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    global ai
    if message.author == client.user:
        return
    print('{0.author.mention} '.format(message) + message.content)
    msg = message.content
    if 'big boss pig' in msg:
        pic = waddles()
        await client.send_message(message.channel, pic)
    elif 'wendip' in msg:
        pic = fakeWen()
        await client.send_message(message.channel, pic)
    elif 'dippyfresh' in msg:
        pic = dippyfresh()
        await client.send_message(message.channel, pic)
    elif 'stan with waddles' in msg:
        pic = stan()
        await client.send_message(message.channel, pic)
    elif 'oink' in msg:
        await client.send_message(message.channel, 'oink')
    if msg.startswith('<@232785888654917634> '):
        msg = msg.replace('<@232785888654917634> ', '')
        if (('random') or ('fic')) in msg:
            reply = fic()
            await client.send_message(message.channel, reply)
        elif 'update' in msg:
            try:
                msg = msg.replace('update ', '')
                await UpdateDB()
                await client.send_message(message.channel, "The database of fics has been updated (probably) :D")
            except:
                await client.send_message(message.channel, "Something went horribly wrong :D")
        elif msg.startswith('dice '):
            try:
                print("thing: "+msg)
                nums = msg.replace('dice ', '').split(' ')
                print("thing2: "+message.content.replace('dice ', ''))
                msg = Dice(nums[0], nums[1])
            except:
                msg = "Whoops, I failed to recognize that, try again..?"
            await client.send_message(message.channel, msg)
        else:
            reply = ai.respond(msg)
            await client.send_message(message.channel, reply)

@client.event
async def on_ready():
    global ai
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print("Setting up AI")
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
    ai.setBotPredicate('botmaster', 'Mabel')
    ai.setBotPredicate('email', 'NyxTheDarkness@riseup.net')
    ai.setBotPredicate('gender', 'Pig')
    ai.setBotPredicate('state', 'OR')
    ai.setBotPredicate('city', 'Gravity Falls')
    ai.setBotPredicate('domain', 'Pig')
    ai.setBotPredicate('job', 'being a pig')

    print('------')

client.run("MjMyNzg1ODg4NjU0OTE3NjM0.CtT-kw.Mb64uBquYixNnaaQgcVNzO3YiSM")
