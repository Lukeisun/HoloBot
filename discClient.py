import discord
from config import *
from holoChannelID import *
from yt import isLive
from embeddedMessages import *
import time
import asyncio

class MyClient(discord.Client):
    def __init__(self):
        super().__init__()
        # create the background task and run it in the background
        self.bg_task = self.loop.create_task(self.background_query())

    async def on_message(self, message):
        if message.author.id == self.user.id:
            return

    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    async def background_query(self):
        await self.wait_until_ready()
        await asyncio.sleep(5)
        while not self.is_closed():
            if FLAGFORINDIVIDUALCHANNEL == 0:
                for chan in range (0, 4):
                    if chan == 0:
                        channel = self.get_channel(CHANNELJP)
                        ID = HOLOIDS
                    elif chan == 1:
                        channel = self.get_channel(CHANNELEN)
                        ID = HOLOENIDS
                    elif chan == 2:
                        channel = self.get_channel(CHANNELST)
                        ID = HOLOSTARSIDS
                    elif chan == 3:
                        channel = self.get_channel(CHANNELID)
                        ID = HOLOidIDS
                    await postMessageInChannel(channel, ID)
            elif FLAGFORINDIVIDUALCHANNEL == 1:
                channel = self.get_channel(BOTCHANNEL)
                ID = ALLHOLOIDS
                await postMessageInChannel(channel, ID)
            print("Going to sleep")
            await asyncio.sleep(300)
            print("Awaken my bustas")


client = MyClient()


async def postMessageInChannel(channel, ID):
    print("Printing clearing")
    await channel.send(embed=clearMessageEmbed())
    time.sleep(3)
    await channel.purge(limit=60, check=is_me)
    print("Going into innerloop")
    await channel.send(embed=startMessage())
    j = 0
    for i in ID:
        live = isLive(j, ID)
        if(live):
            embed = displayEmbed(j, i, ID)
            await channel.send(embed=embed)
        j = j+1
    print("Done with loop")


def is_me(m):
    return m.author == client.user


client.run(TOKEN)
