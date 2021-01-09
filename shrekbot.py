import discord
import time
client = discord.Client()
@client.event
async def on_ready():
    print(f"Logged in as {client.user}")
    print("Ready to spam.")
@client.event
async def on_message(message):
    if message.content.startswith('!shrek'):
        file = open('shrek.txt', 'r')
        for i in file:
            i = i.split()
            for item in i:
                await message.channel.send(item)
                time.sleep(0.8)
client.run('Nzk2NzQwMTI4NzY0NTkyMTU4.X_cUEQ.Qw-jkcnmuNhb4fyIm8juxuvTIZw')