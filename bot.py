import discord
import asyncio
from discord.ext import commands
import json

with open('config.json', 'r') as config_file: #load config.json
    load = json.load(config_file)
    print(load["prefix_command"])