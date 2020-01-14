import discord
import asyncio
import os
import sys
from discord import Member
from discord.ext import commands
from itertools import cycle

client = discord.Client()

token = os.environ["key"]

@client.event
async def on_ready():
    print("Logged in ") 
    print(client.user.name)
    print(client.user.id)
    print("====================")

@client.event
async def on_message(message):
    if message.content.startswith("!역할") and message.channel.id == 644507145026404352:
        
        channel = client.get_channel(592296776850210816)

        embed = discord.Embed(title="레인보우 식스", description="레인보우 식스 관련 역할", color=0x00ff00)
        embed.add_field(name="멘션 허용", value="레인보우 식스 관련 멘션을 받으려면 첫번째 버튼을 누르세요", inline=False)
        embed.add_field(name="멘션 거부", value="레인보우 식스 관련 멘션을 받지 않으려면 두번째 버튼을 누르세요", inline=False)
        message = await channel.send(embed=embed)
        #message 변수가 본래 있던 스크립트의 변수, Message는 새로 생긴 Discord Module의 함수 (오류가 생길 수 있으니 테스트 필요)
        await Message.add_reaction(message, emoji="\U0001F600")
        await Message.add_reaction(message, emoji="\U0001F64F")
        
        embed = discord.Embed(title="데스티니 2", description="데스티니 2 관련 역할", color=0x00ff00)
        embed.add_field(name="멘션 허용", value="데스티니 2 관련 멘션을 받으려면 첫번째 버튼을 누르세요", inline=False)
        embed.add_field(name="멘션 거부", value="데스티니 2 관련 멘션을 받지 않으려면 두번째 버튼을 누르세요", inline=False)
        message = await channel.send(embed=embed)
        await Message.add_reaction(message, emoji="\U0001F910")
        await Message.add_reaction(message, emoji="\U0001F44F")
        
        embed = discord.Embed(title="GTA5", description="GTA5 관련 역할", color=0x00ff00)
        embed.add_field(name="멘션 허용", value="GTA5 관련 멘션을 받으려면 첫번째 버튼을 누르세요", inline=False)
        embed.add_field(name="멘션 거부", value="GTA5 관련 멘션을 받지 않으려면 두번째 버튼을 누르세요", inline=False)
        message = await channel.send(embed=embed)
        await Message.add_reaction(message, emoji="\U0001F91D")
        await Message.add_reaction(message, emoji="\U0001F91A")

        embed = discord.Embed(title="마인크래프트", description="마인크래프트 관련 역할", color=0x00ff00)
        embed.add_field(name="멘션 허용", value="마인크래프트 관련 멘션을 받으려면 첫번째 버튼을 누르세요", inline=False)
        embed.add_field(name="멘션 거부", value="마인크래프트 관련 멘션을 받지 않으려면 두번째 버튼을 누르세요", inline=False)
        message = await channel.send(embed=embed)
        await Message.add_reaction(message, emoji="\U0001F590")
        await Message.add_reaction(message, emoji="\U0001F488")

        embed = discord.Embed(title="콜오브듀티", description="콜오브듀티 관련 역할", color=0x00ff00)
        embed.add_field(name="멘션 허용", value="콜오브듀티 관련 멘션을 받으려면 첫번째 버튼을 누르세요", inline=False)
        embed.add_field(name="멘션 거부", value="콜오브듀티 관련 멘션을 받지 않으려면 두번째 버튼을 누르세요", inline=False)
        message = await channel.send(embed=embed)
        await Message.add_reaction(message, emoji="\U0001F5A5")
        await Message.add_reaction(message, emoji="\U00002328")

    if message.content.startswith("!가이드") and message.channel.id == 644507145026404352:  
        channel = client.get_channel(638039195234992155)

        embed = discord.Embed(title="[Unknown Company]에 오신 것을 환영합니다!", description="아티스트(Artist)들과 게이머(Gamer)들을 위한 커뮤니티로 기본적인 예의를 지켜주시길 바랍니다. 공지(#notice)를 종종 확인해주시고, 필요에 따라 #role 에서 역할을 부여받으시면 됩니다. 이 내용을 모두 확인하셨다면 아래 이모지 버튼을 눌러 활동에 참여하세요!", color=0x00ff00)
        message = await channel.send(embed=embed)
        await Message.add_reaction(message, emoji="\U0001F446")

