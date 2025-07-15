from dataclasses import dataclass

from FileManager.CoreFunction.FileFormatABC import FileFormatABC

@dataclass
class BotData(FileFormatABC):
    marching_season: bool
    concert_season: bool
    pep_season: bool

    bot_manager_id: str
    bot_manager_gmail: str

    librarian_id: int
    librarian_gmail: int

    version: str = "v1"