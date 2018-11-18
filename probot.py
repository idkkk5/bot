import discord
import asyncio
from discord.ext import commands
import json
import os
from time import strftime,localtime

d=commands.Bot(command_prefix='D')

async def playing():
 while True:
  for x in range(999999):
    await d.change_presence(game=discord.Game(name='Made by Dabs Gt#5590!!'))
    await asyncio.sleep(18)
    await d.change_presence(game=discord.Game(name='Servers:'+str(len(d.servers))+'  Users:'+str(len(set(d.get_all_members())))))
    await asyncio.sleep(18)
    await d.change_presence(game=discord.Game(name='24/7 ONLINE Hosted on Heroku!'))
    await asyncio.sleep(18)
    
@d.event
async def on_ready():
  print('Bot is up!')
  d.loop.create_task(playing())
    
@d.command(pass_context=True)
async def ping():
  await d.say('Pongo!')
  
@d.command()
async def time():
  t=strftime('%d/%m/%Y %H:%M:%S',localtime())
  await d.say(t)
  
@d.command(pass_context=True)
async def pingo(ctx):
  t = await d.say('Calculating...')
  ms = (t.timestamp-ctx.message.timestamp).total_seconds() * 1000
  await d.edit_message(t, new_content=f'Ping:{int(ms)}')
    
d.run(os.getenv('Token'))