@client.event
async def on_reaction_add(reaction, user):

    if reaction.emoji == "\U0001F446":
        role = discord.utils.get(user.server.roles, id="450322259660374036")
        await Member.add_roles(user, role)
        
    if reaction.emoji == "\U0001F44F":
        role = discord.utils.get(user.server.roles, id="638038286392098818")
        await Member.add_roles(user, role)

    if reaction.emoji == "\U0001F600":
        role = discord.utils.get(user.server.roles, id="592295687786594305")
        await Member.add_roles(user, role)

    if reaction.emoji == "\U0001F64F":
        role = discord.utils.get(user.server.roles, id="592296285994745856")
        await Member.add_roles(user, role)

    if reaction.emoji == "\U0001F910":
        role = discord.utils.get(user.server.roles, id="638035231349276672")
        await Member.add_roles(user, role)
    
    if reaction.emoji == "\U0001F91D":
        role = discord.utils.get(user.server.roles, id="638522416611721216")
        await Member.add_roles(user, role)
    
    if reaction.emoji == "\U0001F91A":
        role = discord.utils.get(user.server.roles, id="638038441010921484")
        await Member.add_roles(user, role)
    
    if reaction.emoji == "\U0001F590":
        role = discord.utils.get(user.server.roles, id="638036108235636746")
        await Member.add_roles(user, role)
    
    if reaction.emoji == "\U0001F488":
        role = discord.utils.get(user.server.roles, id="638038347746377768")
        await Member.add_roles(user, role)

    if reaction.emoji == "\U0001F5A5":
        role = discord.utils.get(user.server.roles, id="638035923799375893")
        await Member.add_roles(user, role)

    if reaction.emoji == "\U00002328":
        role = discord.utils.get(user.server.roles, id="638038402297626634")
        await Member.add_roles(user, role)
        
@client.event
async def on_reaction_remove(reaction, user):

    if reaction.emoji == "\U0001F446":
        role = discord.utils.get(user.server.roles, id="450322259660374036")
        await Member.remove_roles(user, role)
        
    if reaction.emoji == "\U0001F44F":
        role = discord.utils.get(user.server.roles, id="638038286392098818")
        await Member.remove_roles(user, role)

    if reaction.emoji == "\U0001F600":
        role = discord.utils.get(user.server.roles, id="592295687786594305")
        await Member.remove_roles(user, role)

    if reaction.emoji == "\U0001F64F":
        role = discord.utils.get(user.server.roles, id="592296285994745856")
        await Member.remove_roles(user, role)

    if reaction.emoji == "\U0001F910":
        role = discord.utils.get(user.server.roles, id="638035231349276672")
        await Member.remove_roles(user, role)
    
    if reaction.emoji == "\U0001F91D":
        role = discord.utils.get(user.server.roles, id="638522416611721216")
        await Member.remove_roles(user, role)
    
    if reaction.emoji == "\U0001F91A":
        role = discord.utils.get(user.server.roles, id="638038441010921484")
        await Member.remove_roles(user, role)
    
    if reaction.emoji == "\U0001F590":
        role = discord.utils.get(user.server.roles, id="638036108235636746")
        await Member.remove_roles(user, role)
    
    if reaction.emoji == "\U0001F488":
        role = discord.utils.get(user.server.roles, id="638038347746377768")
        await Member.remove_roles(user, role)

    if reaction.emoji == "\U0001F5A5":
        role = discord.utils.get(user.server.roles, id="638035923799375893")
        await Member.remove_roles(user, role)

    if reaction.emoji == "\U00002328":
        role = discord.utils.get(user.server.roles, id="638038402297626634")
        await Member.remove_roles(user, role)
        
    

client.run(token)
