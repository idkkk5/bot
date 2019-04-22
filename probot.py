import discord
import asyncio
from discord.ext import commands
import os
from time import strftime,localtime
from datetime import datetime
import time
import random

p=commands.Bot(command_prefix='P',pm_help=True)
start=time.time()
TOKEN=os.getenv('Token')
dabs='533956824005869589'

async def playing():
 while True:
  for x in range(999999):
    await p.change_presence(game=discord.Game(name='Made by Dabs Yt#7312'))
    await asyncio.sleep(15)
    await p.change_presence(game=discord.Game(name='Users:'+str(len(set(p.get_all_members())))))
    await asyncio.sleep(15)
    now=time.time()
    secs=int(now-start)
    mins=int(secs//60)
    await p.change_presence(game=discord.Game(name=f'Uptime is {mins} minutes.'))
    await asyncio.sleep(15)
    
@p.event
async def on_ready():
  print('Bot is up!')
  p.loop.create_task(playing())
  
@p.event
async def on_member_join(member):
    role = discord.utils.get(member.server.roles,name="Dab Member")
    await p.add_roles(member, role)

#@p.command(pass_context=True)
#async def ping():
#  await p.say('Why you ping me boi????')

p.remove_command('help')
@p.command(pass_context=True)
async def help(ctx):
    t=strftime('%d/%m/%Y %H:%M:%S',localtime())
    e=discord.Embed(color=0xFF00FF)
    e.add_field(name='Help',value='Shows this message')
    e.add_field(name='Pinfo [tag]',value='Shows info about a member.')
    e.add_field(name='Pmsg [#channel] [message]',value='Sends a message to a desired channel [OWNER ONLY]')
    e.add_field(name='Pavatar [tag]',value='Gives you a link to an avatar of a member.')
    e.set_footer(text=f'Sent at {t}')
    await p.send_message(ctx.message.author,embed=e)

@p.command(pass_context=True)
async def info(ctx,m:discord.Member):
    t=strftime('%d/%m/%Y %H:%M:%S',localtime())
    e=discord.Embed(title=f'Info for {m}',color=0x500000)
    e.add_field(name='Name',value=m.name)
    e.add_field(name='Created at',value=m.created_at)
    e.add_field(name='Name on this server',value=m.display_name)
    e.set_footer(text=f'Sent at {t}')
    await p.say(embed=e)
    
@p.command(pass_context=True)
async def msg(ctx,c:discord.Channel,*,m:str):
    if ctx.message.author.id==(dabs):
     await p.send_message(c,m)
     await p.say('Success ✓')
    else:
     await p.say(f'No permission, {ctx.message.author.mention}.')

@p.command(pass_context=True)
async def avatar(ctx,u:discord.Member=None):
    if u==p.user:
        await p.say(f'{u.mention} uses a default avatar.')
    else:
        await p.say(f'Link: {u.avatar_url}')

p.run(TOKEN)
