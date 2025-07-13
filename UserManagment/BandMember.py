import discord

from UserManagment.UserInfo import UserInfo

class BandMember:
    def __init__(self, member: discord.Member, user_info: UserInfo | None = None):
        if user_info is None: # Set to default
            user_info = UserInfo()
        if member is None:
            raise Exception(f"The member passed for {user_info.user_name} is None")
        self._user_info: UserInfo = user_info

        self.name: str = member.name
        self.nick: str | None = member.nick
        self.id: int = member.id

        self._member = member
        self._instrument: discord.Role | None = None
        self._section: discord.Role | None = None
        self._leadership: discord.Role | None = None
        self.set_user_info(user_info)

    @property
    def instrument(self) -> discord.Role:
        return self._instrument

    @property
    def section(self) -> discord.Role:
        return self._section

    @property
    def leadership(self) -> discord.Role:
        return self._leadership

    @property
    def member(self) -> discord.Member:
        return self._member

    def set_user_info(self, user_info: UserInfo) -> None:
        '''
        Sets the user_info for the BandMember, and updates the other variables
        '''
        if user_info is None: # Shouldn't happen, but a member should always have a valid user_info
            raise Exception(f"Userinfo is None for band member {self.name}")

        self._user_info = user_info
        self._instrument = user_info.instrument
        self._section = user_info.section
        self._leadership = user_info.leadership

    def get_user_info(self) -> UserInfo:
        return self._user_info