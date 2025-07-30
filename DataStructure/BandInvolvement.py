from dataclasses import dataclass
from typing import List

from DataStructure.Band import Band
from UserManagment.Roles import Sections, Instruments, Leadership

@dataclass
class BandInvolvement:
    bandID: int
    leadership: Leadership
    section: Sections
    instrument: Instruments
    parts: List[str] # List of part IDs

    def belongs_to(self, band: Band) -> bool:
        if band.id == self.bandID:
            return True
        return False
