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
        live = query("UCUKD-uaobj9jiqB-VXt71mA")
        if(live):
            await channel.send('LIVE!')
        time.sleep(60)

def query(channelID):
    info = returnResp(channelID)
    live = isLive(info)
    return live


@client.event
async def on_message(message):
    print("A message was sent!")
    if message.author == client.user:
        return


client.run(TOKEN)
