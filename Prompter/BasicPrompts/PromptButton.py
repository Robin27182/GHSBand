import discord


class PromptButton(discord.ui.Button):
    def __init__(self, label, style: int, return_value):
        super().__init__(label=label, style=style)
        self.return_value = return_value  # store the answer value

    async def callback(self, interaction: discord.Interaction):
        self.view.result = self.return_value
        self.view.stop()
        await interaction.response.defer()