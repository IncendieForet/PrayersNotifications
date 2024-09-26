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

![start](https://cdn.discordapp.com/attachments/1204126618130452521/1288959449947574323/start.png?ex=66f71488&is=66f5c308&hm=a5b321d6b37cd3ea4cdea6201dc62679a33f541d834359ec88e26f33dad3c412&)

We can observe above that you can **specify your country** if you are having trouble finding your city


### **2. View Notifications**
The bot sends notifications directly to a specified Discord  user at the designated prayer times. These notifications are customized based on the user's location.

The bot will send Prayer start notifications based on your location.


Example of a notification displayed on Discord :

![notifications](https://cdn.discordapp.com/attachments/1204126618130452521/1288959449649647658/notifications.png?ex=66f71488&is=66f5c308&hm=4f6c4d90dd066fc98da4d3f9aae014fa44b4da51951ddf465b03c57b29e041a3&)


### **3. Change Location Settings**
You can easily change your location without restarting the bot. Simply modify the city or geographical location, and the bot will automatically update its settings by storing the new location in a JSON file.

To change the location :

Use the same **pray** command as when starting the bot, but specify the new city. 

`.pray <location>`

The bot will automatically update the location information and save it to the JSON file without needing a restart.
The new location will be applied immediately for the upcoming notifications. 

![modification](https://cdn.discordapp.com/attachments/1204126618130452521/1288959449352114246/modifications.png?ex=66f71488&is=66f5c308&hm=168da45516519548f95ca1b0c310bc23650237728669754ba8ed939463593ba1&)

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

![stop](https://cdn.discordapp.com/attachments/1204126618130452521/1288959450178392064/stop.png?ex=66f71488&is=66f5c308&hm=d77fa38acb4b34ec6c1c6f0cfe5053139819c396caef326934e39c0ea9ac824e&)
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
