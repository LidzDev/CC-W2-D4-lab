class Room:

    def __init__(self, input_name, input_capacity, input_entry_fee, input_till):
        self.name = input_name
        self.capacity = input_capacity
        self.entry_fee = input_entry_fee
        self.till = input_till
        self.singers = []
        self.songs = []

    def add_guest(self, input_guest):
        if self.check_capacity():
            self.singers.append(input_guest.name)
            self.charge_entry(input_guest)

    def kick_guest(self, input_guest):
        self.singers.remove(input_guest.name)

    def add_song(self, input_song):
        self.songs.append(input_song)

    def check_capacity(self):
        return (len(self.singers) <  self.capacity)
    
    def charge_entry(self, input_guest):
        if (input_guest.check_wallet_sufficient_cash_to_pay(self.entry_fee)):
                input_guest.pay_with_wallet(self.entry_fee)
                self.till += self.entry_fee


