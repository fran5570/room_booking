from data.storage import Database


class UserController:
    def __init__(self, db: Database):
        self.conn = db.get_connection()

    def create_user(self, name: str, email: str):
        cursor = self.conn.cursor()
        try:
            cursor.execute(
                "INSERT INTO users (name, email) VALUES (?, ?)", (name, email)
            )
            self.conn.commit()
            print("✅ User created successfully.")
        except Exception as e:
            print("❌ Error creating user:", e)

    def list_users(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()
        if users:
            print("\n📋 List of users:")
            for user in users:
                print(f"[{user[0]}] {user[1]} - {user[2]}")
        else:
            print("⚠️ No users found.")

    def get_user_by_id(self, user_id: int):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM users WHERE user_id = ?", (user_id,))
        user = cursor.fetchone()
        if user:
            return user
        else:
            print("⚠️ User not found.")
            return None

    def delete_user(self, user_id: int):
        try:
            cursor = self.conn.cursor()
            cursor.execute("DELETE FROM users WHERE user_id = ?", (user_id,))
            self.conn.commit()
            print("🗑️ Usuario eliminado correctamente.")
        except Exception as e:
            print("❌ Error deleting user:", e)
