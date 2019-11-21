import discord
import os
from discord.ext import commands

bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    print(F"Logged in as {bot.user}")

@bot.command()
async def echo(ctx):
    await ctx.send(ctx.message);

bot.run(os.environ.get("TOKEN", ""))