import hashlib
from io import BytesIO
from typing import List

import discord

from Bot.BotData import BotData
from DataStructure.Band import Band
from DataStructure.Music import Part
from DataStructure.Song import Song
from FileManager.FileManager import FileManager
from MusicManagment.DropboxManager import DropboxManager
from pathlib import Path

from UserManagment.Roles import Sections, RoleWrapper


class MusicManager:
    def __init__(self, guild: discord.Guild, bot_data: BotData, bot_data_manager: FileManager, dropbox_manager: DropboxManager):
        self.bot_data = bot_data # Needed to update the music.
        self.bot_data_manager = bot_data_manager
        self.dropbox_manager = dropbox_manager
        self.guild = guild

    async def update_music(self):
        self.bot_data.bands = []
        all_files = await self.dropbox_manager.list_all_files()

        all_band_names: List[str] = []
        all_bands: List[Band] = []
        #Combine the band name and the song, that way if two bands have the same song, they are treated as such.
        all_bandsong_names: List[str] = []

        for file_path in all_files:
            path = Path(file_path)

            # Shouldn't happen, check to see if the file is a pdf.
            if path.suffix.lower() != ".pdf":
                continue

            # The structure is category/song_name/section/file.pdf
            divisions = path.parts
            if len(divisions) < 3:
                continue  # Not deep enough, ignore

            band_name = divisions[0].lower()
            song_name = divisions[1].lower()
            section_name = divisions[2].lower()
            pdf_name = path.stem # Could use divisions[3], just easier to remove .pdf

            part_names = pdf_name.split("-")[1:]

            band: Band = None
            song: Song = None
            section: RoleWrapper = Sections.get_role_by_name(section_name)
            parts: List[Part] = []

            band_id: int = self._make_id(band_name)
            song_id: int = self._make_id(band_name + song_name)

            for part_name in part_names:
                part_id = self._make_id(band_name + song_name + part_name)
                parts.append(Part(part_id, part_name, song_id, section.id))

            if (band_name + song_name) in all_bandsong_names:
                print((band_name + song_name), all_bandsong_names)
                song = self.get_song(song_id)
                song.parts.extend(parts)
            else:
                all_bandsong_names.append(band_name + song_name)
                song = Song(song_id, song_name, band_id, parts)

            # Assign bands
            if band_name in all_band_names:
                band = self.get_band(band_id)
                band.songs.append(song)
            else:
                all_band_names.append(band_name)
                band = Band(band_id, band_name, False, [song])
                self.bot_data.bands.append(band)

        await self.bot_data_manager.write(str(self.guild.id), self.bot_data)

    def get_band(self, id: int):
        for band in self.bot_data.bands:
            if band.id == id:
                return band

        raise ValueError("Given ID does not match any Band ID in bot_data.bands")


    def get_song(self, id: int):
        for band in self.bot_data.bands:
            for song in band.songs:
                if song.id == id:
                    return song

        raise ValueError("Given ID does not match any Song ID in bot_data.bands.songs")


    def get_part(self, id: int):
        for band in self.bot_data.bands:
            for song in band.songs:
                for part in song.parts:
                    if part.id == id:
                        return part

        raise ValueError("Given ID does not match any Part ID in bot_data.bands.songs.parts")

    def _make_id(self, name) -> int:
        hash_bytes = hashlib.sha1(name.encode()).digest()
        return int.from_bytes(hash_bytes[:8], 'big')  # 8 bytes = 64-bit int