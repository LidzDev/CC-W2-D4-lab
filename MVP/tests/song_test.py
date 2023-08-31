import unittest
from src.song import Song

class TestSong(unittest.TestCase):

    def setUp(self):
        self.song_1 = Song("Fake It", "Seether")

    def test_song_has_name(self):
        self.assertEqual("Fake It", self.song_1.name)
    
    def test_song_has_artist(self):
        self.assertEqual("Seether", self.song_1.artist)