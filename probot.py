import discord
from discord.ext import commands
import asyncio
import time
import os

p=commands.Bot(command_prefix='P')

@p.event
async def on_ready():
    print(f'{p.user.name} is up.')
    await p.change_presence(game=discord.Game(name='Pro'))
    
    
p.run(os.getenv('Token'))
