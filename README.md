# Prayer Notification Bot
## Introduction
This project is a Prayer Notification Bot built using Python, the Discord API, and Muslim Pro with asynchronous task management via Asyncio. It allows users to receive automated notifications based on their location and the scheduled prayer times. The bot can be executed on various environments, including a **virtual machine (VM)**, though I personally use a **Raspberry Pi 4B** for execution.

The bot is flexible and can be adapted for other types of scheduled notifications, making it a versatile tool for time-based event reminders.

## Features
### **1. How to Receive Notifications ?**
The bot sends automated notifications to the user based on prayer times. It calculates the times depending on the user's geographical location, ensuring that the reminders are accurate.

To start receiving notifications :

Use the **pray** command followed with the name of the city you are currently located.

`.pray <location>`

Here's how it looks when you'll start receiving Discord Notifications :

![start](https://media.discordapp.net/attachments/1204126618130452521/1288959449947574323/start.png?ex=68566c48&is=68551ac8&hm=af5c609da63d39075117a0e6954eddcc121fee5b8d80953116c96e35220fed02&=&format=webp&quality=lossless&width=701&height=139)

We can observe above that you can **specify your country** if you are having trouble finding your city


### **2. View Notifications**
The bot sends notifications directly to a specified Discord  user at the designated prayer times. These notifications are customized based on the user's location.

The bot will send Prayer start notifications based on your location.


Example of a notification displayed on Discord :

![notifications](https://media.discordapp.net/attachments/1204126618130452521/1288959449649647658/notifications.png?ex=68566c48&is=68551ac8&hm=a8d333b8057f509380038792b0c13ad5bd1bcd1ab70c727ac1cfb4f9188c4441&=&format=webp&quality=lossless&width=435&height=387)


### **3. Change Location Settings**
You can easily change your location without restarting the bot. Simply modify the city or geographical location, and the bot will automatically update its settings by storing the new location in a JSON file.

To change the location :

Use the same **pray** command as when starting the bot, but specify the new city. 

`.pray <location>`

The bot will automatically update the location information and save it to the JSON file without needing a restart.
The new location will be applied immediately for the upcoming notifications. 

![modification](https://media.discordapp.net/attachments/1204126618130452521/1288959449352114246/modifications.png?ex=68566c48&is=68551ac8&hm=9b9b60069ace854259e34c67bc27689707f4ed0ceb0d8d8275637079aad74fc6&=&format=webp&quality=lossless&width=902&height=144)

Example of the JSON format we're using :

`{
  "546546546546546546": {
    "link": "https://prayer-times.muslimpro.com/fr/Horaires-prieres-Orleans-France-2989317",
    "location": "Orl\u00e9ans"
  }
}`

### **4. Stop Receiving Notifications**
To stop receiving notifications, you can use the **pstop** command like this :

`.pstop`

![stop](https://media.discordapp.net/attachments/1204126618130452521/1288959450178392064/stop.png?ex=68566c48&is=68551ac8&hm=572e4429945bb8b7fb3e1f360d53d471fefcea1e56a161bf83f51342a3102881&=&format=webp&quality=lossless&width=556&height=151)
## Installation
### Clone the repository :
`git clone https://github.com/IncendieForet/PrayersNotifications.git`
### Install the required dependencies:
`pip install -r requirements.txt`
### Configure the bot with your channel ID and your Discord API key
`ia.get_channel(0000000000000).send("connected")`

`ia.run("YourToken")`
### Run the bot on your device :
`python prayernotifications.py`
