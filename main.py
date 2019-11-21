import discord
import os
import datetime
from discord.ext import commands

bot = commands.Bot(command_prefix="!")
users = []

@bot.event
async def on_ready():
    print(F"Logged in as {bot.user}")

@bot.command()
async def echo(ctx):
    await ctx.send(ctx.message.content)

@bot.command()
async def birthday(ctx, *args):
    if args[0] == "set":
        #await ctx.send(F"You passed the argument {args[0]}")
        d = datetime.date(2019, args[2], args[1])
        await ctx.send(F"The date you set is {d}")

bot.run(os.environ.get("TOKEN", ""))