import discord
import asyncio
from discord.ext import commands
import json
import os
from time import strftime,localtime
from datetime import datetime
import time
import platform

p=commands.Bot(command_prefix='P',pm_help=True)
start=time.time()

async def playing():
 while True:
  for x in range(999999):
    await p.change_presence(game=discord.Game(name='Made by Dabs Gt#5590'))
    await asyncio.sleep(18)
    await p.change_presence(game=discord.Game(name='Servers:'+str(len(p.servers))+'  Users:'+str(len(set(p.get_all_members())))))
    await asyncio.sleep(18)
    await p.change_presence(game=discord.Game(name='Type Phelp for info.'))
    await asyncio.sleep(18)
    
@p.event
async def on_ready():
  print('Bot is up!')
  p.loop.create_task(playing())
  
@p.event
async def on_member_join(member):
    role = discord.utils.get(member.server.roles, id="Dab Member")
    await p.add_roles(member, role)

@p.command(pass_context=True)
async def ping():
  await p.say('Why you ping me boi????')
  
p.remove_command('help')
@p.command(pass_context=True)
async def help(ctx):
    embed=discord.Embed(color=0x800000)
    embed.add_field(name='Help!',value='Shows this message')
    embed.add_field(name='Puptime',value='Shows bot uptime')
    await p.send_message(ctx.message.author,embed=embed)

@p.command(pass_context=True)
async def uptime(ctx):
    now=time.time()
    secs=int(now-start)
    await p.say(f'Uptime is: {secs} seconds.')

p.run(os.getenv('Token'))
