import discord
import asyncio
from discord.ext import commands

d=commands.Bot(command_prefix='D')
Token='NTAxMTI1Njk2ODc0MDg2NDEw.Ds2z-A.KFtoPlt6sNfbgXxdxhOaO-Pikw0'

@d.event
async def on_ready():
  print('Bot is up!')

@d.event
async def on_command_error(er,ctx):
  c=ctx.message.channel
  if isinstance(er,commands.errors.CommandInvokeError):
    await d.send_message(c,'Missing permissions!')
    
  if isinstance(er,commands.errors.BadArgument):
    await d.send_message(c,'Invalid arguements!')
    
@d.event
async def on_member_join(member):
  c=ctx.message.channel
  
  await d.send_message(c,member,'has just joined us!')
 
@d.command()
async def ping():
  await d.say('pong')
  
@d.command(pass_context=True)
async def kick(ctx,tag:discord.Member):
  p=ctx.message.author
  if ctx.message.author.server_permissions.administrator:
    await d.kick(tag)
    await d.say(tag,'is kicked.')
  
@d.command(pass_context=True)
async def ban(ctx,tag:discord.Member):
  p=ctx.message.author
  if ctx.message.author.server_permissions.administrator:
    await d.ban(tag)
    await d.say(tag,'is banned.')
    
d.remove_command('help')
@d.command(pass_context=True)
async def prset(ctx,t1:str,t2:int):
  if t2 > 3 or t2 < 0:
    await d.say('Type must be 0-3!')
  else:
    await d.change_presence(game=discord.Game(name=t1,type=t2))
    await d.say('Success!')
	
d.run(Token)