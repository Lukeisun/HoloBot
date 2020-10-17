import discord
from config import *
from holoChannelID import HOLOIDS
from yt import isLive
from embeddedMessages import *
import time
client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    channel = client.get_channel(BOTCHANNEL)
    while True:
        await channel.send(embed=clearMessageEmbed())
        time.sleep(5)
        await channel.purge(check=is_me)
        # async for msg in channel.history():
        #     await channel.delete_messages(msg)
        await channel.send(embed=startMessage())
        j = 0
        for i in HOLOIDS:
            live = isLive(j)
            if(live):
                embed = displayEmbed(j, channel, i)
                await channel.send(embed=embed)
            j = j+1
        time.sleep(6000)


def is_me(m):
    return m.author == client.user


@client.event
async def on_message(message):
    print("A message was sent!")
    if message.author == client.user:
        return


client.run(TOKEN)
