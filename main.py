import json
import discord
from discord.ext import tasks
from discord.ext import commands
import pymysql.cursors


#read config file
with open('config/config.json', 'r') as file:
    configFile = json.load(file)

prefix = configFile["prefix"]
token = configFile["token"]
host = configFile["host"]
user = configFile["user"]
password = configFile["password"]
database = configFile["database"]


client = discord.Client()
bot = commands.Bot(command_prefix=prefix)

@bot.event
async def on_ready():
    connection = pymysql.connect(host=host,
                                 user=user,
                                 password=password,
                                 database=database,
                                 cursorclass=pymysql.cursors.DictCursor)

