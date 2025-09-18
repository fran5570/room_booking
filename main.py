from views.console_menu import user_menu, room_menu, reservation_menu
from controllers.user_controller import UserController
from data.storage import Database


def main():
    db = Database()
    controller = UserController(db)
    while True:
        print("\n=== MAIN MENU ===")
        print("1. User menu")
        print("2. Room menu")
        print("3. Reservation menu")
        print("4. Delete user")
        print("0. Exit")
        option = input("Choose an option: ")

        if option == "1":
            user_menu()
        elif option == "2":
            room_menu()
        elif option == "3":
            reservation_menu()
        elif option == "4":
            try:
                user_id = int(input("Enter user ID to delete: "))
                controller.delete_user(user_id)
            except ValueError:
                print("❌ Invalid ID.")

        elif option == "0":
            print("👋 Exiting program...")
            break
        else:
            print("⚠️ Invalid option.")


if __name__ == "__main__":
    main()
