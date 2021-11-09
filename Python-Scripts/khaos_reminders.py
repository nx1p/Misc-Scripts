#!/bin/python3

########################################
#                                      #
#       Khaos_Sys Reminder Script      #
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-  #
#                                      #
# Author: Cryptid&Electra Khaos        #
# Created: 09/07/2020                  #
# Last update: 20/07/2020              #
# Version: v0.5                        #
# Time worked on: ~7.5 hours           #
#                                      #
########################################
## TO-DO
# [X] Ask for confirmation to start up
# [X] Edit the confirmation message to show how long until time out
#     - Time taken: (1h 12m)
# [ ] Do the whole actual reminders stuff, sending X message after X time and all
#     [X] Make function to do basic morning reminders (Time: 40m)
#     [ ] Make function to remind take Estrogen every 5 hours
#     [ ] Make function ask if want regular caffeine reminders?
# [X] Framework for writing commands and a command to shut bot down (Time taken: 50m)
# [X] Code a way for the script to interact with Node-Red (Async TCP?) (Time taken: ~30m)
#     [X] Ask for confirmation to shutdown when sleep tracking starts
# [X] Bot double checks only one instance is running on start up (Time: ~30m)

## Bugs
# - When the "sleep-tracking-start" tcp command is sent it triggers the unknown handler command
#   But also runs the sleep tracking start function too? So it works but it shouldn't be saying
#   That the command's unknown?
#   Same logic/code that works for the discord command handler and that doesn't have that problem?



# note to self: API key has been reset, if ever working with this code again,
# configure code to use a config file and set a .gitignore to not push this config file to public repos
# more info? check out these concise stack overflow answers future me 
# https://stackoverflow.com/questions/44342276/how-to-push-code-to-github-hiding-the-api-keys

#Standard imports
import asyncio
import os
import time

#Non-standard imports
import discord
import psutil

# Define Constants(-ish?)
# Is CLIENT a constant?
CLIENT = discord.Client()
REMINDER_ID = 730746502112084008
BOT_PROMPT = "**\\>**"
COMMAND_PREFIX = "kb;"
TOKEN = 'NzMwNzQ0MjU5Mjc1MzkxMDM3.Xwb9Fg.qFbmnyjr6iF7OlV2O7s54UXS0WY'

# Function taken from https://stackoverflow.com/questions/788411/check-to-see-if-python-script-is-running
# Tested to run on Mac OS, will probably need modification to run on Linux
def is_running(script):
    for q in psutil.process_iter():
        if q.name().startswith('Python'):
            if len(q.cmdline())>1 and script in q.cmdline()[1] and q.pid !=os.getpid():
                print("'{}' Process is already running".format(script))
                return True

    return False


#Function to be called to turn off the bot
async def shutdown_bot(client, msg):
    channel = client.get_channel(REMINDER_ID)
    await channel.send(f'{BOT_PROMPT} Shutdown command recieved, shutting down now')
    await client.close()


#Default function if a command is unknown
async def unknown_command(client, msg):
    channel = client.get_channel(REMINDER_ID)
    await channel.send(f'{BOT_PROMPT} ERROR: Unknown request \"{msg}\"')

#Default function if a tcp command is unknown
async def unknown_tcp_msg(client, message, writer):
    channel = client.get_channel(REMINDER_ID)
    await channel.send(f'{BOT_PROMPT} WARNING: Received Unknown TCP command \"{message}\"')
    return

#Ask confirmation to shutdown
async def ask_confirmation_shutdown(client, message, writer):
    channel = client.get_channel(REMINDER_ID)
    await channel.send(f'{BOT_PROMPT} WARNING: Received Unknown TCP command \"{message}\"')

    log("Asking if system should shutdown")
    msg = await channel.send((f'{BOT_PROMPT} sleep tracking started?\n'
                              f'{BOT_PROMPT} system shutdown? (✅/❌)\n'))
    timeout_msg = await channel.send(f'{BOT_PROMPT} timeout in 01H:00M:00S\n')

    await msg.add_reaction("✅")
    await msg.add_reaction("❌")


    # define function to wait for reaction reply
    def check(reaction, user):
        return user != CLIENT.user and (str(reaction.emoji) == '✅' or str(reaction.emoji) == '❌')

    edit_timeout_task = asyncio.create_task(edit_timeout(timeout_msg, time.perf_counter()))


    # wait for a reaction reply and then act according on the reply or lack of
    try:
        reaction, user = await client.wait_for('reaction_add', timeout=3600.0, check=check)
    except asyncio.timeouterror:
        await channel.send(f'{BOT_PROMPT} timed out, not shutting down')
        log("shutdown question timed out")
        return
    else:
        if str(reaction.emoji) == '✅':
            log("system will shutdown now")
            await channel.send(f'{BOT_PROMPT} reminder system shutting down now')
            await client.close()
        elif str(reaction.emoji) == '❌':
            log("system should not shutdown")
            await channel.send(f'{BOT_PROMPT} reminder system staying up')
    finally:
        edit_timeout_task.cancel()


    return

