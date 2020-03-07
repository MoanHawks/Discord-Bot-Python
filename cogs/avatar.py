import asyncio
import discord
import random
import datetime
from discord.ext import commands

class avatarCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def avatar(self, ctx, user: discord.Member=None):
    	if user is None:
    		user = ctx.author
    	a = discord.Colour.from_hsv(random.random(), 1, 1) # random color for embed
    	embed = discord.Embed(title="{}'s Avatar".format(user.name), color=a, timestamp=datetime.datetime.utcnow())
    	embed.set_image(url=user.avatar_url)
    	await ctx.send(embed=embed)
    	
def setup(bot):
    bot.add_cog(avatarCog(bot))
         
    