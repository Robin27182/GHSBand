from typing import Type

import discord
from discord import Member
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os
from pathlib import Path

from Bot.BotData import BotData
from Bot.CommandRegistry import CommandRegistry
from FileManager.FileInterpreterABC import FileInterpreterABC
from FileManager.FileManager import FileManager
from Bot.BotDataInterpreter import BotDataInterpreter
from UserManagment.UserDataInterpreter import UserDataInterpreter
from MusicManagment.DropboxManager import DropboxManager
from MusicManagment.MusicManager import MusicManager

from UserManagment.BandMemberManager import BandMemberManager
from UserManagment.Roles import Instruments, Sections, Leadership, Custom

load_dotenv(dotenv_path=Path(__file__).parent / "SensitiveInfo" / ".env")

token = os.getenv("DISCORD_TOKEN")
dropbox_token = os.getenv("DROPBOX_TOKEN")

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='/', intents=intents)
guild = None  # Will be assigned on_ready

current_dir = Path(__file__).parent.resolve()




@bot.event
async def on_ready():
    global guild
    guild = bot.guilds[1]
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")
    Instruments.resolve_roles(guild)
    Sections.resolve_roles(guild)
    Leadership.resolve_roles(guild)

    sensitive_dir = current_dir / "SensitiveInfo"

    user_data_interpreter: Type[FileInterpreterABC] = UserDataInterpreter()
    user_data_manager: FileManager = FileManager(user_data_interpreter,
                                                 base_dir=sensitive_dir/"UserData",
                                                 remote_manager=None)

    bot_data_interpreter: Type[FileInterpreterABC] = BotDataInterpreter()
    bot_data_manager = FileManager(bot_data_interpreter,
                                   base_dir=sensitive_dir/"BotData",
                                    remote_manager=None)

    bot_data = BotData(bands=[],
                       bot_manager_id=871479113796444182,
                       librarian_id=871479113796444182,
                       bot_manager_gmail="",
                       librarian_gmail="")

    await bot_data_manager.write(str(guild.id), bot_data)




    bot_data: BotData = await bot_data_manager.read(str(guild.id))

    dropbox_manager = DropboxManager(dropbox_token)
    music_manager = MusicManager(guild, bot_data, bot_data_manager, dropbox_manager)
    await music_manager.update_music()
    '''
    print("start update")
    await music_manager.update_music()
    print("end update")
    files = []
    for song_name in await music_manager.get_song_names("marching"):
        print(f"\n{song_name}")
        print( (await music_manager.get_song_parts(song_name, "percussion"))[2])
        part = (await music_manager.get_song_parts(song_name, "percussion"))[2]
        print(await music_manager.get_music(song_name, part))
        music = await music_manager.get_music(song_name, part)
        files.append(await music_manager.get_music_file(music))

    channel = bot.get_channel(1382375540647923832)
    await channel.send("I love you!", files=files)
    '''


    band_member_manager = BandMemberManager(guild, user_data_manager, bot_data)
    await band_member_manager.create_all_band_members()

    await music_manager.update_music()

    command_registry = CommandRegistry(band_member_manager, music_manager)
    for cmd in command_registry.registered_commands:
        bot.tree.add_command(cmd, guild=discord.Object(id=guild.id))

    await bot.tree.sync(guild=guild)
    #me = await band_member_manager.get_band_member(guild.get_member(bot_data.bot_manager_id))
    #await me.wipe_info()
    print("stop waiting idiot")

def resolve_all_roles(guild: discord.Guild):
    Leadership.resolve_roles(guild)
    Sections.resolve_roles(guild)
    Instruments.resolve_roles(guild)
    Custom.resolve_roles(guild)

@bot.event
async def on_member_join(member: Member):
    pass


@bot.event
async def on_message(message):
    pass


@bot.event
async def on_member_update(before: discord.Member, after: discord.Member):
    pass


bot.run(token, log_handler=handler, log_level=logging.DEBUG)
