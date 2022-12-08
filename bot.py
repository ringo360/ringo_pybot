#import discord
#import discord.app_commands
#
#client = discord.Client()
#tree = discord.app_commands.CommandTree(client) 
#intents = discord.Intents.default()
#intents.message_content = True
#bot = commands.Bot(command_prefix="d.", intents=intents)


import discord
from discord import commands,Permissions
import colorama,random
from colorama import Fore, init, Back, Style
import os

os.system("cls")

token = "token"



bot = commands.Bot(command_prefix="!", help_command=None, intents=discord.Intents.all())

@tree.command(
    name="slashtest",
    description="python is easy? = Idk LOL"
)

async def hoge(ctx:discord.Interaction):
	await ctx.responce.send_message("This is Python bot! :D")

@bot.command(name="test")
async def testcmd(ctx):
	await ctx.send(f"{ctx.message.author.name}ｻﾝ, ｺﾝﾆﾁﾊｧｧｧ!")

@client.event
async def on_ready():
    print(Fore.LIGHTBLUE_EX + Back.BLACK + "ringoxd's pybot is ready!")
client.run(token)