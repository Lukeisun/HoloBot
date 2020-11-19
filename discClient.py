import discord
from config import *
from holoChannelID import *
from yt import isLive
from embeddedMessages import *
import time
import asyncio
import json
import os
from discord.ext import commands


class MyBot(commands.Bot):
    def __init__(self, command_prefix):
        super().__init__(command_prefix)
        # create the background task and run it in the background
        self.bg_task = self.loop.create_task(self.background_query())

    async def on_guild_join(self, guild):
        channel = discord.utils.get(guild.text_channels, name='general')
        await channel.send(embed=joinServerEmbed())
        writeToJson(guild)

    async def on_guild_remove(self, guild):
        new_data = {
            "names": []
        }
        with open('channels.json', 'r') as f:
            data = json.load(f)
        if data == new_data:
            pass
        else:
            for entry in data["names"]:
                if guild.name == entry["name"]:
                    pass
                else:
                    print('hai'+guild.name)
                    new_data["names"].append(entry)
            print(new_data)
            dumpJson(new_data)

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
                for i in range (0, 4):
                    if i == 0:
                        channel = self.get_channel(CHANNELJP)
                        ID = HOLOIDS
                    elif i == 1:
                        channel = self.get_channel(CHANNELEN)
                        ID = HOLOENIDS
                    elif i == 2:
                        channel = self.get_channel(CHANNELST)
                        ID = HOLOSTARSIDS
                    elif i == 3:
                        channel = self.get_channel(CHANNELID)
                        ID = HOLOidIDS
                    await postMessageInChannel(channel, ID)
            elif FLAGFORINDIVIDUALCHANNEL == 1:
                channel = self.get_channel(BOTCHANNEL)
                ID = ALLHOLOIDS
                await postMessageInChannel(channel, ID)
            print("Going to sleep")
            await asyncio.sleep(300)
            print("Awaken my bustas\n")


client = MyBot(command_prefix='.')
bot = commands.Bot(command_prefix='.')

@bot.command()
async def channelEN(ctx, args=None):
    await updateJSONchannel(ctx,args,"en")

@bot.command()
async def channelJP(ctx, args=None):
    await updateJSONchannel(ctx,args,"jp")

@bot.command()
async def channelID(ctx, args=None):
    await updateJSONchannel(ctx, args,"id")

@bot.command()
async def channelHST(ctx, args=None):
    await updateJSONchannel(ctx, args, "hst")

@bot.command()
async def channelALL(ctx, args=None):
    await updateJSONchannel(ctx,args, "all")



async def updateJSONchannel(ctx,args, region):
     if args is None:
        await ctx.send("Please add a channel name")
     elif len(args)>1:
        channel = lookupChannel(ctx,args)
        if(channel is not None):
            updateJSON(region, ctx,channel)
            await ctx.send("Channel "+ region + " has been set to " + str(channel))
        else:
            await ctx.send("No such channel")


def lookupChannel(ctx,args):
    for channel in ctx.guild.text_channels:
        if(args == channel.name):
            return channel.id
    return None       


def updateJSON(region, ctx, channel):
    key = region+"ID"
    with open('channels.json', 'r') as f:
        data = json.load(f)
        for item in data["names"]:
            if ctx.guild.id == item['serverID']:
                item[key] = channel
                print(item[key])
    dumpJson(data)


def writeToJson(guild):
    with open('channels.json', 'r') as f:
        data = json.load(f)
        temp = data["names"]
        y = {
            'name': guild.name,
            'serverID': guild.id,
            'prefix': '.',
            'enID': None,
            'idID': None,
            'jpID': None,
            'hstID': None,
            'allID': None
        }
        temp.append(y)
    dumpJson(data)


def dumpJson(data):
    with open('channels.json', 'w') as f:
        json.dump(data, f, indent=4)


async def postMessageInChannel(channel, ID):
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

    print("Done with loop\n")


def is_me(m):
    return m.author == client.user


loop=asyncio.get_event_loop()
loop.create_task(client.start(TOKEN))
loop.create_task(bot.start(TOKEN))
loop.run_forever()
#client.run(TOKEN)
