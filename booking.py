from datetime import date

class Booking:
    def __init__(self):
        self.bookings = {}
    
    def book(self, room_number, booking_date, hotel):
        if booking_date <= date.today():
            return "A dátum érvénytelen. Kérjük, jövőbeli dátumot adjon meg."
        if room_number not in hotel.rooms:
            return "A szoba nem létezik a szállodában."
        if (room_number, booking_date) in self.bookings:
            return "Ez a szoba már foglalt erre a dátumra."
        self.bookings[(room_number, booking_date)] = hotel.rooms[room_number].get_price()
        return f"Foglalás rögzítve. Ár: {hotel.rooms[room_number].get_price()} Ft"

    def cancel_booking(self, room_number, booking_date):
        if (room_number, booking_date) in self.bookings:
            del self.bookings[(room_number, booking_date)]
            return "Foglalás lemondva."
        return "Nem létező foglalás."

    def list_bookings(self):
        if not self.bookings:
            return "Nincsenek foglalások."
        return '\n'.join([f"Szobaszám: {k[0]}, Dátum: {k[1]}, Ár: {v} Ft" for k, v in self.bookings.items()])
