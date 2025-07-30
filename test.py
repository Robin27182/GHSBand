import hashlib
import json
import uuid
from dataclasses import asdict

from DataStructure.Band import Band
from DataStructure.Music import Part
from DataStructure.Song import Song
'''
band_id = "bandid1"
part1 = Part("partid1", "snare", "id1", "1234")
part2 = Part("partid2", "flute", "id1", "4321")
song1 = Song("id1","sunkist", "band_id1", [part1, part2])

part3 = Part("partid3", "flute", "id2", "1")
part4 = Part("partid4", "clarinet", "id2", "1")

song2 = Song("id2","sunkist", "band_id1", [part1, part2])


a = Band(band_id, "marching", [song1,song2])
print(json.dumps(asdict(a), indent=4))
'''

def generate_song_id(song_name: str) -> int:
    # Use a consistent hash and convert to an integer


print(generate_song_id("freebird"))