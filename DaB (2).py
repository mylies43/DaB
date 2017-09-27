import discord
import sys
from datetime import datetime
import asyncio
import sys
from discord.ext import commands
import random
from random import randint

description = '''An example bot to showcase the discord.ext.commands extension
module.

There are a number of utility commands being showcased here.'''
bot = commands.Bot(command_prefix='!', description=description)
client = discord.Client()

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print(bot.user.discriminator)
    print('------')

@bot.event
async def on_message(message):
    keyword = "FRICK"
    
    print(message.content)
    print('message is from channel {} by {}'.format(message.channel,message.author))
    if message.author.discriminator != bot.user.discriminator:
       print("Not created by bot")
       if keyword in message.content.upper():
                await bot.send_file(message.channel,'frick.jpg')
                await bot.send_message(message.channel,"YOU SAID FRICK")
    await bot.process_commands(message)
               
    print('------')

@bot.command(pass_context=True)
async def hello(ctx):
        await bot.say("Hi!")

@bot.command(pass_context=True)
async def cool(ctx):
        print('Cool Command Invoked')
        rando = randint(0,1)
        print('Rando is {}'.format(rando))
        userName = ctx.message.author
        if(rando > 0.5):
            await bot.say("{} is not cool".format(userName))
        else:
            await bot.say("{} is cool".format(userName))
        print('------')


        
@bot.command()
async def off():
    print('Turning off')
    discord.Client.logout
    await bot.say("ah guess its bedtime. Good night!")
    print('Goodbye')
    print('------')

    
#bot.close()
#sys.exit()
bot.run('MzYxNzMzNzM4MjU5OTM5MzMw.DKofTg.Sl8OgPitrmx9Bx2nWbyavhKiyac')


