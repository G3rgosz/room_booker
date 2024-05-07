from room import SingleRoom, DoubleRoom

class Hotel:

    def __init__(self, name):
        self.name = name
        self.rooms = {}

    def add_room(self, room):
        self.rooms[room.room_number] = room

    def list_rooms(self):
        if not self.rooms:
            print("Jelenleg nincsenek szobák a szállodában.")
        else:
            print("Szobák listája:")
            for room_number, room in self.rooms.items():
                print(f"Szobaszám: {room_number}, Ár: {room.get_price()} Ft")
