import discord
from discord.ext import commands
import asyncio
import random
import time
from time import perf_counter


class pingCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        stre = self.bot.latency * 1000
        a = discord.Colour.from_hsv(random.random(), 1, 1) #random color embed
        em = discord.Embed(title=f'Pong\nBot Latency: {int(stre)}ms', colour=a)
        await ctx.send(embed=em)


def setup(bot):
    bot.add_cog(pingCog(bot))
