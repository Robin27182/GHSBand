
import discord.ui

from Prompter.BasicPrompts.PromptButton import PromptButton
from UserManagment.BandMember import BandMember
from UserManagment.Roles import Instruments


class InstrumentPrompt:
    @staticmethod
    async def ask(band_member: BandMember, prompt: str) -> Instruments:
        view = InstrumentView()
        await band_member.member.send(prompt, view=view)
        await view.wait()
        return view.result

class InstrumentView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=180)
        self.result: Instruments | None = None
        for instrument in Instruments:
            self.add_item(PromptButton(label=instrument.name, style=discord.ButtonStyle.grey, return_value=instrument))

