async def initialize_userdata():
    current_dir = Path(__file__).parent.resolve()
    test_dir = current_dir / "SensitiveInfo" / "UserData"

    cool_song_1 = Music(music_name="Rad song bro", part_name="CENTER SNARE")
    cool_song_2 = Music(music_name="Thrilling activity", part_name="CENTER SNARE")
    cool_song_3 = Music(music_name="Lemon dude", part_name="CENTER SNARE")

    interpreter = UserDataInterpreter()
    file_manager = FileManager(interpreter, base_dir=test_dir, remote_manager=None)

    test_data = UserData("JOSE")
    test_data.email_address = "dcrobin567@gmail.com"

    test_data.marching_involvement.band_participant = True
    test_data.marching_involvement.instrument = RoleWrapper(Instruments, "", "Snare")
    test_data.marching_involvement.section = RoleWrapper(Sections, "", "Percussion")
    test_data.marching_involvement.leadership = RoleWrapper(Leadership, "", "Section Leader")
    test_data.marching_involvement.music = [cool_song_1, cool_song_2, cool_song_3]

    test_data.concert_involvement.band_participant = True
    test_data.concert_involvement.instrument = RoleWrapper(Instruments, "", "Snare")
    test_data.concert_involvement.section = RoleWrapper(Sections, "", "Percussion")
    test_data.concert_involvement.leadership = RoleWrapper(Leadership, "", "Section Leader")
    test_data.concert_involvement.music = [cool_song_1, cool_song_2, cool_song_3]

    test_data.pep_involvement.band_participant = True
    test_data.pep_involvement.instrument = RoleWrapper(Instruments, "", "Snare")
    test_data.pep_involvement.section = RoleWrapper(Sections, "", "Percussion")
    test_data.pep_involvement.leadership = RoleWrapper(Leadership, "", "Section Leader")
    test_data.pep_involvement.music = [cool_song_1, cool_song_2, cool_song_3]

    await file_manager.write("a", test_data)
    print("Hope")
    test_data_revived: UserData = await file_manager.read("a")
    print(test_data_revived)
