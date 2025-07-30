from dataclasses import dataclass, field
from typing import List

from FileManager.FileFormatABC import FileFormatABC
from DataStructure.BandInvolvement import BandInvolvement
from UserManagment.Roles import RoleWrapper


@dataclass
class UserData(FileFormatABC):
    user_name: str
    email_address: str = None

    participation: List[BandInvolvement] = field(default_factory=list)
    custom_roles: List[RoleWrapper] = field(default_factory=list)
    version: str = "v4"