import discord
import asyncio
from discord.ext import commands
import json
import os
from time import strftime,localtime
from datetime import datetime
import time
import platform
import datetime

d=commands.Bot(command_prefix='D')
os.chdir(r'/storage/sdcard0/.backups/Discord/Bots')
start_time=time.time()

async def playing():
 while True:
  for x in range(999999):
    await d.change_presence(game=discord.Game(name='Made by Dabs Gt#5590!!'))
    await asyncio.sleep(18)
    await d.change_presence(game=discord.Game(name='Servers:'+str(len(d.servers))+'  Users:'+str(len(set(d.get_all_members())))))
    await asyncio.sleep(18)
    await d.change_presence(game=discord.Game(name='24/7 Online Everyday!'))
    await asyncio.sleep(18)
    
@d.event
async def on_ready():
  print('Bot is up!')
  d.loop.create_task(playing())
  
@d.event
async def on_member_join(user):
  with open('users.json','r') as f:
    users=json.load(f)
    
  await update_data(users,user)
  
  with open('users.json','w') as f:
    json.dump(users,f)
    
@d.event
async def on_message(message):
  if message.author==d.user:
    return 0
  with open('users.json','r') as f:
    users=json.load(f)
    await update_data(users,message.author)
    await add_experience(users,message.author,5)
    await level_up(users,message.author,message.channel)
  with open('users.json','w') as f:
     json.dump(users,f)
    
  await d.process_commands(message)
  
@d.event
async def on_member_join(user):
  with open('users.json','r') as f:
    users=json.load(f)
    await update_data(users,user)
  with open('users.json','w') as f:
    json.dump(users,f)
    
async def update_data(users,user):
  if not user.id in users:
    users[user.id]={}
    users[user.id]['experience']=0
    users[user.id]['level']=1
    
async def add_experience(users,user,exp):
  users[user.id]['experience']+=exp
  
async def level_up(users,user,channel):
  experience=users[user.id]['experience']
  lvl_start=users[user.id]['level']
  lvl_end=int(experience**(1/5))
  if lvl_start < lvl_end:
    await d.send_message(channel,f'Congrats {user.mention} you are now level {lvl_end}!')
    users[user.id]['level']=lvl_end
    
async def reset(users,user,channel):
  users[user.id]['experience']=0
  users[user.id]['level']=1
  await d.send_message(channel,'Your stats have been reset!')
  
@d.command(pass_context=True)
async def ping():
  await d.say('Pongo!')
  
@d.command()
async def time():
  t=strftime('%d/%m/%Y %H:%M:%S',localtime())
  await d.say(t)
	
@d.command(pass_context=True)
async def hostinfo(ctx):
  p = ctx.message.author
  t = await d.send_message(p,'Calculating...')
  ms = (t.timestamp-ctx.message.timestamp).total_seconds() * 1000
  await d.delete_message(t)
  pingt=f'{int(ms)}'

  e3=discord.Embed(title='Host info!',color=0x765400)
#  current_time = time.time()
#  difference = int(round(current_time - start_time))
#  text = str(datetime.timedelta(seconds=difference))
  #e3.add_field(name='Uptime',value=text,inline=True)
  e3.add_field(name='Ping',value=pingt,inline=True)
  e3.add_field(name='Platform',value=platform.system(),inline=True)
  e3.add_field(name='Platform Name',value=os.name,inline=True)
  e3.add_field(name='Python Version',value=platform.python_version(),inline=True)
  e3.add_field(name='Discord Version',value=discord.__version__,inline=True)
  e3.set_footer(text='Made by Dabs Gt#5590!')
  await d.send_message(p,embed=e3)
  
d.run(os.getenv('Token'))
