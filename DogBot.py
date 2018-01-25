#DogBot
#Written by Andrew Huynh

import discord
from discord.ext import commands
from discord.ext.commands import Bot 
import asyncio
import random

dogs = ['1.jpeg', '2.jpeg','3.jpeg','4.jpeg','5.jpeg','6.jpeg','7.jpeg','8.jpeg','9.jpeg','10.jpeg']

client = discord.Client()
server = client.get_server('405860470252240916')

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
	print('bot is ready')

@bot.command(pass_context=True)
async def bark(ctx):
	await bot.say("woof woof")
	print('user barked')

@bot.command(pass_context=True)
async def dog(ctx):
	ran = dogs[random.randrange(0,9,1)]
	await bot.send_file(ctx.message.channel, ran)
	print('dog sent')

@bot.command(pass_context=True)
async def commands(ctx):
	await bot.say('!dog\n!bark')


bot.run("KEY")
