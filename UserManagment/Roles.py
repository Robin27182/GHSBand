from abc import ABC
import discord

class RoleWrapper:
    """
    Simple wrapper class for the discord.Role object
    TO WORK WITH DISCORD API, CALL .raw
    """
    def __init__(self, category, role: discord.Role, name: str) -> None:
        self._role = role
        self.name = name
        self.category = category

    def __getattr__(self, attr):
        return getattr(self._role, attr)

    def __str__(self):
        return str(self._role)

    @property
    def raw(self):
        return self._role

class RoleMeta(type):
    """Allows MarchingRole to be iterable"""
    def __iter__(cls):
        for attr in cls._roles:
            yield getattr(cls, attr)

class MarchingRole(ABC, metaclass=RoleMeta):
    """
    This is an abstract class. DO NOT MAKE AN INSTANCE OF THIS
    The metaclass just allows inheriting instances to be iterable.
    All inheriting classes are expected to have _roles, and the class variables associated
    _roles follows the format "Name in class": "Name that discord can find"
    """
    @classmethod
    def resolve_roles(cls, guild: discord.Guild):
        for attr_name, role_name in cls._roles.items():
            role = discord.utils.get(guild.roles, name=role_name)
            if role is None:
                raise ValueError(f"Role '{role_name}' not found in guild.")
            wrapped = RoleWrapper(cls, role, role_name)
            setattr(cls, attr_name, wrapped)


class Instruments(MarchingRole):
    """
    All variables are type RoleWrapper at runtime, excepting _roles, which is how they are assigned at runtime
    _roles follows the format "Name in class": "Name that discord can find"
    """
    _roles = {
        "flute": "flute",
        "clarinet": "clarinet",
        "alto_sax": "alto sax",
        "tenor_sax": "tenor sax",
        "trumpet": "trumpet",
        "horn": "horn",
        "trombone": "trombone",
        "baritone": "baritone",
        "tuba": "tuba",
        "snare": "snare",
        "tenors": "tenors",
        "bass": "bass",
        "tambourine": "tambourine",
        "cymbals": "cymbals",
    }
    flute = None
    clarinet = None
    alto_sax = None
    tenor_sax = None
    trumpet = None
    horn = None
    trombone = None
    tuba = None
    snare = None
    tenors = None
    bass = None
    tambourine = None
    cymbals = None

class Sections(MarchingRole):
    """
    All variables are type RoleWrapper at runtime, excepting _roles, which is how they are assigned at runtime
    _roles follows the format "Name in class": "Name that discord can find"
    """
    _roles = {
        "percussion": "percussion",
        "brass": "brass",
        "woodwind": "woodwind",
        "color_guard": "color guard",
    }
    percussion = None
    brass = None
    woodwind = None
    color_guard = None

class Leadership(MarchingRole):
    """
    All variables are type RoleWrapper at runtime, excepting _roles, which is how they are assigned at runtime
    _roles follows the format "Name in class": "Name that discord can find"
    """
    _roles = {
        "director": "director",
        "drum_major": "drum major",
        "section_leader": "section leader",
        "head_quartermaster": "head quartermaster",
        "quartermaster": "quartermaster",
        "player": "player",
    }
    director = None
    drum_major = None
    section_leader = None
    head_quartermaster = None
    quartermaster = None
    player = None

class Custom(MarchingRole):
    """
    All variables are type RoleWrapper at runtime, excepting _roles, which is how they are assigned at runtime
    _roles follows the format "Name in class": "Name that discord can find"
    """
    _roles = {
        "librarian" : "librarian",
        "minecraft_server_owner" : "minecraft server owner"
    }
    librarian = None
    minecraft_server_owner = None

'''
# ---- TEST CODE ----
if __name__ == "__main__":
    class MockRole:
        def __init__(self, name):
            self.name = name

        def __str__(self):
            return f"<Role name={self.name}>"

    class MockGuild:
        def __init__(self, role_names):
            self.roles = [MockRole(name) for name in role_names]

    # Simulate a guild with all required roles
    mock_guild = MockGuild([
        "flute", "clarinet", "alto sax", "tenor sax", "trumpet", "horn", "trombone", "baritone", "tuba",
        "snare", "tenors", "bass", "tambourine", "cymbals",
        "percussion", "brass", "woodwind", "color guard",
        "director", "drum major", "section leader", "head quartermaster", "quartermaster", "librarian", "player"
    ])

    # Patch discord.utils.get for this test context
    import discord.utils
    discord.utils.get = lambda roles, name: next((r for r in roles if r.name == name), None)

    # Resolve and print to test
    Instruments.resolve_roles(mock_guild)
    Sections.resolve_roles(mock_guild)
    Leadership.resolve_roles(mock_guild)

    print("Instruments.flute:", Instruments.flute)
    print("Sections.brass:", Sections.brass)
    print("Leadership.director:", Leadership.director)
'''