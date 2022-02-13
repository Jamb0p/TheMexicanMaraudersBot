import json
import discord
from discord.ext import tasks
from discord.ext import commands

#read config file
with open('config/config.json', 'r') as file:
    configFile = json.load(file)

prefix = configFile["prefix"]
token = configFile["token"]

client = discord.Client()
bot = commands.Bot(command_prefix=prefix)

