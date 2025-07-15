from dataclasses import asdict

import discord

from Bot.BotData import BotData
from FileManager.FileImplement.FileManagerShard import FileManagerShard
from UserManagment.BandInvolvement import BandInvolvement
from UserManagment.UserData import UserData


class BandMember:
    def __init__(self, member: discord.Member, user_data: UserData, file_manager_shard: FileManagerShard):
        if not isinstance(member, discord.Member):
            raise TypeError(f"Member is of the wrong type. It is type {type(member)}.")

        if not isinstance(user_data, UserData):
            raise TypeError(f"user data is of the wrong type. It is type {type(user_data)}.")

        if not isinstance(file_manager_shard, FileManagerShard):
            raise TypeError(f"File manager shard is of the wrong type. It is type {type(file_manager_shard)}.")


        # We do not want to be reassigning any of these
        self._member = member
        self._user_data = user_data
        self._file_manager_shard = file_manager_shard

    @property
    def member(self):
        return self._member

    @property
    def id(self):
        return self._member.id

    @property
    def user_data(self):
        return self._user_data

    def __getattr__(self, item):
        return getattr(self.user_data, item)

    async def update_current_info(self):
        await self._file_manager_shard.write(self.user_data, False)