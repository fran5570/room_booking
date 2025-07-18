from data.storage import Database
from controllers.user_controller import UserController
from controllers.room_controller import RoomController
from controllers.reservation_controller import ReservationController


def user_menu():
    db = Database()
    user_controller = UserController(db)

    while True:
        print("\n=== USER MENU ===")
        print("1. Create user")
        print("2. List users")
        print("3. Get user by ID")
        print("0. Back to main menu")
        option = input("Choose an option: ")

        if option == "1":
            name = input("Enter name: ")
            email = input("Enter email: ")
            user_controller.create_user(name, email)

        elif option == "2":
            user_controller.list_users()

        elif option == "3":
            try:
                user_id = int(input("Enter user ID: "))
                user = user_controller.get_user_by_id(user_id)
                if user:
                    print(f"✅ Found: {user[1]} - {user[2]}")
            except ValueError:
                print("❌ Invalid ID format.")

        elif option == "0":
            break

        else:
            print("⚠️ Invalid option.")

def room_menu():
    db = Database()
    room_controller = RoomController(db)

    while True:
        print("\n=== ROOM MENU ===")
        print("1. Create room")
        print("2. List rooms")
        print("3. Get room by ID")
        print("0. Back to main menu")
        option = input("Choose an option: ")

        if option == "1":
            name = input("Enter room name: ")
            try:
                capacity = int(input("Enter capacity: "))
                room_controller.create_room(name, capacity)
            except ValueError:
                print("❌ Invalid capacity format.")

        elif option == "2":
            room_controller.list_rooms()

        elif option == "3":
            try:
                room_id = int(input("Enter room ID: "))
                room = room_controller.get_room_by_id(room_id)
                if room:
                    print(f"✅ Found: {room[1]} - Capacity: {room[2]}")
            except ValueError:
                print("❌ Invalid ID format.")

        elif option == "0":
            break

        else:
            print("⚠️ Invalid option.")


def reservation_menu():
    print(">> Debug: entering reservation menu")

    db = Database()
    reservation_controller = ReservationController(db)
    user_controller = UserController(db)
    room_controller = RoomController(db)

    while True:
        print("\n=== RESERVATION MENU ===")
        print("1. Create reservation")
        print("2. List all reservations")
        print("3. List reservations by user")
        print("4. List reservations by room")
        print("0. Back to main menu")
        option = input("Choose an option: ")

        if option == "1":
            user_controller.list_users()
            try:
                user_id = int(input("Enter user ID: "))
            except ValueError:
                print("❌ Invalid user ID.")
                continue

            room_controller.list_rooms()
            try:
                room_id = int(input("Enter room ID: "))
            except ValueError:
                print("❌ Invalid room ID.")
                continue

            date = input("Enter date (YYYY-MM-DD): ")
            start = input("Start time (HH:MM): ")
            end = input("End time (HH:MM): ")
            reservation_controller.create_reservation(user_id, room_id, date, start, end)

        elif option == "2":
            reservation_controller.list_reservations()

        elif option == "3":
            try:
                user_id = int(input("Enter user ID: "))
                reservation_controller.list_reservations_by_user(user_id)
            except ValueError:
                print("❌ Invalid user ID.")

        elif option == "4":
            try:
                room_id = int(input("Enter room ID: "))
                reservation_controller.list_reservations_by_room(room_id)
            except ValueError:
                print("❌ Invalid room ID.")

        elif option == "0":
            break

        else:
            print("⚠️ Invalid option.")

