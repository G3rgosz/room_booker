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
        print() 

        if choice == '1':
            room_number = int(input("Szobaszám: "))
            booking_date = input("Dátum (YYYY-MM-DD): ")
            result = booking.book(room_number, date.fromisoformat(booking_date), hotel)
            print(result)
        elif choice == '2':
            room_number = int(input("Szobaszám: "))
            booking_date = input("Dátum (YYYY-MM-DD): ")
            result = booking.cancel_booking(room_number, date.fromisoformat(booking_date))
            print(result)
        elif choice == '3':
            print(booking.list_bookings())
        elif choice == '4':
            print("Kilépés a programból.")
            break
        else:
            print("Érvénytelen választás. Próbálja újra.")

if __name__ == "__main__":
    loader()
    user_interface()