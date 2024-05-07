from abc import ABC, abstractmethod

class Room(ABC):
    def __init__(self, price, room_number):
        self.price = price
        self.room_number = room_number

    @abstractmethod
    def get_price(self):
        pass

class SingleRoom(Room):
    def __init__(self, price, room_number):
        super().__init__(price, room_number)
    
    def get_price(self):
        return self.price

class DoubleRoom(Room):
    def __init__(self, price, room_number):
        super().__init__(price, room_number)
    
    def get_price(self):
        return self.price

