#bot.py
import os
import discord

from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    for guild in client.guilds:
        if guild.name == GUILD:
            break
        
        print (
            f'{client.user} is connected to the following guilde:\n'
            f'{guild.name}(id: {guild.id})'
        )

        members = '\n - '.join([member.name for member in guild.members])
        print(f'Guild Members:\n - {members}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('$help'):
        await send_dm(message)

async def send_dm(message):
    channel = await message.author.create_dm()
    print(channel.id)
    await channel.send("god is dead :) ")
    #await message.channel.send("Hi, I'm here to help!")

client.run(TOKEN)
