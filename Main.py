import disnake
import random
from disnake.ext import commands

client = commands.Bot(command_prefix="!")

@client.event
async def on_ready():
    print(f"LES FUCKING GOOOO")

client.load_extension("Dado.Roll")

client.run()