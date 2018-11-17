import discord
from time import localtime,strftime
from discord.ext import commands
import asyncio
import random
import time

tr=strftime('%d/%m/%Y %H:%M:%S',localtime())
d=commands.Bot(command_prefix='D')

@d.event
async def on_ready():
  servers=list(d.servers)
  start=time.time()
  slt=300,600,900
  print('-------------------------')
  print('Bot is up!')
  print('Name:',d.user.name)
  print('Servers:',str(len(d.servers)))
  print('Users:',str(len(set(d.get_all_members()))))
  print('-------------------------')
  for x in range(9999):
    time.sleep(60)
    end=time.time()
    temp=end-start
    mins=temp//60
    print('Bot is up for %d minutes'%(mins))
  
@d.event
async def on_command_error(er,ctx):
  c=ctx.message.channel
  p=ctx.message.author
  if isinstance(er,commands.errors.MissingRequiredArgument):
    await d.send_message(c,'You entered invalid arguements.')
    return
  elif isinstance(er,commands.errors.BadArgument):
    await d.send_message(c,'Bad arguements error!')
    return
  elif isinstance(er,commands.errors.CommandNotFound):
    return
  elif isinstance(er,commands.errors.TooManyArguments):
    await d.send_message(c,'Too many arguements!')
    return
  elif isinstance(er,commands.errors.CommandError):
    await d.send_message(c,'Error on command execution! Please report the bug at Dabs Yt#5590!')
    return 
  elif isinstance(er,commands.errors.UserInputError):
    await d.send_message(c,'Invalid input!')
    return
  elif isinstance(er,commands.errors.DiscordException):
    await d.say('There was an exception! Please try again!')
    return 

d.remove_command('help')
@d.command(pass_context=True)
async def help(ctx):
 p=ctx.message.author
 c=ctx.message.channel
 t=strftime('%d/%m/%Y %H:%M:%S',localtime())
 e1=discord.Embed(color=0x800000)
 e1.add_field(name='Dpresence [text] [type]',value='Changes the bot presence text and type!')
 e1.add_field(name='Dpinfo [tag]',value='Gives you info about a person.')
 e1.add_field(name='Dcinfo',value='Gives info about the current channel')
 e1.add_field(name='Dinvite',value='Gives you a link to invite the bot!')
 e1.add_field(name='Doffers',value='All the bot offers![Soon]')
 e1.set_footer(text='Sent at '+t)
 await d.send_message(p,embed=e1)
 print(p,'used help')
 
@d.command(pass_context=True)
async def presence(ctx,t1:str,t2:int):
  c=ctx.message.channel
  p=ctx.message.author
  t=strftime('%d/%m/%Y %H:%M:%S',localtime())
  await d.change_presence(game=discord.Game(name=t1,type=t2))
  await d.say('**Success!**')

@d.command(pass_context=True)
async def offers(ctx):
  await d.say('**I am selling premium for 5$!Soon linked paypal..**')
  
@d.command(pass_context=True)
async def pinfo(ctx,name:discord.Member):
	person = ctx.message.author
	channel = ctx.message.channel
	pname = f'{name.name}'
	pid = f'{name.id}'
	ptag = f'{name.mention}'
	pcreated = f'{name.created_at}'
	pdisplay= f'{name.display_name}'
	
	pmsg = '**\nName:' + pname + '\nId:' + pid + '\nTag:' + ptag + '\nAccount created at:' + pcreated + '\nServer name:' + pdisplay + '**'
	await d.say(pmsg)
	
@d.command(pass_context=True)
async def cinfo(ctx):
  p=ctx.message.author
  c=ctx.message.channel
  cname=f'#{c.name}'
  cserver=f'{c.server}'
  cid=f'{c.id}'
  ctopic=f'{c.topic}'
  ccreated=f'{c.created_at}'
  ctype=f'{c.type}'
  
  cmsg='**\nName:' + cname + '\nId:' + cid + '\nTopic:' + ctopic + '\nCreated at:' + ccreated + '\nType:' + ctype + '**'
  await d.say(cmsg)

@d.command(pass_context=True)
async def invite(ctx):
  p=ctx.message.author
  await d.send_message(p,'Invite me using this link:https://discordapp.com/api/oauth2/authorize?client_id=501125696874086410&permissions=8&scope=bot')

d.run(os.getenv('Token'))
