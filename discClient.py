import discord
from config import *
from yt import *
import time
client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    channel = client.get_channel(BOTCHANNEL)
    await channel.send('Kikkeriki!!')
    while(1):
        for i in HOLOIDS:
            info = returnResp(i[0])
            live = query(info)
            if(live):
                videoID = findVideoID(info)
                await channel.send(
                 '@everyone'
                 + '`' + i[1] + ' is live!\n`'
                 + 'https://www.youtube.com/watch?v=' + str(videoID))
        time.sleep(60)


def query(info):
    live = isLive(info)
    return live


@client.event
async def on_message(message):
    print("A message was sent!")
    if message.author == client.user:
        return


client.run(TOKEN)
