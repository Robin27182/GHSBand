from collections import abc

import discord.ui

from UserManagment.BandMember import BandMember


class Prompt(abc):
    def __init__(self) -> None:
        pass

    class PromptView(discord.ui.View):
        def __init__(self):
            super().__init__(timeout=180)
            pass