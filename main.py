import discord
from discord.ext import commands

from dotenv import load_dotenv

import os
import logging


load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='>', intents=intents)


@bot.command()
async def test(ctx, *, arg):
	await ctx.send(arg, file=discord.File('moneyboy.jpeg'))


@bot.command()
async def laugh(ctx):
	await ctx.send("https://www.youtube.com/watch?v=iiIPHGH8pYY&pp=ygUNemllaCB1bmQgcGFzcw%3D%3D")


@bot.command()
async def die(ctx):
	exit()

bot.run(DISCORD_TOKEN)
