# HoloBot! 
## I'm currently working on making the bot so all that needs to be done is you just simply invite the bot to your server! Progress is going to be slow as midterms are coming up but I will do my best. Working on it in a separate repo so this one doesn't get all cluttered from testing. 
***This is my first outside of class project that I've done, so please be gentle if you're looking at the repo.***

***However if you see anything that can be improved I ask that you please notify me!***
![image](https://imgur.com/LRRYAjQ.png)
## How to run it
1. First go to the [discord developer portal](https://discord.com/developers/applications)
2. Hit New Application
3. Head to Bot, and create one
4. Copy its token and paste it into config.py
5. Then go into OAuth2, and under scopes hit bot
6. Under bot permissions make sure Send Messages, Manage Messages and Read Message History is ticked.
7. Copy the generated link and invite the bot your server.
8. Now copy the respective channel ID's and paste them into config.py (more clarification in the config.py file)
9. Download [python](https://www.python.org/downloads/) if you haven't
10. Head to a terminal and run "pip install pipenv"
11. Now run these commands (Make sure you're in the correct directory) 
    * pipenv install
    * pipenv run python discClient.py
    ~ Note you must keep this shell running for it to work ~ 
 
  After all that your bot should be working! If there is interest in getting this bot to run on a server, like it is on my server, like heroku I wouldn't mind adding it in!
  
## Description
HoloBot is a discord bot that scrapes the HTML of HoloLive members
youtube channel, which then ascertains if that user is live. Then sends
a message into a respective discord channel.

I hope that anybody who has an interest in HoloLive and runs a
discord would be using this bot.

My main goal of this project was twofold. For one, to get a
better understanding of how it feels to manage a project as well as
contributing to a community that shares an avid interest of mine!

### Any issues/suggestions please dm me on discord Lukeisun#4168
### Feel free to join the discord! https://discord.gg/c2ZjFQH
