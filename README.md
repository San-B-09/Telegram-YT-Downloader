# Telegram-YT-Downloader
This repo contains code for building a YouTube Downloader telegram bot.

> ### Detailed blog for the repo can be found [HERE](https://bijawesanket.medium.com/youtube-content-downloader-telegram-bot-1501ba2fd8f8).

## Installation Details
All the required modules are listed under requirements.txt. Run the following command to install the same:
```
C:\> pip install -r requirements.txt
```

## Essential Requirements
Create a new telegram chatbot using [BotFather](https://core.telegram.org/bots#6-botfather).

Then, create a ```.env``` file and add following variables
```
API_KEY = "here goes your access token from BotFather"
BOT_USER_NAME = "the username you entered"
URL = "the hosting link that we will create later"
```

## Bot Details
```app.py``` contains the complete code for base bot built using ```Flask```. Additionally, we've used **webhook** which provides us a way of letting the bot call our server whenever a message is called, so that we don’t need to make our server suffer in a while loop waiting for a message to come.

### For deployment details, refer this [blog]()

## Go talk to your BOT!
![Sample Chat](https://github.com/San-B-09/Telegram-YT-Downloader/blob/master/README%20Images/Sample%20Chat%20gif.gif)
