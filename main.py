import discord
import os
from discord.ext import commands

bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    print(F"Logged in as {bot.user}")

@bot.command()
async def echo(ctx):
    await ctx.send(ctx.message.content)

@bot.command()
async def birthday(ctx, arg1):
    if arg1 == "set":
        await ctx.send(F"You passed the argument {arg1}")

bot.run(os.environ.get("TOKEN", ""))