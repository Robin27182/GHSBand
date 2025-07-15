from dataclasses import dataclass
from typing import List

from MusicManagment.Music import Music
from UserManagment.Roles import RoleWrapper


@dataclass
class BandInvolvement:
    """
    Please do not assign "leadership" to a role not in Leadership, and same with all the others.
    """
    band_name: str
    band_participant: bool = None
    leadership: RoleWrapper | None = None
    section: RoleWrapper | None = None
    instrument: RoleWrapper | None = None
    music: List[Music] | None = None

