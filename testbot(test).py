 #Copyright © by Dabs Yt™ 2018-2018.

#1.Import

#12/10/2018 14:32
import discord
from discord.ext import commands
import asyncio
import random

#2.Configure prefix

#10/10/2018 23:39
bot=commands.Bot(command_prefix='D')

#3.Startup message.

#10/10/2018 23:00
@bot.event
async def on_ready():
	print('The bot is up!')
	print('Name:'+ bot.user.name)
	print('Id:' + bot.user.id)
	print('~~~~~~~~~~')

#4.Basic commands.

#Ping
@bot.command()
async def ping():
	await bot.say('I got pinged!\n:ping_pong:')
	
#Spam [tag] [msg] [times]
@bot.command(pass_context=True)
async def spam(ctx,person:discord.Member,message:str,times:int):
	for i in range(times):
		await bot.say(f'<@{person.id}>' + ' ' + message)
		
#Choose [str] [str]
@bot.command()
async def choose(*choices : str):
	await bot.say(random.choice(choices))

@bot.command(pass_context=True)
async def give():
	give = 10,9,8,7,6,5,4,3,2,1
	await bot.say(random.choice(give))

#3.All of the mathematical stuff.

#Multiply [num] [num]
@bot.command(pass_context=True)
async def multiply(ctx,a : int,b : int):
	await bot.say(a * b)
	
#Divide [num] [num]
@bot.command(pass_context=True)
async def divide(ctx,a : int,b : int):
	await bot.say(a / b)
	
#Minus [num] [num]
@bot.command(pass_context=True)
async def minus(ctx,a : int,b : int):
	await bot.say(a - b)
	
#Add [num] [num]
@bot.command(pass_context=True)
async def add(ctx,a : int,b : int):
	await bot.say(a + b)


bot.run('NDgzOTE5MzU4NjIwNTk4Mjcz.Dp-77w.jdKFgbfoK4hDakSUWEMoq6dLM3U')