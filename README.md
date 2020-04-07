# Creating your bot

1.) On Telegram, search @ BotFather, send him a “/start” message<br>
2.) Send another “/newbot” message, then follow the instructions to setup a name and a username<br>
3.) Your bot is now ready, be sure to save a backup of your API token, and correct, this API token is your bot_token

# Getting your Chat ID

1.) On Telegram, Create a New Group and add @RawDataBot <br>
2.) After you add the bot it will send a message

```json
        "chat": {
            "id": -435294640,
            "title": "Monitoring",
            "type": "group",
            "all_members_are_administrators": true
```
3.)Get your Chat ID.

# Setup Up Monitoring

1.) Change the Domain to the Domain you want to Monitor.<br>
``` domain = "https://mb.com.ph" ```<br>
2.) Add the Bot Token adn Chat ID <br>
```
bot_token = '1261531883:AAFVsN8rQTcRWHwy2voU6A3lYt1UCL7tF8k'
bot_chatID = '-435294640'
```

# Use Crontab For Continuous monitoring

1.) run EDITOR=nano crontab -e <br>
2.) The Crontab Below will run every 30 Minutes. <br>
``` */30 * * * * /path/123/monitor.py ```

![alt text](https://raw.githubusercontent.com/ctuIhu/check-host-bot/master/screenshot.png)

