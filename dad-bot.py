import discord, random
client = discord.Client()
@client.event
async def on_ready():
    print(f"Logged in as {client.user}")
@client.event
async def on_message(message):
    try:
        add_pun = False
        if message.content.startswith('im') or message.content.startswith('Im') or message.content.startswith(
                'IM') or message.content.startswith('iM') or message.content.startswith(
                "I'm") or message.content.startswith("I'M") or message.content.startswith(
                "i'm") or message.content.startswith("i'M"):
            ls = message.content
            ls = ls.split()
            del ls[0]
            string = ""
            for i in ls:
                string = string + i + " "
            if string.lower() == "pun-bot " or string.lower() == "pun bot ":
                await message.channel.send("You're not Pun Bot! I'm Pun-Bot!")
            else:
                await message.channel.send(f"Hi {string}, I'm Pun-Bot!")
        else:
            ls = message.content
            ls = ls.split()
            for i in ls:
                if message.author == client.user:
                    break
                if i.lower() == "im" or i.lower() == "i'm":
                    string = ""
                    add_pun = True
                if add_pun:
                    if i.lower() == "im" or i.lower() == "i'm":
                        pass
                    string = string + i + " "
            string = string.split()
            final_product = ""
            for items in string:
                if items.lower() == "im" or items.lower() == "i'm":
                    pass
                else:
                    final_product = final_product + items + " "
            if final_product.lower() == "pun-bot " or final_product.lower() == "pun bot ":
                await message.channel.send("You're not Pun Bot! I'm Pun-Bot!")
            else:
                await message.channel.send(f"Hi {final_product}, I'm Pun-Bot!")
    except:
        pass
ask = False
wait_for_ans = False
@client.event
async def on_message(message):
    global ask
    global wait_for_ans
    dice_roll = random.randint(0, 25)
    if dice_roll == 6:
        ask = True
    word_list = ['ok', 'sad', 'happy', 'angry', 'hungry', 'small', 'big', 'excited', 'nice', 'mad']
    trait = word_list[random.randint(0, (len(word_list) - 1))]
    if ask:
        await message.channel.send(f'Are you {trait}?')
        wait_for_ans = True
        ask = False
    if wait_for_ans:
        print("e")
        if message.content.startswith('yes'):
            await message.channel.send(f"Hi {trait}, I'm Pun-Bot!")
            wait_for_ans = False
        elif message.content.startswith('no'):
            await message.channel.send(f"Yeah, I guess not! You're {message.author.mention}")
            wait_for_ans = False
client.run('Nzk2NzUxNDM0MjcyMDc5ODcy.X_cemA.7BXouDrrYZD7ddRYjEgjNmhMWbM')