from room import SingleRoom, DoubleRoom

class Hotel:
    
    def __init__(self, name):
        self.name = name
        self.rooms = {}

    def add_room(self, room):
        self.rooms[room.room_number] = room
