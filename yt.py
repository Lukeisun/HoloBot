from apiclient.discovery import build
from config import YTAPI
import re
import textwrap


def findVideoID(resp):
    truncated = textwrap.shorten(str(resp), width=302)
    ID = re.findall("([A-Za-z0-9_\-]{11})", truncated)
    return ID[len(ID)-1]


def returnResp(channelID):
    youtube = build('youtube', 'v3', developerKey=YTAPI)
    request = youtube.search().list(
         part="snippet",
         channelId=channelID,
         eventType="live",
         type="video"
     )
    response = request.execute()
    return response


def isLive(resp):
    x = re.search("totalResults': 1", str(resp))
    if x is None:
        return False
    else:
        return True


x = returnResp("UCL_qhgtOy0dy1Agp8vkySQg")
print(findVideoID(x))
