import discord
import asyncio
from discord.ext import commands
import json
import os
from time import strftime,localtime
from datetime import datetime
import time
import platform

d=commands.Bot(command_prefix='P')

async def playing():
 while True:
  for x in range(999999):
    await d.change_presence(game=discord.Game(name='Made by Dabs Yt#5590.'))
    await asyncio.sleep(18)
    await d.change_presence(game=discord.Game(name='Servers:'+str(len(d.servers))+'  Users:'+str(len(set(d.get_all_members())))))
    await asyncio.sleep(18)
    await d.change_presence(game=discord.Game(name='Type Phelp for info.'))
    await asyncio.sleep(18)
	
@d.event
async def on_ready():
  print('Bot is up!')
  d.loop.create_task(playing())
  
@d.command(pass_context=True)
async def ping():
  await d.say('Pong!')
  
@d.command()
async def time():
  t=strftime('%d/%m/%Y %H:%M:%S',localtime())
  await d.say(t)
	
@d.command(pass_context=True)
async def host(ctx):
  p = ctx.message.author
  c = ctx.message.channel
  
  t = await d.send_message(c,'Calculating...')
  ms = (t.timestamp-ctx.message.timestamp).total_seconds() * 1000
  await d.delete_message(t)
  pingt=f'{int(ms)}'

  e3=discord.Embed(title='Host info!',color=0x765400)
  e3.add_field(name='Platform',value=platform.system(),inline=True)
  e3.add_field(name='Platform Name',value=os.name,inline=True)
  e3.add_field(name='Python Version',value=platform.python_version(),inline=True)
  e3.add_field(name='Discord Version',value=discord.__version__,inline=True)
  e3.set_footer(text='Made by Dabs Yt#5590!')
  await d.send_message(p,embed=e3)

d.run(os.getenv('Token')
