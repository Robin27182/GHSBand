from Bot.BotData import BotData
from FileManager.CoreFunction.FileInterpreterABC import FileInterpreterABC
from UserManagment.UserData import UserData


class UserDataInterpreter(FileInterpreterABC):
    """Assume the files exist"""
    @property
    def extension(self) -> str:
        return ".json"

    def write(self, formatted: BotData) -> str:
        """
        :param formatted: the implemented FileFormat
        :return: a string to directly write to the file
        """
        ...

    def read(self, file_contents: str) -> BotData:
        """
        :param file_contents: the raw contents of the written file
        :return: the expected implementation of FileFormatABC
        """
        ...