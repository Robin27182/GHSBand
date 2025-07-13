from typing import List

from MusicManagment.Part import Part
from UserManagment.BandMember import BandMember
from UserManagment.UserData import UserData


class MusicManager:
    ...

    def update_music(self, *args) -> None:
        ...

    def get_parts(self, user_data: UserData) -> List[Part]:
        ...

