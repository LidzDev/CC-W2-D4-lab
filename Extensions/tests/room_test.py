import unittest
from src.room import Room
from src.guest import Guest
from src.song import Song
class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room_1 = Room("Black Room", 5, 10, 500)
        self.room_2 = Room("Red Room", 2, 20, 400)
        self.guest_1 = Guest("John", 300)
        self.guest_2 = Guest("Jack", 10)
        self.guest_3 = Guest("Morag", 50)
        self.song_1 = Song("Fake It", "Seether")
        self.song_2 = Song("Nemo", "Nightwish")
        self.song_3 = Song("Leaves", "the Gathering")
        # self.singers = []
        # self.songs = []

    def test_room_has_name(self):
        self.assertEqual("Black Room", self.room_1.name)
        self.assertEqual("Red Room", self.room_2.name)

    def test_room_has_capacity_number(self):
        self.assertEqual(5, self.room_1.capacity)
        self.assertEqual(2, self.room_2.capacity)

    def test_room_has_entry_fee(self):
        self.assertEqual(10, self.room_1.entry_fee)

    def test_room_can_add_guest(self):
        self.assertEqual(True, self.room_2.check_capacity())
        self.room_2.add_guest(self.guest_1)
        self.room_2.add_guest(self.guest_2)
        self.room_2.add_guest(self.guest_3)
        self.assertEqual(False, self.room_2.check_capacity())       

    def test_add_guest(self):
        self.room_1.add_guest(self.guest_1)
        self.assertEqual(1, len(self.room_1.singers))
        self.assertEqual("John", self.room_1.singers[0])

    def test_add_multiple_guests(self):
        self.room_1.add_guest(self.guest_1)
        self.assertEqual(1, len(self.room_1.singers))
        self.room_1.add_guest(self.guest_2)
        self.assertEqual("John", self.room_1.singers[0])
        self.assertEqual("Jack", self.room_1.singers[1])

    def test_kick_guest(self):
        self.room_1.add_guest(self.guest_3)
        self.assertEqual("Morag", self.room_1.singers[0])
        self.room_1.kick_guest(self.guest_3)
        self.assertEqual(0, len(self.room_1.singers))

    def test_kick_multiple_guests(self):
        self.room_1.add_guest(self.guest_1)
        self.room_1.add_guest(self.guest_2)
        self.room_1.add_guest(self.guest_3)
        self.assertEqual(3, len(self.room_1.singers))
        self.room_1.kick_guest(self.guest_2)
        self.room_1.kick_guest(self.guest_3)
        self.assertEqual("John", self.room_1.singers[0])

    def test_add_songs(self):
        self.room_1.add_song(self.song_1)
        self.room_2.add_song(self.song_1)
        self.room_2.add_song(self.song_2)
        self.assertEqual(1, len(self.room_1.songs))
        self.assertEqual(2, len(self.room_2.songs))
        self.assertEqual("Fake It", self.room_1.songs[0].name)
        self.assertEqual("Nightwish", self.room_2.songs[1].artist)
