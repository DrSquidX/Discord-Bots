import discord
import random
from discord.ext import commands
client2 = commands.Bot(command_prefix = 'a?')

@client2.event
async def on_ready():
    print("bot is ready")
@client2.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member : discord.Member, *, reason=None):
    try:
        await member.kick(reason=reason)
        await ctx.send(f'Successfully kicked {member}.')
    except:
        await ctx.send(f'You lack permissions!')
@client2.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member : discord.Member, *, reason=None):
    try:
        await member.ban(reason=reason)
        await ctx.send(f'Successfully Banned {member}.')
    except:
        await ctx.send(f'You lack permissions!')

client2.run('token')
