import sys
import threading
from http.server import HTTPServer
from views.console_menu import user_menu, room_menu, reservation_menu
from controllers.user_controller import UserController
from controllers.health_controller import HealthHandler
from controllers.responses_controller import ResponsesHandler
from data.storage import Database


class CombinedHandler(HealthHandler, ResponsesHandler):
    """Combina los endpoints HTTP de health y responses."""
    pass


def run_http_server(port=8000):
    """Inicia el servidor HTTP."""
    server_address = ("", port)
    httpd = HTTPServer(server_address, CombinedHandler)
    print(f"🌐 Servidor HTTP corriendo en http://localhost:{port}")
    httpd.serve_forever()


def main_console():
    """Ejecución del programa en modo consola."""
    db = Database()
    controller = UserController(db)
    while True:
        print("\n=== MAIN MENU ===")
        print("1. User menu")
        print("2. Room menu")
        print("3. Reservation menu")
        print("4. Delete user")
        print("5. Run HTTP server")
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
        elif option == "5":
            print("🚀 Starting HTTP server in background thread...")
            thread = threading.Thread(target=run_http_server, daemon=True)
            thread.start()
        elif option == "0":
            print("👋 Exiting program...")
            sys.exit(0)
        else:
            print("⚠️ Invalid option.")


if __name__ == "__main__":
    main_console()
