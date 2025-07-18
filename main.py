from views.console_menu import user_menu, room_menu, reservation_menu

def main():
    while True:
        print("\n=== MAIN MENU ===")
        print("1. User menu")
        print("2. Room menu")
        print("3. Reservation menu")
        print("0. Exit")
        option = input("Choose an option: ")

        if option == "1":
            user_menu()
        elif option == "2":
            room_menu()
        elif option == "3":
            reservation_menu()
        elif option == "0":
            print("👋 Exiting program...")
            break
        else:
            print("⚠️ Invalid option.")

# 👇 Esto ejecuta el menú al correr python main.py
if __name__ == "__main__":
    main()
