import discord
from discord.ext import commands

client = commands.Bot(command_prefix="")

@client.event
async def on_ready():
    print("Bot is ready")

@client.command()
async def hello(ctx):
    await ctx.send("Hi there, I am the bot of V&P server. This is a sever made by Vihaan and Prakhar and we want you to invite more people..")

client.run("Nzk1ODgxMzIxODc2MTYwNTIy.X_P0PQ.eP1YRXbu6pRcFpk7apUQ_cwdRxA")