from ast import Delete
from email import message
from urllib import response

import discord
from discord.ext import commands

bot = commands.Bot("!")


@bot.event
async def on_ready():
    print("Bot is running...")


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return()
    await bot.process_commands(message)


@bot.command(name="hi")
async def say_hi(ctx):
    name = ctx.author.name
    response = f'Hello {name}'
    await ctx.send(response)


@bot.command(name="bye")
async def end_convo(ctx):
    name = ctx.author.name
    response = f'Goodbye {name}'
    await ctx.send(response)


botKeyFile = open("BotKey.txt")

bot.run(botKeyFile.read())
