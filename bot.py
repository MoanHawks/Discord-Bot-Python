import discord
import asyncio
from discord.ext import commands
import json

with open('config.json', 'r') as config_file: # load config.json
    load = json.load(config_file)
    prefix = load["prefix_command"]
    token = load["token"]

bot = commands.Bot(command_prefix=prefix)

initial_extensions = ['cogs.ping','cogs.avatar'] # simple cogs command

if __name__ == '__main__':
    for extension in initial_extensions:
        bot.load_extension(extension)


@bot.event
async def on_ready():
    print("bot is run")

bot.run(token)
