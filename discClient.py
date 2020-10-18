import discord
from config import *
from holoChannelID import ALLHOLOIDS
from yt import isLive
from embeddedMessages import *
import time
import asyncio
# bot = discord.Client()
# bchannel = bot.get_channel(BOTCHANNEL)

# @bot.event
# async def on_message(message):
#     print("A message was sent!")
#     await bchannel.send(embed=startMessage())
#     if message.author == bot.user:
#         return
class MyClient(discord.Client):
    def __init__(self):
        super().__init__()
        # create the background task and run it in the background
        self.bg_task = self.loop.create_task(self.background_query())

    async def on_message(self, message):
        if message.author.id == self.user.id:
            return
        print("Message sent")

    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    # async def my_background_task(self):
    #     await self.wait_until_ready()
    #     counter = 0
    #     channel = self.get_channel(BOTCHANNEL)  # channel ID goes here
    #     while not self.is_closed():
    #         counter += 1
    #         await channel.send(counter)
    #         await asyncio.sleep(5)  # task runs every 60 seconds

    async def readyInnerLoop(channel):
        print("entered inner " + channel)
        await channel.send(embed=startMessage())
        print("printed send")
        j = 0
        for i in ALLHOLOIDS:
            live = isLive(j)
            if(live):
                print(i[0])
                embed = displayEmbed(j, channel, i)
                await channel.send(embed=embed)
            j = j+1
        print("Done with innerloop")

    async def background_query(self):
        await self.wait_until_ready()
        channel = self.get_channel(BOTCHANNEL)
        while not self.is_closed():
            print("Printing clearing")
            await channel.send(embed=clearMessageEmbed())
            await asyncio.sleep(3)
            await channel.purge(limit=60, check=is_me)
            print("Going into innerloop")
            await channel.send(embed=startMessage())
            j = 0
            for i in ALLHOLOIDS:
                live = isLive(j)
                if(live):
                    embed = displayEmbed(j, channel, i)
                    await channel.send(embed=embed)
                j = j+1
            print("Done with innerloop")
            print("Going to sleep")
            await asyncio.sleep(300)
            print("Awaken my bustas")


client = MyClient()


def is_me(m):
    return m.author == client.user


client.run(TOKEN)
