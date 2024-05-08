from datetime import date
from hotel import Hotel
from room import SingleRoom, DoubleRoom
from booking import Booking

hotel = Hotel("Best Hotel")
booking = Booking()

def loader():
    hotel.add_room(SingleRoom(5000, 101))
    hotel.add_room(DoubleRoom(8000, 102))
    hotel.add_room(SingleRoom(6000, 103)) 

    booking.book(101, date.fromisoformat("2024-08-08"), hotel)
    booking.book(102, date.fromisoformat("2024-08-17"), hotel)
    booking.book(103, date.fromisoformat("2024-08-29"), hotel)
    booking.book(101, date.fromisoformat("2024-09-01"), hotel)
    booking.book(102, date.fromisoformat("2024-10-10"), hotel)

def user_interface():
    print(f"\nÜdvözöljük a {hotel.name} foglalási rendszerében!")

    while True:
        print("\n1 - Szoba foglalása")
        print("2 - Foglalás lemondása")
        print("3 - Foglalások listázása")
        print("4 - Kilépés\n")

        choice = input("Kérjük, válasszon egy opciót: ")

        if choice == '1':
            while True:
                try:
                    hotel.list_rooms()
                    room_number = int(input("\nVálasztott szobaszám: "))
                    booking_date = input("Dátum (YYYY-MM-DD): ")
                    booking_date = date.fromisoformat(booking_date)
                    if booking_date < date.today():
                        raise ValueError("A dátum nem lehet a mai napnál korábbi.")
                    break
                except ValueError as e:
                    print(f"Hiba: {e}\nKérjük, adjon meg helyes adatokat.\n")
            result = booking.book(room_number, booking_date, hotel)
            print(result)
        elif choice == '2':
            while True:
                try:
                    room_number = int(input("\nSzobaszám: "))
                    booking_date = input("Dátum (YYYY-MM-DD): ")
                    booking_date = date.fromisoformat(booking_date)
                    if booking_date < date.today():
                        raise ValueError("A dátum nem lehet a mai napnál korábbi.")
                    break
                except ValueError as e:
                    print(f"Hiba: {e}\nKérjük, adjon meg helyes adatokat.\n")
            result = booking.cancel_booking(room_number, booking_date)
            print(result)
        elif choice == '3':
            print(f"\n{booking.list_bookings()}")
        elif choice == '4':
            print("\nKilépés a programból.")
            break
        else:
            print("\nÉrvénytelen választás. Próbálja újra.")

if __name__ == "__main__":
    loader()
    user_interface()