import discord
from discord import Member, app_commands
from discord.ext import commands
import logging
from dotenv import load_dotenv

import os


load_dotenv()
token = os.getenv("DISCORD_TOKEN")

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='/', intents=intents)
guild = None

@bot.event
async def on_ready():
    """
    Because we need to talk to discord, we need the bot set up, so that's why there are declarations here
    We are assuming that the server has resorted to primitive states. Fix everything to match files
    """
    global guild
    guild = bot.guilds[0] # Bad, but other methods were not working



@bot.event
async def on_member_join(member: Member):
    ...

@bot.event
async def on_message(message):
    ...

@bot.event
async def on_member_update(before: discord.member, after: discord.member):
    ...

@bot.tree.command(name="swapper", description="Pick your section.")
@app_commands.guilds(discord.Object(id=server_id))
async def _swapper_command(interaction: discord.Interaction):
    ...

bot.run(token, log_handler=handler, log_level=logging.DEBUG)