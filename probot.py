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
  if isinstance(er,commands.errors.CommandNotFound):
    await d.say('Command not found!')

@d.command()
async def ping():
  await d.say('pong')
  
d.run(Token)