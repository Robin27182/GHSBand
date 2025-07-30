from dataclasses import dataclass
from typing import List

from DataStructure.Band import Band
from FileManager.FileFormatABC import FileFormatABC


@dataclass
class BotData(FileFormatABC):
    bands: List[Band]

    bot_manager_id: int
    bot_manager_gmail: str

    librarian_id: int
    librarian_gmail: str

    version: str = "v1"