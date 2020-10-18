import discord
import datetime
import pytz
from yt import findVideoID
from config import WELCOMEMSG


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
    embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/95706039978033152/a_3533b0f7cf4b5c90faf407e68b09b668.gif?size=128")
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
