import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print('Bot is ready')


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.author.guild_permissions.manage_messages == False:
        await message.author.edit(nick = 'Chad')
    await message.channel.send('nah he tweaking')
      
    
TOKEN = os.getenv("TOKEN")
client.run(TOKEN)
