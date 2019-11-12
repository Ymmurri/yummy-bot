import discord
import config

class MyClient(discord.Client):
    async def on_ready(self):
        print(F"Logged on as {self.user}")

client = MyClient()
client.run(config.token)