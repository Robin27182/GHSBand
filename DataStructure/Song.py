from dataclasses import dataclass
from typing import List

from DataStructure.Music import Part


@dataclass
class Song:
    id: int
    name: str
    bandID: int
    parts: List[Part]