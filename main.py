import discord
from datetime import datetime, timedelta

TOKEN = 'Nzc5MzU5MjQwNTg5NjcyNDY4.X7fY2g.NG9RvJTyfIdkDx46bXGjR4N-5cY'
#SERVER = 'BotTestingGround'
SERVER = 'NITRO BOOSTED COMMUNE'

client = discord.Client()
global lastCooldownDate
lastCooldownDate = datetime(2000, 1, 1)
global msgCount
global currentTime
global firstMsgDate
firstMsgDate = datetime(2000, 1, 1)

@client.event
async def on_ready():
    for server in client.guilds:
        if server.name == SERVER:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{server.name}(id: {server.id})'
    )
    global msgCount
    msgCount = 0


@client.event
async def on_message(message):
    global msgCount
    global lastCooldownDate
    global currentTime
    global firstMsgDate
    if message.author == client.user:
        return

    if ((message.channel.name == 'bot-feature-requests') or (message.channel.name == 'dj-booth')):
        return

    if 'cringe' in message.content.lower():
        currentTime = datetime.now()
        if (lastCooldownDate + timedelta(minutes=5) >= currentTime):
            return
        if (msgCount == 0):
            firstMsgDate = datetime.now()
        if((msgCount == 5) & (firstMsgDate + timedelta(minutes=5) >= currentTime)):
            lastCooldownDate = datetime.now()
            msgCount = 0
            return
        if((msgCount == 5) & (firstMsgDate + timedelta(minutes=5) <= currentTime)):
            msgCount = 0
        msgCount = msgCount + 1
        await message.channel.send('epic')

    if 'pog' in message.content.lower():
        currentTime = datetime.now()
        if (lastCooldownDate + timedelta(minutes=5) >= currentTime):
            return
        if (msgCount == 0):
            firstMsgDate = datetime.now()
        if ((msgCount == 5) & (firstMsgDate + timedelta(minutes=5) >= currentTime)):
            lastCooldownDate = datetime.now()
            msgCount = 0
            return
        if ((msgCount == 5) & (firstMsgDate + timedelta(minutes=5) <= currentTime)):
            msgCount = 0
        msgCount = msgCount + 1
        await message.channel.send('Please do not use racist messaging.')



client.run(TOKEN)
