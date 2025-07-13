from dataclasses import dataclass
from typing import List

from FileManager.CoreFunction.FileFormatABC import FileFormatABC
from UserManagment.Roles import Leadership, Sections, Instruments, RoleWrapper


@dataclass
class UserData(FileFormatABC):
    user_name: str
    email_address: str

    marching_band: bool
    marching_leadership: Leadership
    marching_section: Sections
    marching_instrument: Instruments

    concert_band: bool
    concert_leadership: Leadership
    concert_section: Sections
    concert_instrument: Instruments

    pep_band: bool
    pep_leadership: Leadership
    pep_section: Sections
    pep_instrument: Instruments

    custom_roles: List[RoleWrapper]
    version: str = "v3"