import json
from dataclasses import fields
from io import BytesIO

import discord

from Bot.BotData import BotData
from FileManager.CoreFunction.FileInterpreterABC import FileInterpreterABC


class MusicInterpreter(FileInterpreterABC):
    """Assume the files exist"""
    @property
    def extension(self) -> str:
        return ".pdf"

    def write(self, formatted: BotData) -> str:
        """
        :param formatted: the implemented FileFormat
        :return: a string to directly write to the file
        """
        raise Exception("This is intended to be a read-only implementation of Filemanager")

    def read(self, pdf_bytes: bytes) -> discord.file:
        """
        :param file_contents: the raw contents of the written file
        :return: the expected implementation of FileFormatABC
        """
        file_stream = BytesIO(pdf_bytes)
        discord_file = discord.File(fp=file_stream, filename="Default.pdf")
        return discord_file