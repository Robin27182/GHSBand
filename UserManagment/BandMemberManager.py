from site import USER_BASE
from typing import List

import discord

from Bot.BotData import BotData
from FileManager.CoreFunction.FileManager import FileManager
from FileManager.FileImplement.FileManagerShard import FileManagerShard
from UserManagment.BandInvolvement import BandInvolvement
from UserManagment.BandMember import BandMember
from UserManagment.RoleManager import RoleManager
from UserManagment.Roles import Leadership, Sections, Instruments, Custom
from UserManagment.UserData import UserData


class BandMemberManager:
    def __init__(self, guild: discord.Guild, user_data_file_manager: FileManager, bot_data: BotData):
        self.guild = guild
        self.role_manager = RoleManager(guild)
        self.file_manager = user_data_file_manager
        self.bot_data = bot_data
        self.band_members = []

    async def get_band_member(self, member: discord.Member):
        member = self.guild.get_member(member.id) # Refers to the member in the server, not the member in the DM.
        for band_mem in self.band_members:
            if member == band_mem:
                return band_mem
        return await self.create_band_member(member)

    async def create_all_band_members(self):
        for discord_member in self.guild.members:
            await self.create_band_member(discord_member)

    async def create_band_member(self, discord_member: discord.Member) -> BandMember:
        discord_member = self.guild.get_member(discord_member.id) # Refers to the member in the server, not the member in the DM.
        if await self.file_manager.exist(discord_member.name, False):
            user_data = await self.file_manager.read(discord_member.name)
        else:
            user_data = UserData(user_name=discord_member.name)
            await self.file_manager.write(discord_member.name, user_data, True)
        file_shard = FileManagerShard(self.file_manager, discord_member.name)
        new_member = BandMember(discord_member, user_data, file_shard)
        self.band_members.append(new_member)
        return new_member

    async def assign_member_roles(self, band_member: BandMember) -> None:
        """Assigns roles to a band member based on their involvement and permissions."""
        user_data = band_member.user_data

        for category in (Leadership, Sections, Instruments, Custom):
            await self.role_manager.remove_category(band_member, category)

        involvement: List[BandInvolvement] = [
            user_data.marching_involvement if self.bot_data.marching_season else None,
            user_data.concert_involvement if self.bot_data.concert_season else None,
            user_data.pep_involvement if self.bot_data.pep_season else None,
        ]

        for band_involvement in filter(None, involvement):
            if not band_involvement.band_participant:
                continue
            for role in (band_involvement.leadership, band_involvement.section, band_involvement.instrument):
                if role is not None:
                    await self.role_manager.assign_role(band_member, role)

        for custom_role in user_data.custom_roles:
            if custom_role.name == "librarian" and band_member.id == self.bot_data.librarian_id:
                await self.role_manager.assign_role(band_member, custom_role)
            if custom_role.name == "bot manager" and band_member.id == self.bot_data.bot_manager_id:
                await self.role_manager.assign_role(band_member, custom_role)
