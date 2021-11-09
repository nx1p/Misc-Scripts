import time
import datetime
import random
from os import system
import sys
import os.path
import cleverbot
import discord

# note to self: API key has been reset, if ever working with this code again,
# configure code to use a config file and set a .gitignore to not push this config file to public repos
# more info? check out these concise stack overflow answers future me 
# https://stackoverflow.com/questions/44342276/how-to-push-code-to-github-hiding-the-api-keys

#setup
api = "MjUxNjg2Nzc2NDk2ODQ4ODk2.CxnDFQ.7VdTBOniLnEbpuhLGVrm3CNIao8"
client = discord.Client()

print('Setting up')
print('Loading AI')
#Cleverbot
global cb
#Setup Discord connection



@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    global cb
    if message.author == client.user:
        return
    print('{0.author.mention} '.format(message) + message.content)
    msg = message.content
    if msg.startswith('<@251686776496848896> '):
        msg = msg.replace('<@251686776496848896> ', '')
        reply = cb.ask(msg)
        await client.send_message(message.channel, reply)

@client.event
async def on_ready():
    global cb
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print("Setting up AI")
    cb = cleverbot.Cleverbot()
    print('------')


client.run(api)
