import discord
import asyncio
import os
import sys
from discord import Member
from discord.ext import commands
from itertools import cycle

moji1=None
moji2=None
moji3=None

client = discord.Client()

token = os.environ['key']

@client.event
async def on_ready():
    print("Logged in ") 
    print(client.user.name)
    print(client.user.id)
    print("===============")
    
@client.event
async def on_member_join(member):
    fmt = '{1.name} 에 오신것을 환영합니다., {0.mention} 님. '
    channel = member.server.get_channel("450316317988356100")
    role = discord.utils.get(member.server.roles, id="450322259660374036")
    await client.add_roles(member, role)

    global moji3
    
    role = discord.utils.get(member.server.roles, id="460137279533481984")
    await client.add_roles(member, role)

    game = "레인보우 식스 하시면 눌러주세요"
    moji3 = await client.send_message(channel, game)

@client.event
async def on_reaction_add(reaction, user):

    global moji3
    
    channel = client.get_channel('450316317988356100')
        
    if reaction.emoji == "\U0001F3AE":
        role = discord.utils.get(user.server.roles, id="485720562472189952")
        await client.add_roles(user, role)
        
@client.event
async def on_reaction_remove(reaction, user):
        
    if reaction.emoji == "\U0001F3AE":
        role = discord.utils.get(user.server.roles, id="485720562472189952")
        await client.remove_roles(user, role)

client.run(token)
