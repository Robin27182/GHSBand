import discord
from discord import app_commands

class CommandRegistry:
    def __init__(self, config):
        """
        Weird implementation to get the constants in, discord doesn't like commands that have "self."
        :param config:
        """
        self.config = config
        self.registered_commands: list[app_commands.Command] = []

        for attr_name in dir(self):
            attr = getattr(self, attr_name)
            if hasattr(attr, "__app_command__"): # Iterates through all functions that have @slash_command
                meta = attr.__app_command__
                cmd = app_commands.Command( # These are defined in the decorator itself, with "func.__app_command__ ="
                    name=meta["name"],
                    description=meta["description"],
                    callback=attr # We actually get to run the function now.
                )
                self.registered_commands.append(cmd)

    @staticmethod
    def slash_command(name: str, description: str):
        def decorator(func):
            func.__app_command__ = {"name": name, "description": description}
            return func

        return decorator

    @slash_command(name="example", description="Don't worry about it")
    async def example_command(self, interaction: discord.Interaction):
        print("yeah this works")

    @slash_command(name="die", description="Don't about it")
    async def new_command(self, interaction: discord.Interaction):
        print("yeah this worksadasdasdds")

    @slash_command("makedavidskinny", "Not happening")
    async def skinny_command(self, interaction: discord.Interaction):
        await interaction.response.send_message("David lost 100lbs! Just a few more to go!")

    @slash_command("hollyeatsfood", "Not happening")
    async def holly_command(self, interaction: discord.Interaction):
        await interaction.response.send_message("Holly has inflated??? mass hath been added")

    @slash_command("meganinflation", "Not happening")
    async def megan_command(self, interaction: discord.Interaction):
        await interaction.response.send_message("Megan eats 1 million burgers, light work")