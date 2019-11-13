import discord
import os
from discord.ext import commands

bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    print(F"Logged in as {bot.user}")

bot.run(os.environ.get("TOKEN", ""))