from holoChannelID import HOLOIDS
import re
import requests
from bs4 import BeautifulSoup


def findVideoID(channelIDX):
    resp = returnResp(channelIDX)
    ID = re.search('"videoId":"[A-Za-z0-9_\-]{11}"', str(resp))
    retVal = re.search("[A-Za-z0-9_\-]{11}", str(ID))
    return str(retVal.group())


def returnResp(channelIDX):
    fetch = "https://www.youtube.com/channel/"+HOLOIDS[channelIDX][0]
    request = requests.get(fetch)
    response = BeautifulSoup(request.text, "html.parser")
    return response


def isLive(channelIDX):
    response = returnResp(channelIDX)
    x = re.search('"iconType":"LIVE"', str(response))
    if x is not None:
        return True
    else:
        return False
