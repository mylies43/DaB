import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
description = '''An example bot to showcase the discord.ext.commands extension
module.'''
client  = discord.Client();
bot_prefix = "!"
client = commands.Bot(command_prefix='!')

@client.event
async def on_ready():
        print("Hello World!")

@client.command(pass_context=True)
async def hello(ctx):
        await client.say("Hi!")

client.run("MzYxNzMzNzM4MjU5OTM5MzMw.DKofTg.Sl8OgPitrmx9Bx2nWbyavhKiyac")
