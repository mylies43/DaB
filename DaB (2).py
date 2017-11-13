import discord
import sys
import time
from datetime import datetime
import asyncio
import sys
from discord.ext import commands
import random
from random import randint
import giphypop
from PingDetection import Tree
from PingDetection import checkPing

description = '''A shitty little discord bot that is mostly made for shitposting. Created by David Wolak the best programmer around'''
bot = commands.Bot(command_prefix='!', description=description)
client = discord.Client()
g = giphypop.Giphy()

pingTree = Tree()
pingTree.add("mylies43")
pingTree.add("tinlun")
pingTree.add("captainDevlin")
pingTree.add("superSoulSpark")



@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print(bot.user.discriminator)
    print('------')

  
    

    

@bot.event
async def on_message(message):#Activates when there is a message
  
    keyword = "FRICK"
    hotWords = ["FUCK","DAB"]
        
    message_split = message.content.split(' ')
    command = message_split[0]

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
                await bot.send_message(message.channel,"<@{}> SAID FRICK THAT IS A NOT ALLOWED WORD".format(message.author.id))

    
    
    if all(x in message.content.upper() for x in hotWords):# If someone says fuck you dad, or both those words together it responds with a gif of a thumbs up and you too buddy
        if message.content.upper() != "WHAT THE FUCK":
            giffy = g.translate('thumbs up')
            await bot.send_message(message.channel,"You too buddy")
            await bot.send_message(message.channel,giffy.media_url)
            
    if (message.mention_everyone):
        abuse = checkPing(message.author,pingTree)
        if(abuse == 1):
                await bot.send_message(message.channel.server.owner,"User "+ str(message.author) + "has abused their allowed amount of pings. Please take action")
                

    await bot.process_commands(message)#Needs to be at end of check word to process the rest of the commands
                
@bot.command(pass_context = True)
async def what(ctx):
    await bot.send_message(ctx.message.channel,"https://www.youtube.com/watch?v=AXzEcwYs8Eo")
    await bot.delete_message(ctx.message)

@bot.command(pass_context = True)
async def gif(ctx):

    keyWord = ctx.message.content[5:]


    if ctx.message.content[5:]:
        print("Looking for {}".format(keyWord))
        result = g.translate(keyWord)
        if result:
            await bot.send_message(ctx.message.channel,result.url)
            await bot.delete_message(ctx.message)
        else:
            await bot.send_message(ctx.message.channel,"Hmmmm, looks like theres no gifs of this, oh well")
    else:
        await bot.send_message("Opps! Look you messed up, try telling me what look up next time!") 
    print('------')

@bot.command()
async def cmd():
    await bot.say("I'll help you with the commands. Current these commands are active")
    await bot.say("!hello : Gets a responce from me")
    await bot.say("!cool  : Determines if your cool or not")
    await bot.say("!off   : Suppose to turn me off. As if thats allowed!")
    await bot.say("!gif   : Will find a perfect gif for you to use in your petty arguments")
    await bot.say("!DaB   : Provides a short description of who I am!")
    await bot.say("Plus a passive filter for filtering the word frick. Gotta keep these servers clean from sin")



@bot.command(pass_context=True)
async def hello(ctx):
        await bot.say("Hi!")

@bot.command(pass_context=True)
async def DaB(ctx):
    description = "Hello friend. I am shitty little discord bot that is mostly made for shitposting. Created by David Wolak the best programmer around, so if I mess up blame him!"
    await bot.send_message(ctx.message.channel,description)

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
    sys.exit()
    print('------')

    
#bot.close()
#sys.exit()
bot.run('MzYxNzMzNzM4MjU5OTM5MzMw.DKofTg.Sl8OgPitrmx9Bx2nWbyavhKiyac')


