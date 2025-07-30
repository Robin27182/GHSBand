from dataclasses import dataclass

from UserManagment.Roles import Sections


@dataclass
class Part:
    id: int
    name: str
    songID: int
    sectionID: int