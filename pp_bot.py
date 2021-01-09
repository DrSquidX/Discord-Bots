import discord
client = discord.Client()
@client.event
async def on_ready():
    print(f"Logged in as {client.user}")
@client.event
async def on_message(message):
    if 'pp' in message.content.lower() or 'p p' in message.content.lower():
        await message.channel.send(f'{message.author.mention} OI DONT SAY THE FORBIDDEN LETTERS')
        if message.author == client.user:
            await message.channel.send('My bad for saying the forbidden letters.')
        await message.delete()
client.run('Nzk2Njg2MDk4NjU5MTQ3Nzk2.X_bhvw.1t3rD_4nod-UyAoliXo182VvPj8')