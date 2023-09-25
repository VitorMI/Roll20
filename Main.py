import disnake
import random
from disnake.ext import commands

client = commands.Bot()

@client.event
async def on_ready():
    print(f"Start")

client.load_extension("Dado.Roll")

client.run()
