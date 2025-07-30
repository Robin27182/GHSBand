from dataclasses import dataclass
from typing import List

from DataStructure.Song import Song

@dataclass
class Band:
    id: int
    name: str
    in_season: bool
    songs: List[Song]

    def activate(self) -> None:
        self.in_season = True

    def deactivate(self) -> None:
        self.in_season = False