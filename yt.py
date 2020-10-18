import re
import requests
from bs4 import BeautifulSoup


def findVideoID(channelIDX, ID):
    resp = returnResp(channelIDX, ID)
    ID = re.search('"videoId":"[A-Za-z0-9_\-]{11}"', str(resp))
    retVal = re.search("[A-Za-z0-9_\-]{11}", str(ID))
    return str(retVal.group())


def returnResp(channelIDX, ID):
    fetch = "https://www.youtube.com/channel/"+ID[channelIDX][0]
    request = requests.get(fetch)
    response = BeautifulSoup(request.text, "html.parser")
    return response


def isLive(channelIDX, ID):
    response = returnResp(channelIDX, ID)
    x = re.search('"iconType":"LIVE"', str(response))
    if x is not None:
        return True
    else:
        return False
