from typing import Dict

import discord

import Roles
from BandMember import BandMember


class RoleManager:
    def __init__(self, guild: discord.Guild):
        '''
        Possible optimization in the for loop, could combine the two inner loops, but it seems more readable without.
        '''
        self.guild = guild
        self.role_groups =  Roles.MarchingRole.__subclasses__()
        for group in self.role_groups:
            group.resolve_roles(guild)

        name_to_role: Dict[str, discord.Role] = {role.name.lower(): role for role in self.guild.roles}


    def assign_role(self, band_member: BandMember, role: Roles.RoleWrapper) -> None:
        self._check_valid(band_member, BandMember)
        self._check_valid(role, Roles.RoleWrapper)
        band_member.member.add_roles(role.raw) # role just acts like a discord.Role, we pass in the real role with .raw

    def remove_role(self, band_member: BandMember, role: Roles.RoleWrapper) -> None:
        self._check_valid(band_member, BandMember)
        self._check_valid(role, Roles.RoleWrapper)
        real_member = band_member.member
        if role.raw in real_member.roles:
            real_member.remove_roles(role.raw)
        else:
            raise Exception(f"Could not find role {role} in {band_member.name}'s roles.\n({real_member.roles})")

    def remove_category(self, band_member: BandMember, category: Roles.MarchingRole.__subclasses__()) -> None:
        roles = band_member.member.roles
        for role in category:
            if role.raw in roles:
                band_member.member.remove_roles(role.raw)


    def _check_valid(self, instance, cls) -> None:
        """
        Checks if instance is an instance of cls, or a list of classes given though cls.
        If it's not an instance of them, raise an error, else, it would have returned
        """
        if not isinstance(cls, list):
            cls = [cls]

        for cl in cls:
            if isinstance(instance, cl):
                return

        raise TypeError(f"Instance {instance} needs to be of type {cls}, not type {type(instance)}")
