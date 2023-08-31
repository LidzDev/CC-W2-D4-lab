import unittest
from src.guest import Guest

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest_1 = Guest("John", 300)
        self.guest_2 = Guest("Keith", 5)

    def test_guest_has_name(self):
        self.assertEqual("John", self.guest_1.name)

    def test_guest_has_wallet(self):
        self.assertEqual(300, self.guest_1.wallet)

    def test_pay_with_wallet(self):
        self.guest_1.pay_with_wallet(50)
        self.assertEqual(250, self.guest_1.wallet)

    def test_check_wallet_sufficient_cash_to_pay(self):
        self.assertEqual(True, self.guest_1.check_wallet_sufficient_cash_to_pay(20))
        self.assertEqual(False, self.guest_2.check_wallet_sufficient_cash_to_pay(20))

