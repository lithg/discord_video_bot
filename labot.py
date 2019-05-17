import asyncio
import discord

client = discord.Client()

@client.event
async def on_ready():
    print('Logado como: {0.user}'.format(client))
    await client.change_presence(activity=discord.Game(name='Vídeos a cada 24h =]'))

#-------------------------------------------------

@client.event
async def envia_videos():
    await client.wait_until_ready()
    channel = client.get_channel(578934037113077760) # ID CHANNEL
    while not client.is_closed():
        f=open("videos.txt", "r")           #BUSCA VÍDEO DO TXT
        link = f.read()
        await channel.send(link)
        await asyncio.sleep(86400) # 24 HORAS

client.loop.create_task(envia_videos())

client.run('NTc4OTMzNDxxxxxxxpU4R02aUV6AnUuoc') # BOT TOKEN
