class Room:

    def __init__(self, input_name, input_capacity):
        self.name = input_name
        self.capacity = input_capacity
        self.singers = []
        self.songs = []

    def add_guest(self, input_guest):
        self.singers.append(input_guest.name)

    def kick_guest(self, input_guest):
        self.singers.remove(input_guest.name)

    def add_song(self, input_song):
        self.songs.append(input_song)