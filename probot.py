import discord
import asyncio
from discord.ext import commands
import json
import os
from time import strftime,localtime
from datetime import datetime
import time
import platform

p=commands.Bot(command_prefix='P')
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
  
@p.command(pass_context=True)
async def ping():
  await p.say('Why you ping me **NANI**????')
  
p.remove_command('help')
@p.command(pass_context=True)
async def help(ctx):
    embed=discord.Embed(color=0x800000)
    embed.add_field(name='Help!',value='Shows this message')
    embed.add_field(name='Puptime',value='Shows bot uptime')
    await p.send_message(ctx.message.author,embed=embed)

@p.command(pass_context=True)
async def uptime(ctx,type:str=None):
    now=time.time()
    secs=int(now-start)
    mins=int(secs//60)
    hours=int(mins//60)
    if type:
        if type=='s':
          await p.say(f'Uptime is {secs} seconds.')
        elif type=='m':
          await p.say(f'Uptime is {mins} minutes.')
        elif type=='h':
          await p.say(f'Uptime is {hours} hours.')
    elif type==None:
        await p.say('You must specify the type:s for seconds,m for minutes,h for hours.')
    
p.run(os.getenv('Token'))
