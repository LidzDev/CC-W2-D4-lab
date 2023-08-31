import unittest
from src.room import Room

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room_1 = Room("Black Room")

    def test_room_has_name(self):
        self.assertEqual("Black Room", self.room_1.name)