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
    print('message is from channel {} by {}'.format(message.channel,message.author.display_name))
    if message.author.discriminator != bot.user.discriminator:
       print("Not created by bot")
       if keyword in message.content.upper():
                rando = randint(1,3)
                if rando == 1:
                    image = 'frick.jpg'
                elif rando ==2:
                    image = 'frick2.jpg'
                elif rando == 3:
                    image = 'frick3.png'
                    
                await bot.send_file(message.channel,image)
                await bot.send_message(message.channel,"YOU SAID FRICK")
    await bot.process_commands(message)
               
    print('------')

@bot.command(pass_context=True)
async def hello(ctx):
        await bot.say("Hi!")

@bot.command(pass_context=True)
async def cool(ctx):
        print('Cool Command Invoked')
     
        userName = ctx.message.author
        coolFactor = int(userName.discriminator)

        if(ctx.message.author.discriminator == "#3888"):
            await bot.say("Hell YEAH this boy tight")
        else:
            print("{} asked for command".format(ctx.message.author.discriminator))
            if(coolFactor % 2 == 1):
                await bot.say("{} is not cool".format(userName))
            else:
                await bot.say("{} is cool".format(userName))
        print('------')


        
@bot.command()
async def off():
    print('Turning off')
    bot.logout
    await bot.say("ah guess its bedtime. Good night!")
    print('Goodbye')
    print('------')

    
#bot.close()
#sys.exit()
bot.run('MzYxNzMzNzM4MjU5OTM5MzMw.DKofTg.Sl8OgPitrmx9Bx2nWbyavhKiyac')


