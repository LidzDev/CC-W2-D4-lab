import unittest
from src.guest import Guest

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest = Guest("John", 300)

    def test_guest_has_name(self):
        self.assertEqual("John", self.guest.name)

    def test_guest_has_wallet(self):
        self.assertEqual(300, self.guest.wallet)
