import json
from dataclasses import asdict

from UserManagment.UserData import UserData
from DataStructure.BandInvolvement import BandInvolvement
from UserManagment.Roles import RoleWrapper, Leadership, Sections, Instruments, Custom

from FileManager.FileInterpreterABC import FileInterpreterABC


class UserDataInterpreter(FileInterpreterABC):
    @property
    def extension(self) -> str:
        return ".json"

    def _rolewrapper_to_dict(self, role: RoleWrapper | None) -> dict | None:
        if role is None:
            return None
        # Store category name and role name (string)
        return {
            "category": role.category.__name__ if role.category else None,
            "name": role.name
        }

    def _dict_to_rolewrapper(self, data: dict | None) -> RoleWrapper | None:
        if data is None:
            return None
        category_name = data.get("category")
        role_name = data.get("name")

        category_cls = {
            "Leadership": Leadership,
            "Sections": Sections,
            "Instruments": Instruments,
            "Custom": Custom,
        }.get(category_name, None)

        if category_cls is None:
            return None

        return category_cls.get_role_by_name(role_name)

    def _band_involvement_to_dict(self, bi: BandInvolvement) -> dict:
        return {
            "band_name": bi.band_name,
            "band_participant": bi.band_participant,
            "leadership": self._rolewrapper_to_dict(bi.leadership),
            "section": self._rolewrapper_to_dict(bi.section),
            "instrument": self._rolewrapper_to_dict(bi.instrument),
            "music": [asdict(m) for m in bi.music] if bi.music else []
        }

    def _dict_to_band_involvement(self, data: dict) -> BandInvolvement:
        music_list = data.get("music", [])
        music_objs = 1
        return BandInvolvement(
            band_name=data.get("band_name"),
            band_participant=data.get("band_participant"),
            leadership=self._dict_to_rolewrapper(data.get("leadership")),
            section=self._dict_to_rolewrapper(data.get("section")),
            instrument=self._dict_to_rolewrapper(data.get("instrument")),
            music=music_objs
        )

    def write(self, formatted: UserData) -> str:
        # Convert UserData to dict including nested structures
        data = {
            "user_name": formatted.user_name,
            "email_address": formatted.email_address,
            "version": formatted.version,
            "marching_involvement": self._band_involvement_to_dict(formatted.marching_involvement),
            "concert_involvement": self._band_involvement_to_dict(formatted.concert_involvement),
            "pep_involvement": self._band_involvement_to_dict(formatted.pep_involvement),
            "custom_roles": [self._rolewrapper_to_dict(r) for r in formatted.custom_roles]
        }
        return json.dumps(data, indent=4)

    def read(self, file_contents: str) -> UserData:
        data = json.loads(file_contents)
        user = UserData(
            user_name=data.get("user_name"),
            email_address=data.get("email_address"),
        )
        user.version = data.get("version", "v3")
        user.marching_involvement = self._dict_to_band_involvement(data.get("marching_involvement", {}))
        user.concert_involvement = self._dict_to_band_involvement(data.get("concert_involvement", {}))
        user.pep_involvement = self._dict_to_band_involvement(data.get("pep_involvement", {}))
        user.custom_roles = [self._dict_to_rolewrapper(r) for r in data.get("custom_roles", [])]
        return user
