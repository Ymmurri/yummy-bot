import discord
import os

class MyClient(discord.Client):
    async def on_ready(self):
        print(F"Logged on as {self.user}")

client = MyClient()
client.run(os.environ.get("TOKEN", ""))