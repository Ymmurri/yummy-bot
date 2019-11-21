import discord
import os
import datetime
from discord.ext import commands

bot = commands.Bot(command_prefix="!")

users = []

class usr():
    def __init__(self, user):
        self.user = user
        self.name = user.name
    
    def __hash__(self):
        return hash(self.user.hash())

    def __repr__(self):
        return self.user.id
    
    def setBirthday(self, bday):
        self.birthday = bday

def addUser(user):
    for u in users:
        if u.user.id == user.id:
            print("about to break")
            return
    users.append(usr(user))

@bot.event
async def on_ready():
    print(F"Logged in as {bot.user}")
"""
@bot.event
async def on_message(message):
    await addUser(message.author)
"""
@bot.command()
async def echo(ctx):
    await ctx.send(ctx.message.content)

@bot.command()
async def birthday(ctx, *args):
    if args[0] == "set":
        print("Setting birthday")
        addUser(ctx.author)
        d = datetime.date(2019, int(args[2]), int(args[1]))
        print(d)
        for u in users:
            print(u)
            if u.user == ctx.author:
                u.setBirthday(d)
                await ctx.send(F"{u.user.name} has the birthday of {u.birthday}")

@bot.command()
async def listUsers(ctx):
    await ctx.send(users)

        

bot.run(os.environ.get("TOKEN", ""))