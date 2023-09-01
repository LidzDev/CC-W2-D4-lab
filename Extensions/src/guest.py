class Guest:

    def __init__(self, input_name, input_wallet, input_fav_song):
        self.name = input_name
        self.wallet = input_wallet
        self.fav_song = input_fav_song

    def pay_with_wallet(self, input_amount):
        self.wallet -= input_amount

    def check_wallet_sufficient_cash_to_pay(self, input_amount):
        return(self.wallet >= input_amount)

    def check_for_fav_song(self, input_playlist): 
        if self.fav_song in input_playlist:
            return("Whooo")

