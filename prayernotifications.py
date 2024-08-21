import discord,json,requests,datetime,asyncio
from discord.ext import commands,tasks
from bs4 import BeautifulSoup

ia=commands.Bot(command_prefix='.', intents=discord.Intents().all())  

@ia.event
async def on_ready():
    print(f"{ia.user.name} is connected")
    ia.get_channel(0000000000000).send("connected")#replace by your ID Channel
    AutoPrayer.start()

@ia.command(name='pray')#Start receiving prayer Notifications by assigning your city or by modifying it and add link to the json file
async def PrayDB(ctx,*,lien):
    with open("praydb.json",'r') as f:
        data=json.load(f)
    if str(ctx.author.id) not in data and lien.startswith("https://www.muslimpro.com/en/locate?country_code="):#Assigning your MP city link
        page=requests.get(lien)
        data[str(ctx.author.id)]={}
        data[str(ctx.author.id)]['link']=lien
        data[str(ctx.author.id)]['location']=BeautifulSoup(page.content, 'html.parser').find(class_='location').text
        await ctx.send(f"Vous recevrez dorénavant les notifications de prière de {data[str(ctx.author.id)]['location']} chaque jour")
    elif lien.startswith("https://www.muslimpro.com/en/locate?country_code=") and data[str(ctx.author.id)]['link']!=lien:#Modofying your MP city link
        page=requests.get(lien)
        data[str(ctx.author.id)]['link']=lien
        await ctx.send(f"Modification de la ville de {data[str(ctx.author.id)]['location']}, vous recevrez dorénavant les notifications de prière de {BeautifulSoup(page.content, 'html.parser').find(class_='location').text}")
        data[str(ctx.author.id)]['location']=BeautifulSoup(page.content, 'html.parser').find(class_='location').text
    else:#Invalid MP link
        await ctx.send("Lien invalide, veuillez réssayer")
    with open("praydb.json",'w') as f:
        json.dump(data,f)

@ia.command(name='pstop')#Stop receiving prayer Notifications
async def StopDB(ctx,*args):
    with open("praydb.json",'r') as f:
        data=json.load(f)
    if str(ctx.author.id) in data:#You did receive notifications before
        del data[str(ctx.author.id)]
        await ctx.send("Vous ne recevrez désormais plus de notifications de prière")
    else:#You didn't receive notifications before
        await ctx.send("Vous ne recevez pas de notifications de prière")
    with open("/home/adam/praydb.json",'w') as f:
        json.dump(data,f)

@tasks.loop(time=datetime.time(1))#Automate the task everyday at 1 am
async def AutoPrayer():
    name=["Sobh","Sunrise","Dohr","Asr","Maghreb","Icha"]
    for x in [0,2,3,4,5]:#5 Prayers a day
        for i,j in sortHor(x):
            then=datetime.datetime.now().replace(hour=int(j.split(':')[0]),minute=int(j.split(':')[1]))
            await asyncio.sleep((then-datetime.datetime.now()).total_seconds())
            await ia.get_user(int(i)).send(f"{Location(i)} | Heure pour {name[x]} à {j}")

def Location(id):#Return the location of a user from the json file
    with open("praydb.json",'r') as f:
        data=json.load(f)
    return data[id]['location']

def sortHor(nb):#Sort the different timetables of one single Prayer by ascending order
    with open("praydb.json",'r') as f:
        data=json.load(f)
    hor={}
    for i in data:
        page=requests.get(data[i]['link'])
        hor.update({i:BeautifulSoup(page.content, 'html.parser').find_all('p', class_='praytime')[nb].text})
    return sorted(hor.items(), key=lambda x:x[1])

ia.run("YourToken")