import disnake
import random
from disnake.ext import commands


class Command(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command(name= "roll")
    async def roll(inter, sides: int, rolls: int = 1):
        resultado = [random.randint(1, sides) for i in range(rolls)]
        await inter.send(f"d{sides} -> {resultado}")

def setup(bot: commands.Bot):
    bot.add_cog(Command(bot))