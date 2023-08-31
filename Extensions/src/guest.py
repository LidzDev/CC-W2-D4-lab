class Guest:

    def __init__(self, input_name, input_wallet):
        self.name = input_name
        self.wallet = input_wallet

    def pay_with_wallet(self, input_amount):
        self.wallet -= input_amount

    def check_wallet_sufficient_cash_to_pay(self, input_amount):
        return(self.wallet >= input_amount)
