import dropbox
from typing import List
from dropbox.files import WriteMode
#TODO Review
class DropboxManager:
    def __init__(self, access_token: str):
        self.dbx = dropbox.Dropbox(access_token)

    async def list_all_files(self) -> List[str]:
        """Recursively list all file paths (including subfolders)."""
        result = self.dbx.files_list_folder("", recursive=True)
        files = []

        while True:
            for entry in result.entries:
                if isinstance(entry, dropbox.files.FileMetadata):
                    files.append(entry.path_display.lstrip("/"))
            if result.has_more:
                result = self.dbx.files_list_folder_continue(result.cursor)
            else:
                break

        return files

    async def download_file_bytes(self, path: str) -> bytes:
        """Download a file from Dropbox and return its content as bytes."""
        metadata, response = self.dbx.files_download("/" + path)
        return response.content
