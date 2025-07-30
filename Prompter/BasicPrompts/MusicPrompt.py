from typing import List

import discord.ui

from MusicManagment.MusicManager import MusicManager
from Prompter.BasicPrompts.PromptButton import PromptButton
from UserManagment.BandMember import BandMember


class MusicPrompt:
    @staticmethod
    async def ask(band_member: BandMember, music_manager: MusicManager, band_name: str, song_name: str, prompt: str):
        involvement = None
        for involve in [band_member.user_data.pep_involvement,band_member.user_data.concert_involvement,band_member.user_data.marching_involvement]:
            if involve.band_name == band_name:
                involvement = involve
                break

        view = MusicView(await music_manager.get_song_parts(song_name, involvement.section.name))
        await band_member.member.send(prompt, view=view)
        await view.wait()
        return await music_manager.get_music(song_name, view.result)

class MusicView(discord.ui.View):
    def __init__(self, part_names: List[str]):
        super().__init__(timeout=180)
        self.result: str | None = None
        for part_name in part_names:
            self.add_item(PromptButton(label=part_name.replace("_", " "), style=discord.ButtonStyle.grey, return_value=part_name))
