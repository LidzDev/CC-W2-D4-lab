import unittest
from src.guest import Guest

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest = Guest("John", 300)

    def test_guest_has_name(self):
        self.assertEqual("John", self.guest.name)

    def test_guest_has_wallet(self):
        self.assertEqual(300, self.guest.wallet)

    def test_pay_with_wallet(self):
        self.guest.pay_with_wallet(50)
        self.assertEqual(250, self.guest.wallet)
