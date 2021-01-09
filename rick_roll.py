import discord
import time
client = discord.Client()
@client.event
async def on_ready():
    print(f"Logged in as {client.user}")
    print("Ready to spam.")
@client.event
async def on_message(message):
    if message.content.startswith('!e'):
        file = open('rick_roll.txt', 'r')
        for i in file.readlines():
            await message.channel.send(i)
            time.sleep(3)
client.run('token')
