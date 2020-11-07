import discord
import datetime
import pytz
from yt import findVideoID
from config import WELCOMEMSG

def joinServerEmbed():
    embed = discord.Embed(title = "**HoloBot has arrived**",
                        color = discord.Colour.blue(),
                        description='Please have an *admin*, reply with the channel names you would like the bot to post to\n' +
                                    '*Note that you must write which HoloLive group you would like to be updated on*\n' +
                                    'If you would like them all in one chnanel then just .channelALL "channel-name"' +
                                    '\n**Acceptable Commands**\n.channelEN  *For English crew*\n.channelJP  *For the Japanese crew*'+
                                    '\n.channelID   *For the Indonesian crew*\n.channelHST  *For the HoloStar crew*\n'+
                                    '.channelALL    *For the bot to post all updates in one channel*'
    )
    embed.add_field(name="Example 1", value='.channelID botID')
    embed.add_field(name="Example 2", value='.channelEN bot-tracker')
    embed.set_thumbnail(url="https://i.imgur.com/hJSQhKN.png")
    return embed

def clearMessageEmbed():
    embed = discord.Embed(
        title='**Clearing messages**',
        color=discord.Colour.red()
    )
    return embed


def startMessage():
    embed = discord.Embed(
        title='**' + WELCOMEMSG + '**',
        description='Hello everybody! This is HoloBot reporting live!',
        color=discord.Colour.blue()
    )
    embed.add_field(name="**Github**",value="https://github.com/Lukeisun/HoloBot")
    embed.set_thumbnail(url="https://i.imgur.com/hJSQhKN.png")
    return embed


def displayEmbed(j, i, ID):
    vidID = findVideoID(j, ID)
    embed = discord.Embed(
        title=i[1]+' is live!',
        description='https://www.youtube.com/watch?v=' + vidID,
        color=discord.Colour.blue()
    )
    dt_JST = datetime.datetime.now(tz=pytz.timezone('Asia/Tokyo'))
    dt_EST = dt_JST.astimezone(pytz.timezone('US/Eastern'))
    embed.set_footer(text=dt_JST.strftime('%X %Z')
                     + '\n' + dt_EST.strftime('%X %Z'))
    embed.add_field(name="**Link**",
                    value="[☆\*:.｡.o(≧▽≦)o.｡.:\*☆](https://www.youtube.com/watch?v=" +
                    vidID + ")")
    embed.set_image(
     url="https://i.ytimg.com/vi/"+vidID+"/hqdefault_live.jpg")
    return embed
