
import discord.ui

from Prompter.BasicPrompts.PromptButton import PromptButton
from UserManagment.BandMember import BandMember
from UserManagment.Roles import Sections


class SectionPrompt:
    @staticmethod
    async def ask(band_member: BandMember, prompt: str) -> Sections:
        view = SectionView()
        await band_member.member.send(prompt, view=view)
        await view.wait()
        return view.result

class SectionView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=180)
        self.result: Sections | None = None
        for section in Sections:
            self.add_item(PromptButton(label=section.name, style=discord.ButtonStyle.grey, return_value=section))

