import discord
import asyncio
from discord.ext import commands
import json
import os

d=commands.Bot(command_prefix='D')
Token='NTAxMTI1Njk2ODc0MDg2NDEw.Ds2z-A.KFtoPlt6sNfbgXxdxhOaO-Pikw0'
os.chdir(r'/storage/sdcard0/.backups/Discord/Bots')
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
    
#@d.event
#async def on_command_error(er,ctx):
  c=ctx.message.channel
  if isinstance(er,commands.errors.CommandInvokeError):
    await d.send_message(c,'Missing permissions!')
    
  if isinstance(er,commands.errors.BadArgument):
    await d.send_message(c,'Invalid arguements!')
 
@d.command(pass_context=True)
async def ping(ctx):
  await d.say(':ping_pong: Hi')
  
@d.command(pass_context=True)
async def expinfo(ctx,users,user):
  p=ctx.message.author
  c=ctx.message.channel
  e2=discord.Embed(title='Experience levels',color=0x678000)
  e2.add_field(name='Id',value=users[user.id])
  e2.add_field(name='Experience',value=users[user.id]['experience'])
  e2.add_field(name='Level',value=users[user.id]['level'])
  await d.send_message(p,e2=embed)
  
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
    
d.run(Token)