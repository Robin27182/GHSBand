import discord.ui

from Prompter.BasicPrompts.PromptButton import PromptButton
from UserManagment.BandMember import BandMember


class BoolPrompt:
    @staticmethod
    async def ask(band_member: BandMember, prompt: str) -> bool:
        view = BoolView()
        await band_member.member.send(prompt, view=view)
        await view.wait()
        return view.result

class BoolView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=180)
        self.result: bool | None = None
        self.add_item(PromptButton(label="Yes", style=discord.ButtonStyle.green, return_value=True))
        self.add_item(PromptButton(label="No", style=discord.ButtonStyle.red, return_value=False))
        self.add_item(PromptButton(label="Undecided", style=discord.ButtonStyle.gray, return_value=None))

