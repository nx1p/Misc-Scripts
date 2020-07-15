#!/bin/python3

########################################
#                                      #
#       Khaos_Sys Reminder Script      #
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-  #
#                                      #
# Author: Cryptid&Electra Khaos        #
# Created: 09/07/2020                  #
# Last update: 09/07/2020              #
# Version: v0.2                        #
# Time worked on: ~5.0 hours           #
#                                      #
########################################
## TO-DO
# [X] Ask for confirmation to start up
# [X] Edit the confirmation message to show how long until time out
#     - Time taken: (1h 12m)
# [ ] Do the whole actual reminders stuff, sending X message after X time and all
#     [X] Make function to do basic morning reminders (Time: 40m)

import discord
import asyncio
import time

# Define Constants(-ish?)
# Is CLIENT a constant?
CLIENT = discord.Client()
REMINDER_ID = 730746502112084008
BOT_PROMPT = "**\>**"


# Example usage: log("Booting up")
# Use to output infomation to STDOUT adds on a > for style
def log(msg):
    print(f"  > {msg}")


# define function to edit the message for timeout
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
    prompt = "**Reminder\>**"
    reminders = (f'{BOT_PROMPT} Morning Reminders..\n'
                 f'{prompt} Charge SmartWatch\n'
                 f'{prompt} Use mouthwash and/or brush teeth'
                 f'{prompt} Skim google Calander'
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
        if(str(reaction.emoji) == '✅'):
            log("system will init now")
            await channel.send(f'{BOT_PROMPT} reminder system booting up now')
        elif(str(reaction.emoji) == '❌'):
            log("system should not init, closing")
            await channel.send(f'{BOT_PROMPT} reminder system shutting down now')
            await client.close()
    finally:
        edit_timeout_task.cancel()


@CLIENT.event
async def on_ready():
    log('We have logged in as {0.user}'.format(CLIENT))
    await sys_init(CLIENT)
    await morning_reminders(CLIENT)


@CLIENT.event
async def on_message(message):
    if message.author == CLIENT.user:
        return


def setup():
    CLIENT.run('NzMwNzQ0MjU5Mjc1MzkxMDM3.Xwb9Fg.qFbmnyjr6iF7OlV2O7s54UXS0WY')

if __name__ == "__main__":
    setup()
