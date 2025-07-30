from MusicManagment.MusicManager import MusicManager
from Prompter.BasicPrompts.BoolPrompt import BoolPrompt
from Prompter.BasicPrompts.InstrumentPrompt import InstrumentPrompt
from Prompter.BasicPrompts.MusicPrompt import MusicPrompt
from Prompter.BasicPrompts.SectionPrompt import SectionPrompt
from UserManagment.BandMember import BandMember
from UserManagment.BandMemberManager import BandMemberManager
from UserManagment.UserData import UserData


class GeneralPrompt:
    @staticmethod
    async def ask(band_member: BandMember, music_manager: MusicManager, band_member_manager: BandMemberManager) -> None:
        user_data: UserData = band_member.user_data
        section = None
        if all([user_data.marching_involvement.section is None, user_data.pep_involvement.section is None, user_data.concert_involvement.section is None]):
            section = await SectionPrompt.ask(band_member, "What section do you want to declare yourself a part of? You can only be in one section.")
        else:
            for band in [user_data.marching_involvement]:#, user_data.concert_involvement, user_data.pep_involvement]:
                if band.section is not None:
                    section = band.section

        for band in [user_data.marching_involvement]:#, user_data.concert_involvement, user_data.pep_involvement]:
            participant = await BoolPrompt.ask(band_member, f"Are you going to participate in {band.band_name} band?")
            band.band_participant = participant
            if participant is False:
                continue

            band.section = section
            instrument = await InstrumentPrompt.ask(band_member, f"What instrument do you play for {band.band_name} band?")
            band.instrument = instrument
            music = []
            if band.band_name == "marching":
                for song_name in await music_manager.get_song_names("marching"):
                    new_music = await MusicPrompt.ask(band_member, music_manager, "marching", song_name, f"What part do you play for {song_name}")
                    music.append(new_music)
            band.music = music
            files = []
            for part in music:
                files.append(await music_manager.get_music_file(part))
            await band_member.member.send("Here's the music you requested!", files=files)
            await band_member.update_current_info()
            await band_member_manager.assign_member_roles(band_member)