#Dictionary that maps the string of command names to functions
COMMANDS_DICT = {'shutdown': shutdown_bot}

#Dictionary that maps the string of tcp commands to functions
TCP_COMMANDS_DICT = {'sleep-tracking-start': ask_confirmation_shutdown}

# Example usage: log("Booting up")
# Use to output infomation to STDOUT adds on a > for style
def log(msg):
    print(f"  > {msg}")


# Edits the init message to give a timeout countdown
async def edit_timeout(msg, start_timestamp):
    await asyncio.sleep(10)
    new_timeout = time.strftime('%HH:%MM:%SS',
                                time.gmtime(3600 - (time.perf_counter()
                                                    - start_timestamp)))
    await msg.edit(content=(f'{BOT_PROMPT} system init? (✅/❌)\n'
                            f'{BOT_PROMPT} timeout in {new_timeout}\n'))
    await edit_timeout(msg, start_timestamp)


# Morning Reminders
async def morning_reminders(client):
    channel = client.get_channel(REMINDER_ID)
    prompt = "**Reminder\\>**"
    reminders = (f'{BOT_PROMPT} Morning Reminders..\n'
                 f'{prompt} Charge SmartWatch\n'
                 f'{prompt} Use mouthwash and/or brush teeth\n'
                 f'{prompt} Skim google Calander\n'
                 f'{prompt} Eat Breakfast\n')
    await channel.send(reminders)


# Request confirmation from Khaos to Init
async def sys_init(client):
    channel = client.get_channel(REMINDER_ID)

    log("Asking if system should init")
    msg = await channel.send((f'{BOT_PROMPT} system init? (✅/❌)\n'
                              f'{BOT_PROMPT} timeout in 01H:00M:00S\n'))

    await msg.add_reaction("✅")
    await msg.add_reaction("❌")


    # define function to wait for reaction reply
    def check(reaction, user):
        return user != CLIENT.user and (str(reaction.emoji) == '✅' or str(reaction.emoji) == '❌')

    edit_timeout_task = asyncio.create_task(edit_timeout(msg, time.perf_counter()))


    # wait for a reaction reply and then act according on the reply or lack of
    try:
        reaction, user = await client.wait_for('reaction_add', timeout=3600.0, check=check)
    except asyncio.timeouterror:
        await channel.send(f'{BOT_PROMPT} timed out, shutting down')
        log("init question timed out")
        await client.close()
    else:
        if str(reaction.emoji) == '✅':
            log("system will init now")
            await channel.send(f'{BOT_PROMPT} reminder system booting up now')
        elif str(reaction.emoji) == '❌':
            log("system should not init, closing")
            await channel.send(f'{BOT_PROMPT} reminder system shutting down now')
            await client.close()
    finally:
        edit_timeout_task.cancel()


async def handle_tcp_message(reader, writer):
    data = await reader.read(100)
    message = data.decode()
    addr = writer.get_extra_info('peername')

    log(f"Received {message!r} from {addr!r}")
    handler_function = TCP_COMMANDS_DICT.get(str(message), unknown_tcp_msg)
    await handler_function(CLIENT, message, writer)

    #print(f"Send: {message!r}")
    #writer.write(data)
    #await writer.drain()

    print("Close the connection")
    writer.close()

@CLIENT.event
async def on_ready():
    log('We have logged in as {0.user}'.format(CLIENT))
    await sys_init(CLIENT)
    await morning_reminders(CLIENT)
    server = await asyncio.start_server(
        handle_tcp_message, '127.0.0.1', 1337)
    asyncio.create_task(server.serve_forever())



@CLIENT.event
async def on_message(message):
    if message.author == CLIENT.user:
        return
    if message.content.startswith(COMMAND_PREFIX):
        msg = message.content.replace(COMMAND_PREFIX, "", 1)
        command = msg.split(" ", 1)[0]
        command_function = COMMANDS_DICT.get(command, unknown_command)
        await command_function(CLIENT, msg)


def setup():
    CLIENT.run(TOKEN)

if __name__ == "__main__":
    if not is_running("khaos_reminders.py"):
        setup()
