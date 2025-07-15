from dataclasses import dataclass, field, asdict
from typing import List

from FileManager.CoreFunction.FileFormatABC import FileFormatABC
from MusicManagment.Music import Music
from UserManagment.BandInvolvement import BandInvolvement
from UserManagment.Roles import Leadership, Sections, Instruments, RoleWrapper


@dataclass
class UserData(FileFormatABC):
    user_name: str
    email_address: str = None

    marching_involvement: BandInvolvement = field(default_factory=lambda: BandInvolvement(band_name="marching"))
    concert_involvement: BandInvolvement = field(default_factory=lambda: BandInvolvement(band_name="concert"))
    pep_involvement: BandInvolvement = field(default_factory=lambda: BandInvolvement(band_name="pep"))

    custom_roles: List[RoleWrapper] = field(default_factory=list)
    version: str = "v3"