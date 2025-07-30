import json
from dataclasses import fields, asdict

from Bot.BotData import BotData
from FileManager.FileInterpreterABC import FileInterpreterABC


class BotDataInterpreter(FileInterpreterABC):
    """Assume the files exist"""
    @property
    def extension(self) -> str:
        return ".json"

    def write(self, formatted: BotData) -> str:
        """
        :param formatted: the implemented FileFormat
        :return: a string to directly write to the file
        """
        return json.dumps(asdict(formatted), indent=4)

    def read(self, file_contents: str) -> BotData:
        """
        :param file_contents: the raw contents of the written file
        :return: the expected implementation of FileFormatABC
        """
        data = json.loads(file_contents)
        field_names = {f.name for f in fields(BotData)}
        filtered_data = {k: v for k, v in data.items() if k in field_names}

        # Convert music lists of dicts into lists of Music objects
        for music_field in ["marching_music", "concert_music", "pep_music"]:
            if music_field in filtered_data:
                music_list = filtered_data[music_field]
                filtered_data[music_field] = 1
            else:
                print(filtered_data)

        return BotData(**filtered_data)