#ringoXD python bot

import discord
from discord import commands,Permissions
import colorama,random
from colorama import Fore, init, Back, Style
import os

os.system("cls")

token = "token"
client = discord.Client()
bot = commands.Bot(command_prefix="r!", help_command=None, intents=discord.Intents.all())

#======================================================

#Ready Event
@client.event
async def on_ready():
    print(Fore.LIGHTBLUE_EX + Back.BLACK + "ringoxd's pybot is ready!")
client.run(token)

@client.event
async def on_message(message):
	if message.author.bot:
		return
	if message.content == "!help":
		await message.channel.send("作成中")